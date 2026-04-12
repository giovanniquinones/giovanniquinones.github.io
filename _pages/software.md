---
layout: single
title: "Software"
permalink: /software/
author_profile: true
---

<section class="software-page">
  <header class="software-page__hero">
    <p class="software-page__eyebrow">Computational Tools</p>
    <h2>RNA Analysis Software</h2>
    <p>
      Open-source tools for RNA variant discovery, RNA editing, and
      transcriptome-scale analysis.
    </p>
    <p>
      I develop production-ready bioinformatics methods in Python, including
      packaging and distribution workflows for reproducible research software.
      I am also proficient in R and Bash for scalable analysis pipelines and
      rapid prototyping.
    </p>
    <a class="btn" href="https://github.com/giovanniquinones" target="_blank" rel="noopener noreferrer">
      View GitHub Profile
    </a>
  </header>

  <div class="software-grid">
    <article class="software-card">
      <h3 class="software-card__title"><span class="software-card__name">isoLASER</span><img class="software-card__icon" src="{{ '/images/isoLASER_icon.png' | relative_url }}" alt="isoLASER icon" /></h3>
      <p><strong>Role:</strong> Lead developer</p>
      <p>isoLASER performs variant calling, haplotyping, and allele-specific splicing analysis in long-read RNA-sequencing data. This one-stop solution enables classification of genetically regulated splicing events, revealing transcriptome-wide regulation patterns and disease-relevant isoform regulation, including the HLA gene family and Alzheimer's disease risk genes. Built in Python and available on GitHub and PyPI.</p>
      <ul class="software-tags">
        <li>Long-read RNA-seq</li>
        <li>Isoform analysis</li>
        <li>Python</li>
      </ul>
      <p><a href="https://github.com/gxiaolab/isoLASER" target="_blank" rel="noopener noreferrer">Repository</a></p>
      <p><a href="https://doi.org/10.1038/s41467-025-64605-6" target="_blank" rel="noopener noreferrer">Related paper</a></p>
    </article>

    <article class="software-card">
      <h3 class="software-card__title"><span class="software-card__name">scAllele</span><img class="software-card__icon" src="{{ '/images/scAllele_icon.png' | relative_url }}" alt="scAllele icon" /></h3>
      <p><strong>Role:</strong> Lead developer</p>
      <p>scAllele is an integrative tool that performs high-confidence calls of small variants in single-cell RNA-sequencing data. It also enables allele-specific splicing analysis, a feature not previously used at single-cell resolution, allowing identification of cell-type and cancer-specific splicing regulation in our studies. Built in Python and available on GitHub and PyPI.</p>
      <ul class="software-tags">
        <li>scRNA-seq</li>
        <li>Variant calling</li>
        <li>Genomics</li>
      </ul>
      <p><a href="https://github.com/gxiaolab/scAllele" target="_blank" rel="noopener noreferrer">Repository</a></p>
      <p><a href="https://doi.org/10.1126/sciadv.abn6398" target="_blank" rel="noopener noreferrer">Related paper</a></p>
    </article>

    <article class="software-card">
      <h3 class="software-card__title"><span class="software-card__name">L-GIREMI</span><img class="software-card__icon" src="{{ '/images/L-Giremi_icon.png' | relative_url }}" alt="L-GIREMI icon" /></h3>
      <p><strong>Role:</strong> Contributor</p>
      <p>L-GIREMI uses a robust statistical approach based on mutual information for detecting A-to-I RNA editing in long-read RNA sequencing data, unveiling insights about the distribution of editing sites on individual RNA molecules. Built in Python and available on GitHub.</p>
      <ul class="software-tags">
        <li>RNA editing</li>
        <li>Long-read</li>
        <li>Bioinformatics</li>
      </ul>
      <p><a href="https://github.com/gxiaolab/L-GIREMI" target="_blank" rel="noopener noreferrer">Repository</a></p>
      <p><a href="https://doi.org/10.1186/s13059-023-03012-w" target="_blank" rel="noopener noreferrer">Related paper</a></p>
    </article>

    <article class="software-card">
      <h3 class="software-card__title"><span class="software-card__name">BEAPR</span><img class="software-card__icon" src="{{ '/images/BEAPR_icon.png' | relative_url }}" alt="BEAPR icon" /></h3>
      <p><strong>Role:</strong> Contributor</p>
      <p>BEAPR identifies allele-specific binding events in eCLIP-seq data to functionally characterize genetic variants. By modeling crosslinking-induced sequence propensity and variation between replicated experiments, BEAPR achieves high-accuracy calls and identifies clinically relevant variants. Built in C++ and R and available on GitHub.</p>
      <ul class="software-tags">
        <li>Allele-specific analysis</li>
        <li>Statistical modeling</li>
        <li>RNA biology</li>
      </ul>
      <p><a href="https://github.com/gxiaolab/BEAPR" target="_blank" rel="noopener noreferrer">Repository</a></p>
      <p><a href="https://doi.org/10.1038/s41467-019-09292-w" target="_blank" rel="noopener noreferrer">Related paper</a></p>
    </article>
  </div>
</section>
