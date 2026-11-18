#!/usr/bin/env python
"""Small thematic figures for Research cards that have no photograph.

Both figures are ILLUSTRATIONS generated from simple formulas. They contain no data
and no result from any manuscript or from the dryhic project:

    fountain_toy.png    a synthetic Hi-C map: power-law contact decay plus three
                        "fountain" jets, Poisson-sampled so it looks like a sparse
                        single map. Illustrates the kind of structure dryhic aims to
                        score; it is not dryhic output.
    atac_schematic.png  a nucleosome array with one nucleosome-depleted region,
                        Tn5 insertion marks and the read-coverage peak they produce.

Usage:  python figures/make_thematic_figures.py
Requires: numpy, scipy, matplotlib.
"""
from __future__ import annotations

import pathlib

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.patches import Circle, Polygon  # noqa: E402
from scipy.ndimage import gaussian_filter, map_coordinates  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
BACKGROUND = "#0c0f14"  # same ink as the hero (css --hero-ink)
RAMP = ["#0c0f14", "#1f0e0c", "#4a150d", "#86240f", "#b8401a", "#e66a37", "#f9a273", "#ffe3cf"]
CMAP = LinearSegmentedColormap.from_list("ember", RAMP, N=1024)
W, H = 1600, 1000  # 2x of a 800x500 card image (16:10)


def fountain_toy(out: pathlib.Path, seed: int = 7) -> None:
    rng = np.random.default_rng(seed)
    n = 320
    i, j = np.indices((n, n))
    s = np.abs(j - i).astype(float)
    mid = (i + j) / 2
    expected = (s + 1.0) ** -1.05
    jets = np.zeros_like(expected)
    for anchor, amp, spread in [(70, 1.0, 0.10), (165, 1.4, 0.07), (255, 0.8, 0.12)]:
        width = 1.5 + spread * s  # jet widens with distance from the diagonal
        jets += amp * np.exp(-((mid - anchor) ** 2) / (2 * width**2)) * (s + 1.0) ** -0.55
    lam = expected * (1 + 7.0 * jets) * 2500.0
    counts = rng.poisson(lam).astype(float)
    counts = gaussian_filter(counts, 0.9)
    logm = np.log10(counts + 0.3)

    scale = W / n
    tri_h = int(scale * n / 2)
    px = (np.arange(W) + 0.5) / scale
    py = (np.arange(tri_h)[::-1] + 0.5) / scale
    x, y = np.meshgrid(px, py)
    band = map_coordinates(logm, [x - y, x + y], order=1, mode="constant", cval=np.nan)
    vmin, vmax = np.nanpercentile(logm[s > n * 0.55], 55), np.nanpercentile(np.diagonal(logm, 3), 97)
    norm = np.nan_to_num(np.clip((band - vmin) / (vmax - vmin), 0, 1))
    rgb = CMAP(norm)[..., :3]
    canvas = np.empty((H, W, 3))
    canvas[:] = [int(BACKGROUND[k:k + 2], 16) / 255 for k in (1, 3, 5)]
    canvas[H - tri_h - 40:H - 40] = rgb

    fig = plt.figure(figsize=(W / 200, H / 200), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(canvas, interpolation="nearest")
    ax.set_axis_off()
    fig.savefig(out, dpi=200, facecolor=BACKGROUND)
    plt.close(fig)


def atac_schematic(out: pathlib.Path, seed: int = 3) -> None:
    rng = np.random.default_rng(seed)
    fig = plt.figure(figsize=(W / 200, H / 200), dpi=200, facecolor=BACKGROUND)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 160)
    ax.set_ylim(0, 100)
    ax.set_facecolor(BACKGROUND)
    ax.set_axis_off()

    dna_y = 30
    xs = np.linspace(0, 160, 800)
    ax.plot(xs, dna_y + 0.8 * np.sin(xs * 1.4), color="#8d8780", lw=1.6, zorder=1)

    open_lo, open_hi = 66, 96  # nucleosome-depleted region
    centers = [c for c in np.arange(6, 160, 12.5) if not (open_lo - 4 < c < open_hi + 4)]
    for c in centers:
        ax.add_patch(Circle((c, dna_y), 5.2, facecolor="#86240f", edgecolor="#e66a37", lw=1.4, zorder=3))
        ax.add_patch(Circle((c - 1.5, dna_y + 1.6), 1.6, facecolor="#b8401a", edgecolor="none", zorder=4, alpha=0.7))

    # Tn5 insertions: dense in the open region, sparse in linkers between nucleosomes.
    cuts = list(rng.uniform(open_lo, open_hi, 26))
    for a, b in zip(centers[:-1], centers[1:]):
        if rng.random() < 0.45:
            cuts.append(rng.uniform(a + 5.5, b - 5.5) if b - a > 12 else (a + b) / 2)
    for c in cuts:
        ax.add_patch(Polygon([[c - 1.1, dna_y + 9.5], [c + 1.1, dna_y + 9.5], [c, dna_y + 6.8]],
                             closed=True, facecolor="#ff8a5c", edgecolor="none", zorder=5))

    # Read coverage built from the insertions: a peak over the open region.
    grid = np.linspace(0, 160, 1600)
    cov = sum(np.exp(-((grid - c) ** 2) / (2 * 2.2**2)) for c in cuts)
    cov = 48 + 38 * cov / cov.max()
    ax.fill_between(grid, 48, cov, color="#e66a37", alpha=0.85, lw=0, zorder=2)
    ax.plot(grid, cov, color="#ffe3cf", lw=1.4, zorder=3)
    ax.plot([0, 160], [48, 48], color="#4a4642", lw=1.0, zorder=2)

    fig.savefig(out, dpi=200, facecolor=BACKGROUND)
    plt.close(fig)


def main() -> None:
    fountain_toy(HERE / "fountain_toy.png")
    atac_schematic(HERE / "atac_schematic.png")
    print("wrote", HERE / "fountain_toy.png", HERE / "atac_schematic.png")


if __name__ == "__main__":
    main()
