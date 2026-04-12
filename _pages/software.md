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
    <ul>
      <li>
        <strong>isoLASER - Lead Developer:</strong> isoLASER performs variant
        calling, haplotyping, and allele-specific splicing analysis in
        long-read RNA-sequencing data. This one-stop solution enables the
        classification of genetically regulated splicing events revealing
        transcriptome-wide patterns of regulation and disease-relevant isoform
        regulation such as the HLA gene family and Alzheimer's disease risk
        genes. Built in Python, available on GitHub and PyPI. GitHub:
        <a href="https://github.com/gxiaolab/isoLASER" target="_blank" rel="noopener noreferrer">https://github.com/gxiaolab/isoLASER</a>
      </li>
      <li>
        <strong>scAllele - Lead Developer:</strong> scAllele is an integrative
        tool that performs high-confidence calls of small variants in
        single-cell RNA-sequencing. Additionally, scAllele enables
        allele-specific splicing analysis, a unique feature not previously used
        at the single-cell level. This feature allows the identification of
        cell-type and cancer-specific splicing regulation in our studies. Built
        in Python, available on GitHub and PyPI. GitHub:
        <a href="https://github.com/gxiaolab/scAllele" target="_blank" rel="noopener noreferrer">https://github.com/gxiaolab/scAllele</a>
      </li>
      <li>
        <strong>L-GIREMI - Contributor:</strong> L-GIREMI uses a robust
        statistical approach based on mutual information for the detection of
        A-to-I RNA editing in long-read RNA sequencing data, unveiling insights
        about the distribution of these sites on individual RNA molecules.
        Built in Python, available on GitHub. GitHub:
        <a href="https://github.com/gxiaolab/L-GIREMI" target="_blank" rel="noopener noreferrer">https://github.com/gxiaolab/L-GIREMI</a>
      </li>
      <li>
        <strong>BEAPR - Contributor:</strong> BEAPR identifies allele-specific
        binding events in eCLIP-seq data to functionally characterize genetic
        variants. Taking into account crosslinking-induced sequence propensity
        and variation between replicated experiments, BEAPR achieves
        high-accuracy calls and identifies clinically relevant variants. Built
        in C++ and R, available on GitHub. GitHub:
        <a href="https://github.com/gxiaolab/BEAPR" target="_blank" rel="noopener noreferrer">https://github.com/gxiaolab/BEAPR</a>
      </li>
    </ul>
    <a class="btn" href="https://github.com/giovanniquinones" target="_blank" rel="noopener noreferrer">
      View GitHub Profile
    </a>
  </header>

  <div class="software-grid">
    <article class="software-card">
      <h3 class="software-card__title"><span class="software-card__name">isoLASER</span><img class="software-card__icon" src="{{ '/images/isoLASER_icon.png' | relative_url }}" alt="isoLASER icon" /></h3>
      <p><strong>Role:</strong> Lead developer</p>
      <p>Isoform-aware analysis workflows for long-read transcriptomics and RNA processing.</p>
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
      <p>Variant detection and downstream analysis from single-cell RNA sequencing data.</p>
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
      <p>Long-read RNA editing site identification for transcriptome-wide studies.</p>
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
      <p>Computational framework for identifying functional allele-specific molecular signals.</p>
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
