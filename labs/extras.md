---
layout: default
title:  'ChIP-seq down-stream analysis'
---

# ChIP-seq down-stream analysis

## Introduction <a name="Introduction"></a>
Welcome back to the second part of the tutorial. In the first part we have learnt how to access the quality of ChIP-seq data. We now know can tell whether the ChiP has worked or not. We have also learnt hwo to find in a simple way a consenus peakset for down-stream analysis. In this part we will learn i) how to identify sites that are differentially bound between two sample groups and ii) how to place these regions in a biological context

This tutorial has two R excercise that can be run either on Uppmax or locally using R Studio. We recommend transferring files to computer and working locally, it is so much easier to experiment with the code and look at the plots. 

## Content
- [Introduction](#Introduction)
- [Data & Methods](#DataMethods)
- [Setting-up](#Setting-up)
- [Differential bidning](#DB)
- [Functional analysis](#FA)
- [What's next?](#Next)

## Data & Methods <a name="DataMethods">
We will continue using the same data as in the first part of the tutorial. Please note that usually three biological replicates are the minium requirement for statistical analysis such as in factor occupnacy. The ENCODE data we are using have only two replicates and we are using them to demonstrate the tools and methologies. No biological conclusions should be drawn from from them, or any other dataset with dupcliates only. Remember: just because it computes does not make it right! 

## Setting-up  <a name="Setting-up">
If you are choosing to run scripts locally you can skip this part. Refer back to [pre-course](../precourse) preparations on installing R and R-Studio if you have not done this already, 

If you are choosing to run scripts on Uppmax, the setting-up is the same as for the first part of this tutorial. If  you have not logged out from Uppmax you can simply skip this part. If you have logged out: log back in, open interactive session, and run `chipseq_env.sh` script. Note to change reservation name to FRI if it is no longer Thursday. 

```bash

ssh -Y <username>@milou.uppmax.uu.se
interactive -A g2017022 --res=g2017022_FRI
source ~/chipseq_env.sh	

```

## Differential binding <a name="DB">

We will usage Bioconductor package [DiffBind](http://bioconductor.org/packages/release/bioc/html/DiffBind.html) to identify sites that are differentially bound between two sample groups. The package includes "functions to support the processing of peak sets, including overlapping and merging peak sets, counting sequencing reads overlapping intervals in peak sets, and identifying statistically significantly differentially bound sites based on evidence of binding affinity (measured by differences in read densities). To this end it uses statistical routines developed in an RNA-Seq context (primarily the Bioconductor packages edgeR and DESeq2 ). Additionally, the package builds on Rgraphics routines to provide a set of standardized plots to aid in binding analysis." This means that we will repeat finding a consenus peakset in a more powerful way before identyfing differentially bound sites. Actually, defying the consensus peaks is an important step that takes up entire chapter in the DiffBind manual. Read seciotion [6.2](http://bioconductor.org/packages/devel/bioc/vignettes/DiffBind/inst/doc/DiffBind.pdf) if you like to even more. 

Follow Uppmax or local version to go further
* [Uppmax version](#DB_uppmax)
* [Local version](#DB_local)

### Uppmax version <a name="DB_uppmax">

Let's load [R packges module](https://www.uppmax.uu.se/support/user-guides/r_packages-module-guide/) that has a bunch of R packages, including DiffBind package, installed on Uppmax. And let's go to the right directory given you are keeping files structure as for the first part of the tutorial. 

```bash

module load R_packages/3.4.0
cd ~/chipseq/analysis/R

```

In this directory we have placed a sampel sheet named `samples_REST.txt` that points to our BAM files as well as BED files with called peaks, following DiffBind specifications. To inspect: 

```bash

head samples_REST.txt

```

Let's open R on Uppmax by simply typing R

```bash

R

```

From within R we need to load DiffBind library
```bash

library(DiffBind)

```

We will now follow DiffBind example to obtain differentially bound sites, given our samples. You may want to open DiffBind tutorial and read section [3 Example: Obtaining differentially bound sites](http://bioconductor.org/packages/devel/bioc/vignettes/DiffBind/inst/doc/DiffBind.pdf) while typing the command to get more informatin about each step. 

```bash

# reading in the sample information (metadata)
samples = read.csv("samples_REST.txt", sep="\t")

#	inspecting the metadata
samples

#	creating an object containing data
res=dba(sampleSheet=samples, config=data.frame(RunParallel=FALSE))

# inspecting the object: how many peaks are identifed given the default settings?
res

# counting reads mapping to intervals (peaks)
# at this step a normalisation is applied by the default set to: score=DBA_SCORE_TMM_MINUS_FULL
res.cnt = dba.count(res, minOverlap=2, score=DBA_SCORE_TMM_MINUS_FULL, fragmentSize=130)

# inspecting the object: notice the FRiP values! 
res.cnt

# plotting the correlation of libraries based on normalised counts of reads in peaks
pdf("correlation_libraries_normalised.pdf")
plot(res.cnt)
dev.off()

# PCA scores plot: data overview
pdf("PCA_normalised_libraries.pdf")
dba.plotPCA(res.cnt,DBA_TISSUE,label=DBA_TISSUE)
dev.off()

# setting the contrast: how many contrasts were set? 
res.cnt2 = dba.contrast(res.cnt, categories=DBA_TISSUE, minMembers=2)

# inspecting the object
res.cnt2

# performing analysis of differential binding
# which condition are most alike, which are most different, is this in line with part one of the tutorial?
res.cnt3 = dba.analyze(res.cnt2)
res.cnt3

# correlation heatmap  using only significantly differentially bound sites
# choose the contrast of interest e.g. HeLa vs. neuronal (#1)
pdf("correlation_HeLa_vs_neuronal.pdf")
plot(res.cnt3, contrast=1)
dev.off()

# boxplots to view how read distributions differ between classes of binding sites
# are reads distributed evenly between those that increase binding affinity HeLa vs. in neuronal?
pdf("Boxplot_HeLa_vs_neuronal.pdf")
pvals <- dba.plotBox(res.cnt3, contrast=1)
dev.off()

# extrating differentially bidning sites in GRanges
rest.db1 = dba.report(res.cnt3, contrast=1)
head(rest.db1)

# plotting overlaps of sites bound by REST in different cell types
pdf("binding_site_overlap_sknsh.pdf")
dba.plotVenn(res.cnt3, 1:4, label1="HeLa",label2="neuron",label3="HepG2",label4="sknsh")
dev.off()

```


### Local version <a name="DB_local">



## Part 3: Additional analyses
The following parts are optional, and can be preformed independently of one another.

The parts using R can be performed either by executing the scripts provided with the exercise from the command line, or by typing in all commands in an R console. The latter is recommended for people who have some previous exposure to the R environment. Post-peak calling QC is performed using the R / Bioconductor package ChIPQC, and some steps are redundant with the steps already performed; it is an alternative to the already presented workflow. Differential Occupancy and Peak Annotation sections present examples using R packages developed specifically for analysis of ChIP-seq data (there are many more useful packages in Bioconductor).

### Differential Occupancy and Peak Annotation in R

Before you start using R, you need to set the environmental variable that holds information on where R libraries are installed. In this exercise you will use libraries installed in the class home directory (simply because it takes quite some time to install all dependencies). The path should already be set, inspect it by:

```bash
echo $R_LIBS
```

The result should be `/sw/courses/ngsintro/chipseq/software/R_lib`. If it is not, source the `chipseq_env.sh` script.

Please note that normally three biological replicates are required for statistical analysis of factor occupancy. There are only two replicates each in the ENCODE data sets used in this class - hence you use duplicates for demonstration sake. This script uses the same sample information file as the previous one; the paths are all relative to the `/analysis/R directory`.

```bash
cd ../analysis/R
Rscript diffbind_annot.R
```

People familiar with R can modify and execute the commands from within the R terminal, selecting different contrasts of interest, for example.








## Differential binding (run locally) <a name="DB_local">
## Functional analysis <a name="FA">
## Functional analysis <a name="FA_local">
## What's next <a name="Next">


### Signal visualisation using deepTools

You will visualise ChIP signal in relation to annotated transcription start sites (TSS) on chromosomes 1 and 2. A description of all visualisation options is given at [deepTools](http://deeptools.readthedocs.org/en/latest/content/list_of_tools.html). Create a separate directory in `/analysis`; cd to it. Check if all the paths to create links are correct for the location of your directory. For details on the options of the applications used, please consult the documentation available at [computeMatrix](http://deeptools.readthedocs.org/en/latest/content/tools/computeMatrix.html) and [plotHeatmap](http://deeptools.readthedocs.org/en/latest/content/tools/plotHeatmap.html).

First you will compute the matrix of values using computeMatrix. This program takes [bigWig](https://genome.ucsc.edu/goldenpath/help/bigWig.html) files as input; you will need to convert bedgraph to bigWig using UCSC utilities:

```bash
cd analysis/
mkdir vis
cd vis

cp ../../hg19/chrom.sizes.hg19 chrom.sizes.hg19
cp ../bam_preproc/ENCFF000PED.chr12.cov.norm1x.bedgraph ./

module load ucsc-utilities/v287

bedGraphToBigWig ENCFF000PED.chr12.cov.norm1x.bedgraph chrom.sizes.hg19 hela_1.bw

module unload ucsc-utilities/v287
```

You are now ready to compute the matrix of scores for visualisation. You will need a bed file with positions of TSS; you can copy it to your current directory.

```bash
cp ../../hg19/refGene_hg19_TSS_chr12.bed ./

module load deepTools/2.0.1

computeMatrix reference-point -S hela_1.bw \
-R refGene_hg19_TSS_chr12.bed -b 5000 -a 5000 \
--outFileName matrix.tss.dat --outFileNameMatrix matrix.tss.txt \
--referencePoint=TSS --numberOfProcessors=max
```

Having the matrix of scores ready, you can now plot the binding profile around TSS and the heatmap:

```bash
plotHeatmap --matrixFile matrix.tss.dat \
--outFileName tss.hela_1.pdf \
--sortRegions descend --sortUsing mean

module unload deepTools/2.0.1
```

## Concluding remarks

The workflow presented in this exercise is similar to a typical one used for analysis of ChIP-seq data. There are more types of analyses you can do, which were not discussed here. One typical task is to identify short sequence motifs enriched in the regions bound by the assayed factor (peaks). There are several tools available, and I recommend testing at least two tools for your data.

[Homer](http://homer.salk.edu/homer/)

[GEM](http://groups.csail.mit.edu/cgs/gem/)

[RSAT](http://floresta.eead.csic.es/rsat/peak-motifs_form.cgi)

[MEME](http://meme-suite.org/)

## Appendix


### Alternative Quality Control Workflow in R

Before you start using R, you need to set the environmental variable that holds information on where R libraries are installed. In this exercise you will use libraries installed in the class home directory (simply because it takes quite some time to install all dependencies). The path should already be set, inspect it by:

```bash
echo $R_LIBS
```

The result should be `/sw/courses/ngsintro/chipseq/software/R_lib`. If it is not, source the `chipseq_env.sh` script.


You will start in directory `/analysis/R`. The file `REST_samples.txt` contains information on files location, and the paths are given in relation to `/analysis/R`; if you choose to start in another directory, please modify the paths in `REST_samples.txt`. This script takes a while to run.

```bash
cd ../analysis/R
Rscript chipqc.R
```

Inspect the html output of this script.