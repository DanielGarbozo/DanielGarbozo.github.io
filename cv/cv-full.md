<!-- Full CV, redacted for the public repository: no phone number, no street address,
     no referee email addresses, and no results from unpublished manuscripts.
     The website links the one-page version (cv.html / cv.pdf). -->

**Daniel Garbozo**

**Bioinformatic \| 3D Genome & Chromatin \| Multi-Omics & NGS \| Reproducible Pipelines (Nextflow, Python, R) \| Protein Structure & ML for Genomics**

**SUMMARY**

| Basic Info | Peruvian · English (C1) · Spanish (native) · Email: [danielgarbozo4@gmail.com](mailto:danielgarbozo4@gmail.com) · GitHub: [github.com/DanielGarbozo](https://github.com/DanielGarbozo) · LinkedIn: [in/danielgarbozo](https://www.linkedin.com/in/danielgarbozo) · Website: [danielgarbozo.github.io](https://danielgarbozo.github.io) |
| :---- | :---- |
| **Experience** | 3+ years of bioinformatics research across University of Pennsylvania (Bernstein Lab), New York University (Ercan Lab), The Rockefeller University (Risca Lab), Johns Hopkins Bloomberg School of Public Health (Gilman Lab), BigMind, plus applied pipeline development with distributed international teams. |
| **Publications** | 5 manuscripts (co-author on a clinical Chagas-biomarker study under review at Journal of Infectious Diseases; first author on OmicsKit, under review at Bioinformatics Advances; and three in progress (two as first author): a tuberculosis platelet transcriptomics study, a cohesin and condensin dosage-compensation study in C. elegans, and a molecular dynamics study of the Newcastle disease virus fusion protein). |
| **Software** | Author of **dryhic** (Python, in development)**,**  **hicpup** (Python), **hicpup-nf** (Nextflow), **ercantools** (R); and core developer of **OmicsKit(R)**. |
| **Profile** | Bioinformatician building **production-grade**, **reproducible software** for large-scale omics, DSL2 Nextflow pipelines with Docker/Singularity profiles, and published R and Python packages. Experienced across the NGS to multi-omics workflow, with an understanding of the biology behind the data and growing experience integrating AI tools. Proficient in Linux and HPC environments. Has leadered the bioinformatics component across laboratories and institutions, committed to have a collaborative environment such as mentoring peers. Strong technical writer and proactive collaborator, with a keen interest in expanding into ML, Deep Learning, integration with clinical data as multimodal layers such images and clinical data. |
| **Scientific Interest** | Integrative foundation models for genomics and clinical data. |
| **Education** | B.Sc. Genetics & Biotechnology, Universidad Nacional Mayor de San Marcos (UNMSM), Lima, Peru · 2020-2024 |

**ABILITIES**

***Multi-Omics & NGS Analysis***

▸ **RNA-seq:** differential expression (DESeq2, limma, edgeR), transcript quantification (Salmon, tximport), and competitive pathway enrichment (GSEA, CAMERA, PADOG).

▸ **ChIP-seq:** alignment and QC, peak calling (MACS2), coverage and signal tracks (deepTools), differential binding (DiffBind), and annotation (ChIPseeker).

▸ **ATAC-seq:** differential accessibility, TF motif analysis (JASPAR, HOCOMOCO), and metagene/signal profiling.

▸ **Hi-C / 3D genomics:** contact-matrix analysis (cooler, cooltools, coolpuppy), expected/observed normalization, pileups, fountain and loop quantification, and P(s) contact-decay profiling.

▸ **Multi-omics integration & visualization:** dimensionality reduction (PCA/UMAP/t-SNE), gene-set networks, ROC/AUC, and survival modeling (Kaplan-Meier), forest-plot (Cox model) consolidated in OmicsKit.

▸ **Single-cell / single-nucleus RNA-seq**: QC and doublet detection (Scrublet), batch integration (Harmony), clustering and marker-based annotation (scanpy, Seurat), reference label transfer from MERFISH atlases, and pseudobulk differential abundance and expression (edgeR, PyDESeq2).

***Programming & Reproducibility***

▸ Proficient in R (package development, Bioconductor) and Python (packaging, Typer CLIs, pytest); Bash/shell scripting.

▸ Workflow managers: Nextflow (DSL2) and Snakemake, developed for HPC execution.

▸ Versioning, documentation, and reproducibility practices (Git/GitHub, MkDocs/Read the Docs, semantic versioning, checksummed artifacts).

***Machine Learning & Deep Learning***

▸ Transformer architectures applied to 2D genomic data (Hi-C contact maps), from model design through training and evaluation.

▸ Simulation-based learning: generating synthetic training data from parametric biophysical simulators and testing how well models transfer to real public datasets.

▸ Method validation against known ground truth: designing synthetic benchmarks and signal-injection tests to confirm a method recovers known signal before applying it to real data.

***HPC & Cloud Computing***

▸ Extensive work on High-Performance Computing clusters (New York University Torch, SLURM scheduling, module environments).

▸ Containerization with Docker and Singularity; exploring Microsoft Azure for cloud-based analysis.

***Scientific Communication & Collaboration***

▸ Led the computational side of multi-institution studies, coordinating with PIs and wet-lab collaborators across University of Pennsylvania, New York University, The Rockefeller University, Johns Hopkins University, and St George's University of London.

▸ Strong technical writer: authored end-to-end documentation for published tools; contributed Methods/Results writing for manuscripts.

▸ Oral presenter at 7+ national and international conferences; active member and organizer within the Peruvian Society for Bioinformatics and Computational Biology.

**MY SOFTWARE CONTRIBUTIONS**

**dryhic: transformer scoring cohesin fountain anchors from a single Hi-C map**   (in development, code not yet public)

*Author · Python, cooler/cooltools, conda · in development*

▸ Building a transformer that scores DNA structures fountain anchors as calibrated per-bin probabilities from a single Hi-C contact map, pretrained on parametric fountain simulators rather than on published calls: fountain strength is continuous, and each existing caller cuts it at a different point.

▸ Benchmark design: rank and calibrate published anchors in a CTCF-free genome with no fine-tuning, which tests simulation to real transfer and whether a strong score only re-implements the caller that produced its labels.

**hicpup: Python package for downstream Hi-C pileup analysis**   [github.com/DanielGarbozo/hicpup](https://github.com/DanielGarbozo/hicpup)

*Author · Python, cooltools/coolpuppy, pytest, GitHub Actions*

▸ Design a modular, tested package with a 4-command Typer CLI (expected \| pileup \| profile \| plot), explicit I/O, and zero global state.

▸ Built a regression test suite (frozen-array, synthetic signal-injection, NaN-contamination checks); CI runs ruff \+ pytest on every push, with type-hinted docs on GitHub Pages.

**hicpup-nf: Nextflow (DSL2) pipeline orchestrating Hi-C analysis**   [github.com/DanielGarbozo/hicpup-nf](https://github.com/DanielGarbozo/hicpup-nf)

*Author · Nextflow DSL2, Docker, Singularity, GitHub Actions*

▸ Built a modular DSL2 pipeline (HIC2COOL → EXPECTED → PILEUP → PROFILE → PLOT), one container per process, following the nf-core pattern; combinable profiles separate engine from dataset (test/docker, full/singularity).

▸ Wrote a real CI pipeline with a no-NaN content assertion; handled .hic vs .cool inputs conditionally and scaled from synthetic fixtures to real public GEO data (.hic → .cool interconversion).

**OmicsKit: R package for reproducible multi-omics analysis & visualization**   [github.com/BigMindLab/OmicsKit](https://github.com/BigMindLab/OmicsKit)

*Core developer · R, Ensembl BioMart · manuscript submitted  \[Bioinformatic Advances\] 2026*

▸ Built reusable R functions for annotation, dimensionality reduction, differential-analysis visualization, pathway enrichment (GSEA/CAMERA/PADOG), gene-set networks, ROC/AUC, and Kaplan-Meier plots; version-aware, multi-species BioMart annotation.

**ercantools: R tools for ChIP-seq / DiffBind visualization**   [https\://github.com/ercanlab/ercantools](https://github.com/ercanlab/ercantools)

*Contributor · R · Ercan Lab*

▸ Contributed reusable plotting and analysis utilities for condensin/dosage-compensation ChIP-seq workflows in C. elegans.

**peroPOA\_snRNAseq: Reanalysis of a Peromyscus preoptic-area snRNA-seq atlas**   [github.com/DanielGarbozo/peroPOA\_snRNAseq](http://github.com/DanielGarbozo/peroPOA_snRNAseq)

*Author (solo project) · Python (scanpy, Harmony, Scrublet, PyDESeq2), R (Seurat, edgeR), conda*

▸ Built a reproducible pipeline, resulting in 53 neuron clusters from 95,057 nuclei of two Peromyscus species (GEO GSE272719) and mapping them onto the mouse POA MERFISH atlas (held-out accuracy 0.73 inhibitory, 0.81 excitatory).

▸ Treated the published result as a hypothesis to test: the between-species ratio of male-biased genes held between 1.4 and 2.7 across three subsampling schemes, two gene-filter settings and two methods (edgeR and PyDESeq2) against a published 2.8.

**SeqWrangler (ClawBio): NGS QC & alignment pipeline**   [https\://github.com/ClawBio/ClawBio/](https://github.com/ClawBio/ClawBio/tree/0d79d37d627fb6f9813f2b53a7de143e0cfdda48)

*Open-source contributor · Python · Advisor: Manuel Corpas, Ph.D.*

▸ Developed a Python pipeline for automated NGS read processing with multi-aligner support (BWA, Bowtie2, minimap2), a synthetic-data demo mode, and mock-based tests emitting reproducibility artifacts (metadata, SHA256 checksums).

**Teloscope (vgl-hub / Vertebrate Genome Lab): documentation**   [https\://github.com/vgl-hub/teloscope](https://github.com/vgl-hub/teloscope)

*Documentation contributor · MkDocs, Read the Docs · tool published (bioRxiv, DOI, Bioconda)*

▸ Designed and deployed a 10-section MkDocs \+ Read the Docs site for a published telomere-annotation tool, with a single-source-of-truth strategy reusing the repo README and a Material-theme configuration managed via a fork/upstream release workflow.

**INDUSTRY EXPERIENCE**

**FARVET S.A.C (veterinary vaccines and pharmaceuticals)**

Bioinformatics Core (Genomics and Proteomics)  *Supervisor: Dr. Luis Tataje-Lavanda*

▸ 07.2026 \- present · Proteomic Bioinformatician

▸Built a genomic surveillance workflow for avian orthoreovirus (ARV) that genotypes field isolates by the σC cell-attachment gene, using Oxford Nanopore consensus sequences.

▸Built codon-aware alignments (MACSE) and maximum-likelihood trees (IQ-TREE, 1,000 UFBoot and SH-aLRT; cross-checked in MEGA) to place Peruvian isolates among the ARV genotype clusters.

▸Predicted σC trimer structures with AlphaFold2-Multimer (LocalColabFold) on an HPC cluster, benchmarked them against an RMSD noise floor built from five σC crystal structures (bio3d), and mapped surface exposure (SASA) across the head domain.

**Bioinformatics consultant (contract)**

▸ 10.2026 \- present · Omics task author for AI evaluation 

▸Designed omics analysis tasks (bulk RNA-seq, single-cell RNA-seq, proteomics, etc.) with reference solutions, verification notes and grading rubrics.

**RESEARCH EXPERIENCE**

**University of Pennsylvania · Epigenetics institute**

Kara Bernstein Lab (ChIP-seq/ 3D genomics & chromatin)  *Supervisor: Ph.D. Victor Leon*

▸ 09.2026 \- present · External collaborator

▸Genomic analysis of double-strand break (DSB) sites in yeast

**New York University · Center for Genomics and Systems Biology**

Ercan Lab (Hi-C / 3D genomics & chromatin)     *PI and Supervisor: Sevinc Ercan, Ph.D.*

▸ 04.2025 \- present · Research Intern

▸ Developed **HPC-compatible ChIP-seq workflows** for paired/single-end AVITI data (mapping, signal-to-noise, peak-calling, coverage, replicate QC); performed DiffBind differential binding across cohesin, condensin, and RNA-polymerase perturbations; adapted DESeq2 RNA-seq for SMC-3/WAPL depletion.

▸ Built **Hi-C / 3D-genomics workflows** on .cool/.hic matrices: chromatin fountains, loop extrusion, X-vs-autosome interaction profiles, 60° cone/profile quantification, and site-centered strength at rex regions, with replicate-aware summaries; packaged the analysis into hicpup and hicpup-nf.

**BigMind · Bioinformatics Group of Multi-Omics & Immunology**

New York University / New York Genome Center     *Supervisor: David Requena, Ph.D.*

▸ 11.2024 \- Present · Research Assistant

▸ Core developer of **OmicsKit** (see Software Contributions).

▸ Led **tuberculosis platelet transcriptomics** with Daniela E. Kirwan, Ph.D. (St George's, University of London): RNA-seq from raw reads through Salmon and DESeq2, with competitive pathway enrichment (CAMERA, PADOG, GSEA).

**The Rockefeller University**

Risca Lab (chromatin structure & ATAC-seq)     *PI and Supervisor: Viviana Risca, Ph.D.*

▸ 11.2025 \- 12.2025 · Research Intern

▸ Performed **DiffBind ATAC-seq differential-accessibility analysis** (macroH2A knockdown vs. wild-type RPE cells, ±TGFB1 stress); ran TF motif analysis (JASPAR/HOCOMOCO), ChIPseeker annotation, and deepTools signal/metagene profiling.

**Johns Hopkins Bloomberg School of Public Health**

Department of International Health     *PI: Robert H. Gilman, MD, DTM\&H*

▸ 03.2024 \- 11.2024 · Research Intern

▸ Led the **RNA-seq analysis for a Chagas cardiomyopathy blood-transcriptome study** (FastQC, MultiQC, BBDuk, Salmon, tximport, DESeq2); generated normalized/TPM/VST matrices and PCA/UMAP/t-SNE/HDBSCAN clustering; performed pathway enrichment across MSigDB and contributed manuscript figures and Methods/Results writing.

**PUBLICATIONS**

▸ **Garbozo D.**, Tataje-Lavanda L, et al. Molecular dynamics of the pre-fusion F glycoprotein in Peruvian field isolates of Newcastle disease virus compared with the S1133 reference strain. 2026 (in preparation) 

▸ Requena D, Guevara-Diaz DF, **Garbozo D.**, Duque C, Medico JA, et al. *Blood transcriptomic biomarkers of cardiomyopathy in chronic Chagas disease.* Journal of Infectious Diseases, 2026 (submitted).

▸ **Garbozo D.**, Guevara-Diaz DF, Tataje-Lavanda L, Requena D. *OmicsKit: A toolset for multi-omics analysis and visualization.* Bioinformatics Advances, 2026 (submitted, under journal review).

▸ **Garbozo D.**, Guevara-Diaz DF, Requena D. *Platelet transcriptomic profiling provides novel insights into Tuberculosis disease.* 2026 (in preparation, under internal review).

▸ Haoyu Wang, Yuya Zhao, **Garbozo D.,** et al., Insights of Cohesin and Condensin in Dosage Compensation in *C. elegans.* 2026 (in preparation).

**SELECTED TRAINING**

▸ **Variant calling with nf-core**: hands-on Sarek pipeline for tumor/normal WES variant calling (STaiMIC, Matera, Italy, 2026).

▸ **Linear Algebra**: Massachusetts Institute of Technology (MIT OpenCourseWare), 2026\.

▸ **Spatial transcriptomics**: sequencing- and imaging-based spatial methods and downstream analysis (Cold Spring Harbor Laboratory, CSHL, 2025).

▸ **Hi-C data analysis & downstream 3D-genome interpretation**: matrix normalization, TAD/loop calling, and contact-decay analysis (New York University, 2025).

▸ **ChIP-seq & differential-binding analysis**: alignment, peak calling, and DiffBind-based differential enrichment (New York University, 2025).

▸ **RNA-seq, differential expression & transcript quantification**: full workflow from reads to enrichment (BigMind, 2024).

**AWARDS, PRESENTATIONS & AFFILIATION**

▸ **Awards & Scholarships: SACNAS Pathway to Graduate School Program 2026, Securing Degrees Scholarship 2026, Cientifico Latino Graduate Student Mentorship Initiative Scholarship (GSMI 2026 scholar), Santander course scholarship 2026,** Fellowship, Galaxy & Bioconductor Community Conference (Cold Spring Harbor Laboratory, 2025).

▸ **Oral presentations: ISCB-Latin America SoIBio SPBBC Conference on Bioinformatics** (Lima, 2026), Australian Bioinformatics and Computational Biology Society Conference (Australia, 2026), Nextflow Summit 2026**, AI in Bioscience: Converging Interests and Joint Solutions** (Mainz, Germany, 2026), VII International Congress SPBBC (Lima, 2025); Galaxy & Bioconductor Community Conference (CSHL, New York, 2025); Bioinformatics Youth Summit SPBBC (Lima, 2024); ASTMH Annual Meeting (2023); IV International Congress SPBBC (Lima, 2022).

▸ **Affiliation: International Society for Computational Biology Membership 2025-2027,**  Ibero-American Network for Foresight in Artificial Intelligence for the Biosciences and Biotechnology (RIABIA-pro) 2024-2026, Peruvian Society for Bioinformatics and Computational Biology (SPBBC), 2024-2026 · The branding team and Regional Students Group contributed to the bid to host the ISCB 2026 conference in Peru.

**REFERENCES**

**Sevinc Ercan, Ph.D.**

Principal Investigator, Ercan Lab, Center for Genomics and Systems Biology; Professor of Biology, New York University

**David Requena, Ph.D.**

Supervisor, BigMind Multi-Omics & Immunology; Postdoctoral Researcher, NYU Grossman School of Medicine; Senior Consultant, Rockefeller & Johns Hopkins Universities,  President of SPBBC

**Robert H. Gilman, MD, DTM\&H**

Principal Investigator, Department of International Health, Johns Hopkins Bloomberg School of Public Health; Professor of International Health

**Daniela E. Kirwan, Ph.D.**

Consultant in Medical Microbiology, Epsom and St Helier University Hospitals NHS Trust; Honorary Clinical Research Fellow, City St George's, University of London

Contact details for referees are available on request.
