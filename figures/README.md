# figures/

Every generated image on the site comes from a script in this folder, so it can be rebuilt.

| Output | Script | Input |
|---|---|---|
| `hic_chrX_hero.png` (3200 × 632, 2× for retina) | `make_hic_hero.py` | GEO GSE188849, `GSE188849_CA1200_auxin1hr_L2-L3_JK07_JK08_30.hic` (~1.3 GB, downloaded automatically) |
| `fountain_toy.png`, `atac_schematic.png` | `make_thematic_figures.py` | none (formulas only; illustrations, no data) |
| everything in `assets/img/` | `build_images.py` | the files above, my photo, the OmicsKit diagram, my peroPOA figure, and the Commons images listed in `CREDITS.md` |

```bash
conda env create -f figures/environment.yml
conda activate site-figures

python figures/make_hic_hero.py          # download -> hic2cool -> ICE -> render
python figures/make_thematic_figures.py
python figures/build_images.py           # crop, resize, WebP + JPEG/PNG, size check
```

## How the hero map is made

1. `hic2cool convert … -r 5000`: Juicer `.hic` to a single-resolution 5 kb cooler.
2. `cooler.balance_cooler(cis_only=True)`: ICE balancing, stored as the `weight` column.
   This is the slow step (about 20 minutes on a laptop, once; the weights are cached in the file).
3. `cooltools.lib.numutils.adaptive_coarsegrain` + `interp_nan`: fills sparse long-range pixels.
4. log10, color limits from the data in view (99th percentile near the diagonal, 60th
   percentile of the farthest contacts), then the matrix is sampled on a 45° grid so the
   diagonal runs along the bottom edge. Chromosome X (17.7 Mb) spans the full width; contacts
   up to 7 Mb apart are shown.
5. A single-hue sequential ramp that starts at the page's hero background (`#0c0f14`), so
   the map melts into the page. No axes, no labels.

Large intermediates (`.hic`, `.cool`, downloaded sources) live in `data/`, which is gitignored.
