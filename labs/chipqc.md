---
layout: default
title:  'ChIPQC'
---

## Introduction
Here, we will explore the alternative quality control workflow, using Bioconductor ChIPQC package. ChIPQC computes quality metrics for aligned data from ChIP-seq experiments. It also provides simple ways to generate a ChIP-seq experiment quality report which can be examined to asses the absolute and relative quality of individual ChIP-seq samples (and their associated controls, as well as overall quality of the experimental data.)


## Setting-up
You can choose to run this example on Uppmax or locally. 

**Uppmax**

To run on Uppmax, assuming the same files structure as for the [ChIP-seq data processing tutorial](processing) set pathway to R libraries installed on Uppmax, navigate to R directory and open R:
```bash

export R_LIBS="/sw/courses/ngsintro/chipseq/software/zzz_R_lib"

cd ~/chipseq/analysis/R

R

```

**Locally**

To run locally, follow set-up instructions from [Down-stream analysis tutorial](diffBinding), differential binding part. We will need the same files and we can work in the same directory. Install ChIPQC library:
```bash
source("https://bioconductor.org/biocLite.R")
biocLite("ChIPQC")
```

## Running ChIPQC
While running commands, have a look at [ChIPQC package documentation](http://bioconductor.org/packages/devel/bioc/vignettes/ChIPQC/inst/doc/ChIPQC.pdf) to learn more about different steps and/or build upon them

```bash

library(DiffBind)
library(ChIPQC)
library(TxDb.Hsapiens.UCSC.hg19.knownGene)


#	reading in the sample information (metadata)
samples = read.csv("samples_REST.txt", sep="\t")

#	inspecting the metadata
samples

#	creating an object containing data
res=dba(sampleSheet=samples, config=data.frame(RunParallel=FALSE))

# inspecting the object
res

#	performing quality control
resqc = ChIPQC(res,annotation="hg19", config=data.frame(RunParallel=TRUE))

#	creating the quality control report in html format
ChIPQCreport(resqc)

```

Examine the html report. What do you think? Are results in line with the previous quality control workflow?







