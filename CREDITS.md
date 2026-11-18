# Credits

Every image on this site is listed here with its source and license. Third-party images were
fetched on **2026-11-18** from their Wikimedia Commons file pages; the license was read from
each page's license template (and, where present, its license review) on that date.

All third-party images were **modified**: cropped to the card's aspect ratio, resized, and
re-encoded as WebP with a JPEG fallback by [`figures/build_images.py`](figures/build_images.py).
The same attribution appears under each image and in the page footer.

## Third-party images

| Used as | File in `assets/img/` | Author | License | Source |
|---|---|---|---|---|
| Research card: cohesin and condensin in *C. elegans* | `research-celegans.{webp,jpg}` | ZEISS Microscopy (Germany) | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/) | Commons: [File:C. elegans, model organism in life sciences (28703152561).jpg](https://commons.wikimedia.org/wiki/File:C._elegans,_model_organism_in_life_sciences_(28703152561).jpg); original on [Flickr](https://www.flickr.com/photos/zeissmicro/28703152561/) |
| Research card: Chagas cardiomyopathy | `research-tcruzi.{webp,jpg}` | NIAID (NIH BioArt Source, illustration 634) | Public domain (`PD-USGov-NIH-NIAID`, work of the US federal government) | Commons: [File:Trypanosoma cruzi (NIH BioArt 634).png](https://commons.wikimedia.org/wiki/File:Trypanosoma_cruzi_(NIH_BioArt_634).png); original at [NIH BioArt](https://bioart.niaid.nih.gov/bioart/634) |
| Research card: platelets in tuberculosis | `research-mtb.{webp,jpg}` | CDC / Dr. Ray Butler; photo Janice Carr | Public domain (`PD-USGov-HHS-CDC`, CDC Public Health Image Library #8438) | Commons: [File:Mycobacterium tuberculosis.jpg](https://commons.wikimedia.org/wiki/File:Mycobacterium_tuberculosis.jpg) |
| Research card: omics with clinical data and images | `research-histology.{webp,jpg}` | Mikael Häggström, M.D. | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Commons: [File:Histopathology of invasive ductal carcinoma, intermediate magnification.jpg](https://commons.wikimedia.org/wiki/File:Histopathology_of_invasive_ductal_carcinoma,_intermediate_magnification.jpg) |
| Research card: poultry viruses | `research-poultry.{webp,jpg}` | safaritravelplus | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (license-reviewed on Commons, 2024-06-20) | Commons: [File:Free Range Chicken.jpg](https://commons.wikimedia.org/wiki/File:Free_Range_Chicken.jpg); original at [safaritravelplus.com](https://www.safaritravelplus.com/images/animals/free-range-chicken/) |
| Background of the counter strip | `strip-flowcell.{webp,jpg}` | Suspencewl | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) | Commons: [File:DNA Nanoball sequencing flow cell.jpg](https://commons.wikimedia.org/wiki/File:DNA_Nanoball_sequencing_flow_cell.jpg) (top panel only) |

Public-domain and CC0 works need no attribution; they are credited anyway.

## Data

| Used in | Data | License / terms |
|---|---|---|
| Hero background (`hero-hic`), `figures/hic_chrX_hero.png` | Hi-C, *C. elegans* CA1200, L2-L3, auxin 1 h: `GSE188849_CA1200_auxin1hr_L2-L3_JK07_JK08_30.hic` from NCBI GEO [GSE188849](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE188849) (Ercan lab; Morao, Kim, … Ercan) | NCBI GEO places no restrictions on the use of submitted data; please cite the series and the associated publication. |
| Research card: `research-perpoa` | Figure `umap_moffitt_labels.png` from my own repository [DanielGarbozo/peroPOA_snRNAseq](https://github.com/DanielGarbozo/peroPOA_snRNAseq), a reanalysis of public GEO [GSE272719](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE272719) | My own work |

## Own work

| File | What it is |
|---|---|
| `profile.{webp,jpg}` | My photograph (`git_profile_pic.jpg`) |
| `hero-hic.{webp,jpg}` | Rendered by [`figures/make_hic_hero.py`](figures/make_hic_hero.py) with cooler and cooltools |
| `research-fountain.{webp,jpg}` | Toy simulation by [`figures/make_thematic_figures.py`](figures/make_thematic_figures.py); an illustration, not dryhic output |
| `research-atac.{webp,jpg}` | ATAC-seq schematic by [`figures/make_thematic_figures.py`](figures/make_thematic_figures.py) |
| `omicskit-architecture.{webp,png}` | OmicsKit architecture diagram (`Omicskit_fig1_architecture.png`), BigMind / OmicsKit authors |
| `assets/favicon.svg`, inline SVG icons | Drawn for this site |

## Fonts and code

- [DM Serif Display](https://fonts.google.com/specimen/DM+Serif+Display) and [Inter](https://fonts.google.com/specimen/Inter), served by Google Fonts under the SIL Open Font License 1.1.
- Layout structure inspired by [swkang73.github.io](https://swkang73.github.io) (a customized CeeVee/KARDS template by Styleshout). No stylesheet, script or image from that site or template was copied; all CSS and JavaScript here were written from scratch.

## Not used

- `background.jpg` (Machu Picchu) carries a visible Shutterstock watermark, so its license could not be verified. It is excluded from the repository in `.gitignore`.
