---
layout: default
title:  'csaw'
---

<!-- version 1
still experimental, to be improved
22 xi 2017
 -->

# Detection of differential binding sites using csaw

This is an alternative workflow for detection of differential binding / occupancy in ChIP-seq data. In contrast to working with reads counted within peaks detected in a peak calling step (as in the earlier example with DiffBind), this approach uses a sliding window to count reads across the genome. Each window is then tested for significant differences between libraries from different conditions, using the methods in the edgeR package. This package also offers an FDR control strategy more appropriate for ChIP-seq experiments than simple BH adjustment.

It can be used for point-source binding (TFs) as well as for broad signal (histones). However, it can only be used for cases where ***global occupancy leves are unchanged***.

As this method is agnostic to signal structure, it requires careful choice of strategies for filtering and normalisation. Here, we show a very simple workflow. More details can be found in the [Csaw User Guide document](http://bioconductor.org/packages/devel/bioc/vignettes/csaw/inst/doc/csawUserGuide.pdf) available from Bioconductor.


## Requirements

* R version 3.4.2 (2017-09-28)
* [statmod](https://cran.r-project.org/web/packages/statmod/index.html), required for csaw
* [gfortran](https://gcc.gnu.org/wiki/GFortranBinaries), required for csaw
* csaw
* edgeR

Required for annotation in our example:
* org.Hs.eg.db
* TxDb.Hsapiens.UCSC.hg19.knownGene

Recommended:
* R-Studio to work in

*Note: this exercise is to be run locally. We have not tested it on Uppmax.*


To install R packages use `install.packages` command e.g.
```
install.packages("https://cran.r-project.org/src/contrib/statmod_1.4.30.tar.gz", repo=NULL, type="source")
```

To install Bioconductor packages:
```
source("https://bioconductor.org/biocLite.R")
biocLite(c("csaw","edgeR","org.Hs.eg.db","TxDb.Hsapiens.UCSC.hg19.knownGene"))
```

To install gfortran follow the directions on its [homepage](https://gcc.gnu.org/wiki/GFortranBinaries). Further dependencies may be required for successful installation.

## Getting the data

We will examine differences in REST binding in two cell types: SKNSH and HeLa. We need to download required files. Let's use the Box links for simplicity. 

HeLa:

* [zip](https://stockholmuniversity.box.com/s/2o3lchp61kzxpil1y1snn4onjk4e0sjo)
* [tar.gz](https://stockholmuniversity.box.com/s/wmx4uhgo3esuessr4f8g9kmvarm42bxz)

SKNSH:

* [zip](https://stockholmuniversity.box.com/s/dkurmi5suwh3qnxnx0ysfhh5c0g2d1ti)
* [tar.gz](https://stockholmuniversity.box.com/s/8m3rgtakx8h8rmhnwltitqccbx7h0wy3)

To extract tar.gz files 
```
tar -zxvf archive_name.tar.gz
```

## Loading data and preparing contrast

Modify the paths to folders with respective data to match your local setup:

```
dir.sknsh = "/path/to/data/sknsh"
dir.hela = "/path/to/data/hela"

hela.1=file.path(dir.hela,"ENCFF000PED.chr12.rmdup.sort.bam")
hela.2=file.path(dir.hela,"ENCFF000PEE.chr12.rmdup.sort.bam")
sknsh.1=file.path(dir.sknsh,"ENCFF000RAG.chr12.rmdup.sort.bam")
sknsh.2=file.path(dir.sknsh,"ENCFF000RAH.chr12.rmdup.sort.bam")

bam.files <- c(hela.1,hela.2,sknsh.1,sknsh.2)
```

We need to provide the information about the design of the experiment using model.matrix function:
```
grouping <- factor(c('hela', 'hela', 'sknsh', 'sknsh'))
design <- model.matrix(~0 + grouping)
colnames(design) <- levels(grouping)
```

The design should look like this:
```
> design
  hela sknsh
1    1     0
2    1     0
3    0     1
4    0     1
attr(,"assign")
[1] 1 1
attr(,"contrasts")
attr(,"contrasts")$grouping
[1] "contr.treatment"
```

We prepare the information on contrast to be tested using makeContrasts function from package limma. This is not the only way to do so, and examples are given in csaw and edgeR manuals. In this case we want to test for the differences in REST binding in HeLa vs. SKNSH cell lines:
```
library(edgeR)
contrast <- makeContrasts(hela - sknsh, levels=design)
```

Now we are ready to load data and create an object with counted reads:
```
library(csaw)
data <- windowCounts(bam.files, ext=100, width=10) 
```
Parameters for file loading can be modified (examples in the csaw User Guide), depending on how the data was processed. Here we explicitely input the value for fragment length as we have this information from the cross correlation analysis performed earlier (ChIP-seq data processing tutorial). It is 100 for Hela and 95 & 115 for sknsh.

We can inspect the resulting `data` object, e.g.:
```
> data$totals
[1] 1637778 2009932 2714033 4180463
```

## Filtering out regions with very low coverage

The next step is to filter out uninformative regions, i.e. windows with low read count, which represent background. There are many strategies to do it, depending on the biology of the experiment, IP efficiency and data processing. Here, we filter out lowest 99.9% of the windows, retaining the 0.1% windows with highest signal. The rationale is that for TF experiments only 0.1% of the genome can be bound, hence the remaining must represent background.

```
keep <- filterWindows(data, type="proportion")$filter > 0.999
data.filt <- data[keep,]
```
To investigate the effectiveness of our filtering strategy:

```
> summary(keep)
   Mode   FALSE    TRUE 
logical  145558    9850 
```

## Normalisation

Assigning reads into larger bins for normalisation:
```
binned <- windowCounts(bam.files, bin=TRUE, width=10000)
```

Calculating normalization factors:
```
data.filt <- normOffsets(binned, se.out=data.filt)
```

Inspecting the normalisation factors:
```
> data.filt$norm.factors
[1] 0.9727458 1.0718693 0.9279702 1.0335341
```


## Detecting differentially binding (DB) sites

Detecting DB windows:
```
data.filt.calc <- asDGEList(data.filt)
data.filt.calc <- estimateDisp(data.filt.calc, design)
fit <- glmQLFit(data.filt.calc, design, robust=TRUE)
results <- glmQLFTest(fit, contrast=contrast)
```

Inspecting the results table:
```
> head(results$table)
     logFC   logCPM         F       PValue
1 7.239404 2.165639 17.229173 3.327018e-05
2 5.244217 2.783211  9.484909 2.074540e-03
3 3.023888 2.755437  4.721852 2.979352e-02
4 2.050617 2.612401  2.684560 1.013412e-01
5 1.827703 2.459979  2.459072 1.168638e-01
6 4.336717 2.052296 14.330442 1.538194e-04
```

## Correcting for multiple testing

First we merge adjacent DB windows into longer clusters. Windows that are less than `tol` apart are considered to be adjacent and are grouped into the same cluster. The chosen `tol`
represents the minimum distance at which two binding events are treated as separate sites.
Large values (500 - 1000 bp) reduce redundancy and favor a region-based interpretation of
the results, while smaller values (< 200 bp) allow resolution of individual binding sites.

```
merged <- mergeWindows(rowRanges(data.filt), tol=1000L)
```

Next, we apply the multiple testing correction to obtain FDR. We combine p-values across clustered tests using Simes??? method to control the cluster FDR.

```
table.combined <- combineTests(merged$id, results$table)
```

The resulting `table.combined` object contains FDR for each cluster:

```
> head(table.combined)
  nWindows logFC.up logFC.down       PValue          FDR
1        7        0          7 2.328912e-04 0.0040397108
2        3        0          3 6.989334e-06 0.0004822892
3        3        0          3 1.948039e-04 0.0036799249
4        5        0          5 4.108169e-05 0.0011680754
5        3        0          3 6.674578e-05 0.0017204192
6        5        0          5 1.880546e-04 0.0036207355
  direction
1      down
2      down
3      down
4      down
5      down
6      down
```


* nWindows - the total number of windows in each cluster;
* fields `*.up` and `*.down` - for each log-FC column in `results$table`; contain the number of
windows with log-FCs above 0.5 or below -0.5, respectively;
* PValue - the combined p-value;
* FDR - the q-value corresponding to the combined p-value;
* direction - the dominant direction of change for windows in each cluster.

Each combined p-value represents evidence against the global null hypothesis,
i.e., all individual nulls are true in each cluster. This may be more relevant than examining each
test individually when multiple tests in a cluster represent parts of the same underlying event, e.g.,
genomic regions consisting of clusters of windows. The BH method is then applied to control the
FDR across all clusters.

## Inspecting the results

We select statistically significant DB events at FDR 0.05:

```
is.sig.region <- table.combined$FDR <= 0.05
table(table.combined$direction[is.sig.region])
```

How many regions were detected as differentialy bound?

```
down   up 
 201  231 
```

out of
```
> length(table.combined$FDR)
[1] 2758
```


We can also obtain information on the best window in each cluster:

```
tab.best <- getBestTest(merged$id, results$table)
```
```
> head(tab.best)
  best     logFC   logCPM        F       PValue
1    1 -7.239404 2.165639 17.22917 2.328912e-04
2    8 -7.000913 1.975575 22.31508 6.989334e-06
3   11 -7.339503 2.239557 15.43879 2.565355e-04
4   14 -7.121331 2.071184 19.89740 4.108169e-05
5   19 -7.208420 2.137556 17.99510 6.674578e-05
6   22 -7.477095 2.352131 14.67127 6.418949e-04
           FDR
1 0.0043108304
2 0.0005293418
3 0.0045354163
4 0.0011680754
5 0.0017204192
6 0.0081582774
```

We can inspect congruency of the replicates on MDS. We subsample counts for faster calculations:

```
par(mfrow=c(2,2))
adj.counts <- cpm(data.filt.calc, log=TRUE)
for (top in c(100, 500, 1000, 5000)) {
out <- plotMDS(adj.counts, main=top, col=c("blue", "blue", "red", "red"),
labels=c("hela", "hela", "sknsh", "sknsh"), top=top)
}
```

## Annotation of the results


```
library(org.Hs.eg.db)
library(TxDb.Hsapiens.UCSC.hg19.knownGene)

anno <- detailRanges(merged$region, txdb=TxDb.Hsapiens.UCSC.hg19.knownGene,
orgdb=org.Hs.eg.db, promoter=c(3000, 1000), dist=5000)

merged$region$overlap <- anno$overlap
merged$region$left <- anno$left
merged$region$right <- anno$right
```

## Creating the final object with results and annotation

Now we bring it all together:

```
all.results <- data.frame(as.data.frame(merged$region)[,1:3], table.combined, anno)
```

All significant regions are in:
```
sig=all.results[all.results$FDR<0.05,]
```

To view the top of the `all.results`table:

```
all.results <- all.results[order(all.results$PValue),]
```

```
> head(all.results)
     seqnames     start       end nWindows logFC.up
1726     chr2  25642751  25642760        1        1
822      chr1 143647051 143647060        1        0
876      chr1 149785201 149785210        1        0
386      chr1  40530701  40530710        1        1
2519     chr2 199778551 199778560        1        1
1613     chr2   8683951   8683960        1        0
     logFC.down       PValue          FDR direction
1726          0 7.875683e-07 0.0004407602        up
822           1 1.197351e-06 0.0004407602      down
876           1 1.197351e-06 0.0004407602      down
386           0 1.574877e-06 0.0004407602        up
2519          0 1.574877e-06 0.0004407602        up
1613          1 2.198223e-06 0.0004407602      down
                          overlap                  left
1726                     DTNB|I|-     DTNB|18-19|-[347]
822                                                    
876  HIST2H2BF|0|-,HIST2H3D|0-1|- HIST2H2BF|1-2|-[1273]
386                      CAP1|I|+      CAP1|5-11|+[470]
2519                                                   
1613                                                   
                     right
1726                      
822  <100286793>|10|-[579]
876                       
386     CAP1|12-14|+[1177]
2519                      
1613   
```
We of course discourage ranking the results by p value ;-).

Now you are ready to save the results as a table, inspect further and generate a compelling scientific hypothesis.
You can also compare the outcome with results obtained from peak-based couting approach.

One final note: In this example we have used preprocessed bam files, i.e. reads mapped to the regions of spurious high signal in ChIP-seq (i.e. the ENCODE "blacklisted regions") were removed, as we the so called **duplicated reads** - reads mapped to the same genomic positions. While filtering out the blacklisted regions is always recommended, **removal of duplicated reads is not recommended** for DB analysis, as they may represent true signal. As always, your mileage may vary, depending on the project, so exploring several options is essential for obtaining meaningful results.


<!-- #### for sanity reasons: (need to dig deeper to find a better example)
check against macs2 peaks

bedtools intersect -a hela_1_peaks.chr12.bed -b hela_2_peaks.chr12.bed -f 0.50 -r > peaks_hela.chr12.bed
bedtools intersect -a sknsh_1_peaks.chr12.bed -b sknsh_2_peaks.chr12.bed -f 0.50 -r > peaks_sknsh.chr12.bed

bedtools intersect -a peaks_sknsh.chr12.bed -b peaks_hela.chr12.bed -f 0.50 -r > peaks_sknsh_hela.chr12.bed

    1088 peaks_hela.chr12.bed
    2031 peaks_sknsh.chr12.bed
	473 peaks_sknsh_hela.chr12.bed



all.results <- all.results[order(all.results$start),]

macs2 in sknsh 1:
chr1	1270265	1270622	sknsh_1_REST.enc.macs2_peak_25	2714	.	80.09766	275.94952	271.41241	304

csaw DB:
11       chr1   1270251   1270610        8        7
 -->

<!-- 
 > sessionInfo()
R version 3.4.2 (2017-09-28)
Platform: x86_64-apple-darwin15.6.0 (64-bit)
Running under: OS X El Capitan 10.11.6

Matrix products: default
BLAS: /System/Library/Frameworks/Accelerate.framework/Versions/A/Frameworks/vecLib.framework/Versions/A/libBLAS.dylib
LAPACK: /Library/Frameworks/R.framework/Versions/3.4/Resources/lib/libRlapack.dylib

locale:
[1] en_US.UTF-8/en_US.UTF-8/en_US.UTF-8/C/en_US.UTF-8/en_US.UTF-8

attached base packages:
[1] parallel  stats4    stats     graphics  grDevices utils     datasets 
[8] methods   base     

other attached packages:
 [1] TxDb.Hsapiens.UCSC.hg19.knownGene_3.2.2
 [2] GenomicFeatures_1.30.0                 
 [3] org.Hs.eg.db_3.5.0                     
 [4] AnnotationDbi_1.40.0                   
 [5] csaw_1.12.0                            
 [6] BiocParallel_1.12.0                    
 [7] SummarizedExperiment_1.8.0             
 [8] DelayedArray_0.4.1                     
 [9] matrixStats_0.52.2                     
[10] Biobase_2.38.0                         
[11] GenomicRanges_1.30.0                   
[12] GenomeInfoDb_1.14.0                    
[13] IRanges_2.12.0                         
[14] S4Vectors_0.16.0                       
[15] BiocGenerics_0.24.0                    
[16] edgeR_3.20.1                           
[17] limma_3.34.1                           

loaded via a namespace (and not attached):
 [1] Rcpp_0.12.13             compiler_3.4.2          
 [3] XVector_0.18.0           prettyunits_1.0.2       
 [5] bitops_1.0-6             tools_3.4.2             
 [7] zlibbioc_1.24.0          progress_1.1.2          
 [9] statmod_1.4.30           biomaRt_2.34.0          
[11] digest_0.6.12            bit_1.1-12              
[13] RSQLite_2.0              memoise_1.1.0           
[15] tibble_1.3.4             lattice_0.20-35         
[17] pkgconfig_2.0.1          rlang_0.1.4             
[19] Matrix_1.2-12            DBI_0.7                 
[21] GenomeInfoDbData_0.99.1  rtracklayer_1.38.0      
[23] stringr_1.2.0            Biostrings_2.46.0       
[25] locfit_1.5-9.1           bit64_0.9-7             
[27] grid_3.4.2               R6_2.2.2                
[29] XML_3.98-1.9             RMySQL_0.10.13          
[31] magrittr_1.5             Rhtslib_1.10.0          
[33] blob_1.1.0               splines_3.4.2           
[35] GenomicAlignments_1.14.1 Rsamtools_1.30.0        
[37] assertthat_0.2.0         stringi_1.1.6           
[39] RCurl_1.95-4.8     
-->   

