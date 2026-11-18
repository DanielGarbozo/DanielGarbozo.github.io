#!/usr/bin/env python
"""Render the hero background: a real Hi-C contact map of the C. elegans X chromosome.

Data
    GEO GSE188849 (Ercan lab, Hi-C SubSeries), sample CA1200, L2-L3 larvae, auxin 1 hr,
    deposited as a Juicer .hic file (~1.3 GB). This is the same public control file that
    hicpup-nf's `full` profile uses.

Pipeline
    1. download the .hic from GEO (skipped if already present)
    2. hic2cool convert -> single-resolution 5 kb .cool
    3. cooler ICE balancing (stored as the `weight` column)
    4. cooltools adaptive coarse-graining to fill sparse long-range pixels
    5. log10, rotate 45 degrees so the diagonal runs along the bottom edge,
       color with a single-hue sequential ramp that starts at the page's hero
       background color, and write a 2x (retina) PNG with no axes.

Usage
    python figures/make_hic_hero.py --workdir data/hic
    python figures/make_hic_hero.py --cool path/to/existing_5kb.cool

Requires: cooler, cooltools, hic2cool, numpy, scipy, matplotlib, pillow.
Tested with cooler 0.10.4, cooltools 0.7.1, hic2cool 0.8.3.
"""
from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys
import urllib.request

import cooler
import numpy as np
from cooltools.lib.numutils import adaptive_coarsegrain, interp_nan
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image
from scipy.ndimage import map_coordinates

GEO_URL = (
    "https://ftp.ncbi.nlm.nih.gov/geo/series/GSE188nnn/GSE188849/suppl/"
    "GSE188849_CA1200_auxin1hr_L2-L3_JK07_JK08_30.hic"
)
HIC_SIZE_BYTES = 1_374_081_024  # Content-Length reported by GEO

# Must equal --hero-ink in css/style.css so the image melts into the page.
BACKGROUND = "#0c0f14"
# One warm hue, monotonically increasing in lightness (dark surface -> light tint).
RAMP = ["#0c0f14", "#1f0e0c", "#4a150d", "#86240f", "#b8401a", "#e66a37", "#f9a273", "#ffe3cf"]

HERE = pathlib.Path(__file__).resolve().parent


def download(url: str, dest: pathlib.Path) -> None:
    if dest.exists() and dest.stat().st_size == HIC_SIZE_BYTES:
        print(f"[hic] using existing {dest}")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"[hic] downloading {url} (~1.3 GB) ...")
    tmp = dest.with_suffix(".part")
    with urllib.request.urlopen(url, timeout=120) as r, open(tmp, "wb") as fh:
        shutil.copyfileobj(r, fh, length=1 << 22)
    tmp.rename(dest)


def hic_to_cool(hic: pathlib.Path, cool: pathlib.Path, resolution: int) -> None:
    if cool.exists():
        print(f"[cool] using existing {cool}")
        return
    print(f"[cool] hic2cool convert -r {resolution}")
    subprocess.run(
        ["hic2cool", "convert", str(hic), str(cool), "-r", str(resolution), "-p", "4"],
        check=True,
    )


def ensure_balanced(path: pathlib.Path) -> cooler.Cooler:
    clr = cooler.Cooler(str(path))
    if "weight" not in clr.bins().columns:
        print("[cool] ICE balancing with cooler.balance_cooler")
        cooler.balance_cooler(clr, store=True, cis_only=True)
        clr = cooler.Cooler(str(path))
    return clr


def rotated_band(logm: np.ndarray, width_px: int, maxdist_bins: int) -> np.ndarray:
    """Sample the matrix on a 45-degree rotated grid.

    Output row 0 is the top of the image (largest genomic distance); the last
    row is the main diagonal. Pixels outside the matrix are NaN.
    """
    n = logm.shape[0]
    scale = width_px / n  # pixels per bin along the diagonal
    height_px = int(round(scale * maxdist_bins / 2))
    px = (np.arange(width_px) + 0.5) / scale  # position along diagonal, in bins
    py = (np.arange(height_px)[::-1] + 0.5) / scale  # half-distance from the diagonal
    x, y = np.meshgrid(px, py)
    i, j = x - y, x + y
    return map_coordinates(logm, [i, j], order=1, mode="constant", cval=np.nan)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workdir", type=pathlib.Path, default=HERE.parent / "data" / "hic",
                    help="where the .hic and .cool are kept (gitignored)")
    ap.add_argument("--cool", type=pathlib.Path, help="use an existing single-resolution .cool")
    ap.add_argument("--resolution", type=int, default=5000)
    ap.add_argument("--chrom", default="X")
    ap.add_argument("--maxdist", type=float, default=7e6, help="largest separation shown, bp")
    ap.add_argument("--width", type=int, default=3200, help="output width in px (2x of 1600 CSS px)")
    ap.add_argument("--out", type=pathlib.Path, default=HERE / "hic_chrX_hero.png")
    args = ap.parse_args()

    if args.cool is None:
        hic = args.workdir / GEO_URL.rsplit("/", 1)[-1]
        args.cool = args.workdir / f"ca1200_{args.resolution // 1000}kb.cool"
        download(GEO_URL, hic)
        hic_to_cool(hic, args.cool, args.resolution)

    clr = ensure_balanced(args.cool)
    assert clr.binsize == args.resolution, f"cooler binsize {clr.binsize} != {args.resolution}"
    raw = clr.matrix(balance=False).fetch(args.chrom).astype(float)
    bal = clr.matrix(balance=True).fetch(args.chrom)
    print(f"[map] chr{args.chrom}: {bal.shape[0]} bins x {args.resolution} bp")

    # Coarse-grain sparse pixels (cooltools), then interpolate masked bins.
    smooth = adaptive_coarsegrain(bal, raw, cutoff=3, max_levels=8)
    smooth = interp_nan(smooth)
    with np.errstate(divide="ignore", invalid="ignore"):
        logm = np.log10(smooth)
    logm[~np.isfinite(logm)] = np.nan

    maxdist_bins = int(args.maxdist // args.resolution)
    band = rotated_band(logm, args.width, maxdist_bins)

    # Color limits from the data in view: near-diagonal ceiling, far-contact floor.
    n = logm.shape[0]
    near = np.concatenate([np.diagonal(logm, k) for k in range(2, 40)])
    far = np.concatenate([np.diagonal(logm, k) for k in range(int(maxdist_bins * 0.8), min(maxdist_bins, n - 1))])
    vmax = np.nanpercentile(near, 99.0)
    vmin = np.nanpercentile(far, 60.0)
    print(f"[map] log10 limits {vmin:.2f} .. {vmax:.2f}")

    norm = np.clip((band - vmin) / (vmax - vmin), 0, 1)
    norm = np.where(np.isnan(norm), 0.0, norm)
    cmap = LinearSegmentedColormap.from_list("ember", RAMP, N=1024)
    rgb = cmap(norm)[..., :3]

    # Ease the top 18% into the background so the map has no hard upper edge.
    h = rgb.shape[0]
    fade = np.clip(np.linspace(0, 1, h) / 0.18, 0, 1)[:, None, None] ** 1.5
    bg = np.array([int(BACKGROUND[k:k + 2], 16) / 255 for k in (1, 3, 5)])
    rgb = bg + (rgb - bg) * fade

    img = Image.fromarray((rgb * 255).round().astype(np.uint8), "RGB")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    img.save(args.out, optimize=True)
    print(f"[out] {args.out} {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    sys.exit(main())
