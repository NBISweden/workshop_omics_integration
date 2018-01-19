---
layout: default
title:  'Signal visualisation with deepTools'
---

## Signal visualisation with deepTools
One more thing that may come useful when analysing ChIP-seq data is visualising ChIP signal in relation to annotated transcription start sites (TSS) on chromosomes 1 and 2. Here, we will do just that in three main steps i.e.
* converting bedgraph to bigWig using UCSC utilities
* calculating scores per genome regions using among others the bigWig file
* plotting a heatmap of scores associated with genomic regions


In case you have logged out Uppmax:
```bash

ssh -Y <username>@milou.uppmax.uu.se
interactive -A g2017022 -p core -n 4 -t 8:00:00 --res=g2017022_FRI
source ~/chipseq_env.sh	

```

Assuming we the same files structure as in the first data processing tutorial, create a separate directory in `~/chipseq/analysis` and cd to it. Copy the files needed for this exercise. 

```bash
cd ~/chipseq/analysis/
mkdir ~/chipseq/analysis/vis
cd ~/chipseq/analysis/vis

cp ../../hg19/chrom.sizes.hg19 chrom.sizes.hg19
cp ../bam_preproc/ENCFF000PED.chr12.cov.norm1x.bedgraph ./
```
To calculate scores per genome with deepTools [computeMatrix](http://deeptools.readthedocs.org/en/latest/content/tools/computeMatrix.html) we need [bigWig](https://genome.ucsc.edu/goldenpath/help/bigWig.html) file that we can obtain by converting bedgraph using UCSC utilities:

```bash
module load ucsc-utilities/v287

bedGraphToBigWig ENCFF000PED.chr12.cov.norm1x.bedgraph chrom.sizes.hg19 hela_1.bw

module unload ucsc-utilities/v287
```

We can now compute the matrix of scores for visualisation using [computeMatrix](http://deeptools.readthedocs.org/en/latest/content/tools/computeMatrix.html). This tool calculates scores per genome regions and prepares an intermediate file that can be used with plotHeatmap and plotProfiles. Typically, the genome regions are genes, but any other regions defined in a BED file can be used. computeMatrix accepts multiple score files (bigWig format) and multiple regions files (BED format). This tool can also be used to filter and sort regions according to their score.

We will need a BED file with positions of TSS that we can copy to the working directory before running computeMatrix e.g.
```bash
module load deepTools/2.0.1

cp ../../hg19/refGene_hg19_TSS_chr12.bed ./

computeMatrix reference-point -S hela_1.bw \
-R refGene_hg19_TSS_chr12.bed -b 5000 -a 5000 \
--outFileName matrix.tss.dat --outFileNameMatrix matrix.tss.txt \
--referencePoint=TSS --numberOfProcessors=max
```

We can now create a heatmap for scores associated with genomic regions, i.e. plot the binding profile around TSS 
```bash

plotHeatmap --matrixFile matrix.tss.dat \
--outFileName tss.hela_1.pdf \
--sortRegions descend --sortUsing mean

```

Have a look at the `tss.hela_1.pdf`. What do you think?

