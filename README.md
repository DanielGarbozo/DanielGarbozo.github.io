# danielgarbozo.github.io

Personal academic website of Daniel Garbozo, bioinformatician (3D genome and chromatin,
multi-omics and NGS, reproducible pipelines). Plain HTML, CSS and JavaScript: no framework,
no build step, no npm, no Jekyll. Served by GitHub Pages at <https://danielgarbozo.github.io>.

## Preview locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Layout

```
index.html            the site (Home, About, Research, Software, Publications, Experience, Community, Contact)
cv.html               one-page CV; prints to exactly one A4 page
cv.pdf                generated from cv.html (cv/make_cv_pdf.py)
404.html              not-found page
css/style.css         site styles: color tokens on :root, dark palette under prefers-color-scheme
css/cv.css            CV styles, including the A4 print sheet
js/main.js            mobile menu, section highlight, counters, copy-email, greeting popup
assets/img/           optimized images (WebP + JPEG/PNG fallback, each under 300 KB)
assets/favicon.svg
figures/              scripts that generate every figure + the images in assets/img/
cv/cv-full.md         full CV, redacted for public view
cv/make_cv_pdf.py     cv.html -> cv.pdf (headless Chromium via Playwright)
CREDITS.md            source, author and license of every image
.nojekyll             serve files as-is
```

## Content rules

- `CV 2026 - 4pg.md` is the single source of truth. The original stays out of git
  (`.gitignore`) because it has a phone number, a street address and referees' emails;
  `cv/cv-full.md` is the redacted copy.
- Manuscripts that are submitted or in preparation are shown by title, authors and status
  only, and the research cards describe them by question and method. No numbers, effect sizes,
  gene or sample counts, or named biomarkers from unpublished work. The only numbers shown
  come from the public peroPOA_snRNAseq README.
- Every third-party image is in `CREDITS.md`, with a short attribution under the image and in the footer.

## Regenerate figures, images and the CV PDF

```bash
conda env create -f figures/environment.yml && conda activate site-figures
python figures/make_hic_hero.py            # GEO GSE188849 -> hic2cool -> cooler ICE -> cooltools -> PNG
python figures/make_thematic_figures.py    # toy fountain map + ATAC-seq schematic
python figures/build_images.py             # crop/resize -> assets/img/*.webp + fallback

pip install playwright && playwright install chromium
python cv/make_cv_pdf.py                   # refuses to write if cv.html overflows one page
```

Without Python, print the CV from Chrome: open `cv.html`, Print, Destination "Save as PDF",
Paper A4, Margins "None", untick "Headers and footers".

## When dryhic is public

In `index.html`, find the `dryhic` card (Software section), replace
`<span class="no-link">Code not yet public</span>` with a GitHub link like the other cards,
and change its `In development` status if you want. The Research card can stay as is.

## Deploy (GitHub Pages, user site)

```bash
git remote add origin https://github.com/DanielGarbozo/DanielGarbozo.github.io.git
git push -u origin main
```

or create the repository and push in one step with the GitHub CLI:

```bash
gh repo create DanielGarbozo.github.io --public --source=. --remote=origin --push
```

Then serve `main` from the repository root (skip if Settings → Pages already shows it live):

```bash
gh api -X POST repos/DanielGarbozo/DanielGarbozo.github.io/pages \
  -f "source[branch]=main" -f "source[path]=/"
gh api repos/DanielGarbozo/DanielGarbozo.github.io/pages --jq '.html_url,.status'
```

The site is live at <https://danielgarbozo.github.io> a minute or two after the first build.

## License

Text, photographs and figures © Daniel Garbozo unless noted in `CREDITS.md`. Third-party
images keep their own licenses (CC BY 2.0, CC0, public domain), listed there.
