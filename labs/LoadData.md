---
layout: default
title:  'Loading data'
---
# Loading data
<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline4">1. Introduction</a>
<ul>
<li><a href="#orgheadline1">1.1. The scan function</a></li>
<li><a href="#orgheadline3">1.2. The read.table function</a>
</li>
</ul>
</li>
</ul>
</div>
</div>

# Introduction<a id="orgheadline4"></a>

Up until now we have mostly created the object we worked with on the
fly from within R. The most common use-case is however to read in
different data sets that are stored as files, either somewhere on a
server or locally on your computer. In this exercise we will test some
common ways to import data in R and also show to save data from
R. After this exercise you will know how to:

-   Read data from txt files and save the information as a vector, data frame or
    a list.
-   Identify missing data and correctly encode this at import
-   Check that imported objects are imported correctly
-   Read data from online resource
-   Write data to a file

## The scan function<a id="orgheadline1"></a>

The function scan() can be used both to read data from files and
directly from keyboard. The function is very flexible and have many
different settings that allow to read data in different formats. To
read and store a set of words that you type on your keyboard try the
following code that will prompt your for input. After each word press
enter and R will prompt you for new input. After the last word have
been typed press enter twice to get back to your R prompt and have
your character vector named words available in R your session.

    words <- scan(what = character())

### Exercises

{% highlight R %}
shelley.vec <- scan(file = "book_chapter.txt", what = character())
str(shelley.vec)

shelley.list <- scan(file = "book_chapter.txt", what = list(character()))
class(shelley.list)

Read 420 items
 
chr [1:420] "My" "present" "situation" "was" "one" "in" ...
Read 420 records
[1] "list"
{% endhighlight %}

```R
shelley.vec <- scan(file = "book_chapter.txt", what = character())
str(shelley.vec)

shelley.list <- scan(file = "book_chapter.txt", what = list(character()))
class(shelley.list)

Read 420 items
 
chr [1:420] "My" "present" "situation" "was" "one" "in" ...
Read 420 records
[1] "list"
```

~~~ ruby
puts "Hello!"
~~~

Download the file book chapter from this [link](../files/book_chapter.txt). Read the manual for
scan and read the text file named book\_chapter.txt into R, first as
vector and then as a list, with each word in the chapter saved as a
entry in the vector or as a single vector in a list.
<details>
<summary> Click to see how</summary>
```
shelley.vec <- scan(file = "book_chapter.txt", what = character())
str(shelley.vec)

shelley.list <- scan(file = "book_chapter.txt", what = list(character()))
class(shelley.list)

Read 420 items
 
chr [1:420] "My" "present" "situation" "was" "one" "in" ...
Read 420 records
[1] "list"
```

</details>
<br>

Check that your newly created objects contain the correct information
and have been saved as you have intended eg. each entry of the vector
or the list should contain a single word. Once your convinced that you
have a sound word vector and list.

1.  Identify the longest word in your vector.
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
    
        sort(nchar(shelley.vec), decreasing = TRUE)
        which(nchar(shelley.vec) == max(nchar(shelley.vec)))
        shelley.vec[381]

      [1] 690  12  11  10  10  10  10  10  10  10  10  10  10  10  10  10  10  10
     [19]   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9   9
     [37]   9   9   8   8   8   8   8   8   8   8   8   8   8   8   8   8   8   8
     [55]   8   8   8   8   8   8   8   8   8   8   7   7   7   7   7   7   7   7
     [73]   7   7   7   7   7   7   7   7   7   7   7   7   7   7   7   7   7   6
     [91]   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6
    [109]   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6   6
    [127]   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5
    [145]   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5
    [163]   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5   5
    [181]   5   5   5   5   5   4   4   4   4   4   4   4   4   4   4   4   4   4
    [199]   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4
    [217]   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4   4
    [235]   4   4   4   4   4   4   4   3   3   3   3   3   3   3   3   3   3   3
    [253]   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3
    [271]   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3
    [289]   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3
    [307]   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3   3
    [325]   3   3   3   3   2   2   2   2   2   2   2   2   2   2   2   2   2   2
    [343]   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2
    [361]   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2
    [379]   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2   2
    [397]   2   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1   1
    [415]   1   1   1   1   1   1
    [1] 381
    [1] "By the sacred earth on which I kneel, by the shades that wander near me, by the deep and eternal grief that I feel, I swear; and by thee, O Night, and the spirits that preside over thee, to pursue the daemon who caused this misery, until he or I shall perish in mortal conflict. For this purpose I will preserve my life; to execute this dear revenge will I again behold the sun and tread the green herbage of earth, which otherwise should vanish from my eyes forever. And I call on you, spirits of the dead, and on you, wandering ministers of vengeance, to aid and conduct me in my work. Let the cursed and hellish monster drink deep of agony; let him feel the despair that now torments me."
	</pre>
	</details>
<br>
2.  Go back and fix the way you read in the text to make sure that you
    get a vector with all words in chapter as individual entries also
    filter any non-letter characters and now identify the longest word.
<details>
    <summary>:key: Click to see how</summary>
{% highlight R %}
shelley.vec2 <- scan(file = "book_chapter.txt", what = " ", quote = NULL)
shelley.filt2 <- gsub(pattern = '[^[:alnum:] ]', replacement = "", x = shelley.vec2)
which(nchar(shelley.filt2) == max(nchar(shelley.filt2)))
shelley.filt2[301]

Read 551 items
[1] 301
[1] "uninterested"
{% endhighlight %}
</details>
<br>

## The read.table function<a id="orgheadline3"></a>

This is the by far most common way to get data into R. As the function
creates a data frame at import it will only work for data set that
fits those criteria, meaning that the data needs to have a set of
columns of equal length that are separated with a common string
eg. tab, comma, semicolon etc. 

In this code block with first import the data from normalized.txt from
a file (that you can get [here](../files/normalized.txt)) and accept the defaults for all other
arguments in the function. With this settings R will read it as a tab
delimited file and will use the first row of the data as colnames
(header) and the first column as rownames.

    expr.At <- read.table("normalized.txt")
    head(expr.At)

                  bZIP29_1  bZIP29_2  bZIP29_3        WT_1      WT_2       WT_3
    AT1G01020.1  13.572739 14.167143 12.972703  14.8181738 15.904017 11.3270623
    AT1G01030.1   1.417234  1.201454  1.385434   0.8590246  1.096829  0.8596431
    AT1G01040.2  41.862906 41.199853 42.696566  37.5286358 34.849241 48.6456871
    AT1G01050.1 102.422397 98.318969 92.068406 104.2104178 97.418336 86.0654463
    AT1G01060.1   3.216031  4.004846  3.589534   3.7045434  2.642360  6.2703380
    AT1G01070.1   8.230858 17.871625 14.924906   7.9996663  8.824486 13.8554244

One does however not have to have all data as a file an the local
disk, instead one can read data from online resources. The following
command will read in a file from a web server.

    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    abalone = read.table(url, header = F , sep = ',') 
    head(abalone)

      V1    V2    V3    V4     V5     V6     V7    V8 V9
    1  M 0.455 0.365 0.095 0.5140 0.2245 0.1010 0.150 15
    2  M 0.350 0.265 0.090 0.2255 0.0995 0.0485 0.070  7
    3  F 0.530 0.420 0.135 0.6770 0.2565 0.1415 0.210  9
    4  M 0.440 0.365 0.125 0.5160 0.2155 0.1140 0.155 10
    5  I 0.330 0.255 0.080 0.2050 0.0895 0.0395 0.055  7
    6  I 0.425 0.300 0.095 0.3515 0.1410 0.0775 0.120  8

### Exercises

1.  Download the file [example.data](../files/example.data) to your
    computer and import it to R using the read.table function. This
    files consist of gene expression values. Once you have the object
    in R validate that it looks okay and export it using the
    write.table function. Encode all NA values as "missing", at
    export.  
	<details> 
	<summary>:key: Click to see how</summary> 
	<pre>
    
        ed <- read.table("example.data", sep = ":")
        head(ed)
        str(ed)
    
                        V1               V2               V3               V4
        1         bZIP29_1         bZIP29_2         bZIP29_3             WT_1
        2             <NA> 14.1671426761817 12.9727029171751 14.8181737869517
        3 1.41723379939617 1.20145379585993             <NA>             <NA>
        4 41.8629060744716 41.1998530830302 42.6965659118674  37.528635786519
        5 102.422396502516 98.3189689612045 92.0684061403395 104.210417827802
        6             <NA> 4.00484598619978 3.58953430232514 3.70454344673793
                        V5               V6
        1             WT_2             WT_3
        2             <NA>             <NA>
        3   1.096828754225             <NA>
        4 34.8492408728761 48.6456870599298
        5 97.4183357161658  86.065446336799
        6 2.64236018063295 6.27033804098888
		
        'data.frame':   18946 obs. of  6 variables:
         $ V1: Factor w/ 3053 levels "0","0.0545089922844682",..: 3053 NA 27 1844 85 NA 2715 2291 1260 1052 ...
         $ V2: Factor w/ 3265 levels "0","0.0500605748274972",..: 3265 579 25 1970 3242 1920 879 2473 1184 1313 ...
         $ V3: Factor w/ 2888 levels "0","0.0629742860057041",..: 2888 304 NA 1802 2775 1449 527 2574 1026 1034 ...
         $ V4: Factor w/ 3112 levels "0","0.05368903545997",..: 3112 555 NA 1746 117 1500 2597 1830 1319 NA ...
         $ V5: Factor w/ 3234 levels "0","0.0498558524647727",..: 3234 NA 23 1689 3193 1036 NA 2157 1337 1556 ...
         $ V6: Factor w/ 3287 levels "0","0.0505672422660393",..: 3287 NA NA 2187 3047 2495 NA 2494 1143 944 ...
	 </pre>
	 </details>
<br>

	<details>
	<summary>:key: Click to see how</summary>
	<pre>
   	
		write.table(x = ed, na = "missing", file = "example_mis.data")
	</pre>
	</details>
<br>

2.  Read in the file you just created and double-check that you have the same data as earlier.
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
    
        df.test <- read.table("example_mis.data", na.strings = "missing")

	</pre>
	</details>
<br>

3. Analysing genome annotation in R using read.table

For this exercise we will load a GTF file into R and calculate some
basic summary statistics from the file. In the first part we will use
basic manipulations of data frames to extract the information. In the
second part you get a try out a library designed to work with
annotation data, that stores the information in a more complex format,
that allow for easy manipulation and calculation of summaries from
genome annotation files.

For those not familiar with the gtf format it is a file format
containing annotation information for a genome. It does not contain
the actual DNA sequence of the organism, but instead refers to
positions along the genome.

A valid GTF file should contain the following tab delimited fields
(taken from the ensembl home page).

1.  seqname - name of the chromosome or scaffold; chromosome names can
    be given with or without the 'chr' prefix.
2.  source - name of the program that generated this feature, or the
    data source (database or project name)
3.  feature - feature type name, e.g. Gene, Variation, Similarity
4.  start - Start position of the feature, with sequence numbering
    starting at 1.
5.  end - End position of the feature, with sequence numbering starting
    at 1.
6.  score - A floating point value.
7.  strand - defined as + (forward) or - (reverse).
8.  frame - One of '0', '1' or '2'. '0' indicates that the first base
    of the feature is the first base of a codon, '1' that the second
    base is the first base of a codon, and so on..
9.  attribute - A semicolon-separated list of tag-value pairs,
    providing additional information about each feature.

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-right">1.</th>
<th scope="col" class="org-left">2.</th>
<th scope="col" class="org-left">3.</th>
<th scope="col" class="org-right">4.</th>
<th scope="col" class="org-right">5.</th>
<th scope="col" class="org-left">6.</th>
<th scope="col" class="org-left">7.</th>
<th scope="col" class="org-left">8.</th>
<th scope="col" class="org-left">9.</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-right">1</td>
<td class="org-left">transcribed_unprocessed_pseudogene</td>
<td class="org-left">gene</td>
<td class="org-right">11869</td>
<td class="org-right">14409</td>
<td class="org-left">.</td>
<td class="org-left">+</td>
<td class="org-left">.</td>
<td class="org-left">gene_id; "ENSG00000223972";</td>
</tr>


<tr>
<td class="org-right">1</td>
<td class="org-left">processed_transcript</td>
<td class="org-left">transcript</td>
<td class="org-right">11869</td>
<td class="org-right">14409</td>
<td class="org-left">.</td>
<td class="org-left">+</td>
<td class="org-left">.</td>
<td class="org-left">gene_id; "ENSG00000223972";</td>
</tr>
</tbody>
</table>

The last column can contain a large number of attributes that are
comma-separated.

As these files for many organisms are large we will in this exercise
use the latest version of Drosophila melanogaster genome annotation
available at
<ftp://ftp.ensembl.org/pub/release-86/gtf/drosophila_melanogaster> that
is small enough for analysis even on a laptop.  

Open this and download the file named
Drosophila\_melanogaster.BDGP6.86.gtf.gz to your computer. Unzip this
file and keep track of where your store the file.

With this done read this file into R using the function read.table and
add meaningful column names to the table.
<details>
<summary>:key: Click to see how</summary>
<pre>
    
	d.gtf <- read.table("Drosophila_melanogaster.BDGP6.86.gtf",
                        header = FALSE, comment.char = "#", sep = "\t")
    colnames(d.gtf) <- c("Chromosome", "Source", "Feature", "Start",
                         "End", "Score", "Strand", "Frame", "Attribute")
</pre>
</details>
<br>

Prior to any analysis you should make sure that your attempt to read
in the file has worked as expected. This can for example be done by
having a look at the dimension of the stored object and making sure
that it has the structure you expect. 

<details>
<summary>:key: Click to see how</summary>
<pre>

    dim(d.gtf)
    str(d.gtf)

    [1] 538684      9
    'data.frame':   538684 obs. of  9 variables:
     $ Chromosome: Factor w/ 57 levels "211000022278158",..: 51 51 51 51 51 51 51 51 51 51 ...
     $ Source    : Factor w/ 2 levels "FlyBase","ensembl": 1 1 1 1 1 1 1 1 1 1 ...
     $ Feature   : Factor w/ 9 levels "CDS","Selenocysteine",..: 5 9 3 5 9 3 1 6 3 1 ...
     $ Start     : int  722370 722370 722370 835381 835381 835381 835381 835381 869486 869486 ...
     $ End       : int  722621 722621 722621 2503907 2503907 835491 835491 835383 869548 869548 ...
     $ Score     : Factor w/ 1 level ".": 1 1 1 1 1 1 1 1 1 1 ...
     $ Strand    : Factor w/ 2 levels "+","-": 2 2 2 1 1 1 1 1 1 1 ...
     $ Frame     : Factor w/ 4 levels ".","0","1","2": 1 1 1 1 1 1 2 2 1 2 ...
     $ Attribute : Factor w/ 455338 levels "gene_id FBgn0000003; gene_name 7SLRNA:CR32864; gene_source FlyBase; gene_biotype lincRNA;",..: 348579 348581 348580 453172 453215 453194 453195 453193 453199 453200 ...
</pre>
</details>
<br>

1.  How many chromosome names can be found in the annotation file?
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
    
        levels(d.gtf$Chromosome)
    
         [1] "211000022278158"           "211000022278279"          
         [3] "211000022278282"           "211000022278298"          
         [5] "211000022278307"           "211000022278309"          
         [7] "211000022278436"           "211000022278449"          
         [9] "211000022278498"           "211000022278522"          
        [11] "211000022278603"           "211000022278604"          
        [13] "211000022278664"           "211000022278724"          
        [15] "211000022278750"           "211000022278760"          
        [17] "211000022278875"           "211000022278877"          
        [19] "211000022278878"           "211000022278879"          
        [21] "211000022278880"           "211000022278985"          
        [23] "211000022279055"           "211000022279108"          
        [25] "211000022279132"           "211000022279134"          
        [27] "211000022279165"           "211000022279188"          
        [29] "211000022279222"           "211000022279264"          
        [31] "211000022279342"           "211000022279392"          
        [33] "211000022279446"           "211000022279528"          
        [35] "211000022279529"           "211000022279531"          
        [37] "211000022279555"           "211000022279681"          
        [39] "211000022279708"           "211000022280133"          
        [41] "211000022280328"           "211000022280341"          
        [43] "211000022280347"           "211000022280481"          
        [45] "211000022280494"           "211000022280645"          
        [47] "211000022280703"           "2L"                       
        [49] "2R"                        "3L"                       
        [51] "3R"                        "4"                        
        [53] "Unmapped_Scaffold_8"       "X"                        
        [55] "Y"                         "dmel_mitochondrion_genome"
        [57] "rDNA"

	</pre>
	</details>
<br>
2.  How many exons is there in total and per chromosome?
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
    
        aggregate(d.gtf$Feature, by = list(d.gtf$Chromosome), summary)
    
                             Group.1 x.CDS x.Selenocysteine x.exon x.five_prime_utr
        1            211000022278158     0                0      1                0
        2            211000022278279     0                0      1                0
        3            211000022278282     0                0      1                0
        4            211000022278298     0                0      1                0
        5            211000022278307     0                0      1                0
        6            211000022278309     0                0      1                0
        7            211000022278436     0                0      1                0
        8            211000022278449     0                0      2                0
        9            211000022278498     0                0      1                0
        10           211000022278522     0                0      1                0
        11           211000022278603     0                0      1                0
        12           211000022278604     0                0      1                0
        13           211000022278664     0                0      1                0
        14           211000022278724     0                0      1                0
        15           211000022278750     0                0      1                0
        16           211000022278760     2                0      2                0
        17           211000022278875     0                0      1                0
        18           211000022278877     0                0      1                0
        19           211000022278878     0                0      1                0
        20           211000022278879     0                0      1                0
        21           211000022278880     0                0      1                0
        22           211000022278985     0                0      1                0
        23           211000022279055     0                0      1                0
        24           211000022279108     0                0      1                0
        25           211000022279132     0                0      1                0
        26           211000022279134     0                0      1                0
        27           211000022279165     0                0      1                0
        28           211000022279188     3                0      3                1
        29           211000022279222     0                0      1                0
        30           211000022279264     0                0      1                0
        31           211000022279342     0                0      1                0
        32           211000022279392     0                0      1                0
        33           211000022279446     0                0      1                0
        34           211000022279528     0                0      1                0
        35           211000022279529     0                0      1                0
        36           211000022279531     0                0      1                0
        37           211000022279555     0                0      1                0
        38           211000022279681     0                0      1                0
        39           211000022279708     0                0      1                0
        40           211000022280133     0                0      1                0
        41           211000022280328     4                0      4                1
        42           211000022280341     0                0      1                0
        43           211000022280347     0                0      1                0
        44           211000022280481     0                0      1                0
        45           211000022280494     0                0      2                0
        46           211000022280645     0                0      1                0
        47           211000022280703     0                0      1                0
        48                        2L 28047                2  32747             8374
        49                        2R 33657                0  38551             8842
        50                        3L 29473                0  34347             8738
        51                        3R 37167                0  43159            10693
        52                         4  2732                0   3165              570
        53       Unmapped_Scaffold_8    12                0     14                4
        54                         X 28967                2  34136             8824
        55                         Y   111                0    182               13
        56 dmel_mitochondrion_genome    13                0     37                0
        57                      rDNA     0                0     21                0	
	</pre>
	</details>
<br>	
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
		
		by(data = d.gtf$Feature, d.gtf[,"Chromosome"], summary)
		d.gtf[, "Chromosome"]: 211000022278158
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278279
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278282
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278298
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278307
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278309
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278436
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278449
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               2               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278498
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278522
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278603
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278604
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278664
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278724
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278750
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278760
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      2               0               2               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      1               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278875
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278877
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
			d.gtf[, "Chromosome"]: 211000022278878
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278879
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278880
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022278985
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279055
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279108
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279132
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279134
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279165
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279188
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      3               0               3               1               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      1               1               1               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279222
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279264
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279342
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279392
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279446
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279528
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279529
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279531
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279555
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279681
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022279708
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280133
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280328
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      4               0               4               1               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      1               1               1               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280341
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280347
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280481
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280494
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               2               0               2 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               2 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280645
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 211000022280703
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0               1               0               1 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0               1 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 2L
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                  28047               2           32747            8374            3465 
            start_codon      stop_codon three_prime_utr      transcript 
                   5675            5656            6142            6632 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 2R
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                  33657               0           38551            8842            3601 
            start_codon      stop_codon three_prime_utr      transcript 
                   6028            6018            6484            6927 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 3L
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                  29473               0           34347            8738            3433 
            start_codon      stop_codon three_prime_utr      transcript 
                   5873            5853            6352            6676 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 3R
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                  37167               0           43159           10693            4125 
            start_codon      stop_codon three_prime_utr      transcript 
                   7105            7092            7782            8010 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: 4
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                   2732               0            3165             570             111 
            start_codon      stop_codon three_prime_utr      transcript 
                    295             289             339             343 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: Unmapped_Scaffold_8
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                     12               0              14               4               2 
            start_codon      stop_codon three_prime_utr      transcript 
                      3               3               2               3 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: X
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                  28967               2           34136            8824            2647 
            start_codon      stop_codon three_prime_utr      transcript 
                   5372            5351            5921            5973 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: Y
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                    111               0             182              13              71 
            start_codon      stop_codon three_prime_utr      transcript 
                     23              22              10              72 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: dmel_mitochondrion_genome
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                     13               0              37               0              37 
            start_codon      stop_codon three_prime_utr      transcript 
                     12              10               0              37 
        ------------------------------------------------------------ 
        d.gtf[, "Chromosome"]: rDNA
                    CDS  Selenocysteine            exon  five_prime_utr            gene 
                      0               0              21               0              19 
            start_codon      stop_codon three_prime_utr      transcript 
                      0               0               0              19
    </pre>
	</details>
<br>
3.  Filter the data frame to only retain gene annotations
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
		d.gtf.gene <- d.gtf[d.gtf$Feature == "gene",]
	</pre>
	</details>
<br>

4.  What is the average gene length of in the Drosophila genome?
	<details>
	<summary>:key: Click to see how</summary>
	<pre>

    mean(abs(d.gtf.gene$Start - d.gtf.gene$End))

    [1] 5753.282
	</pre>
	</details>
<br>

5.  What fraction of the genes are encoded on the plus strand of
    the genome.
	<details>
	<summary>:key: Click to see how</summary>
	<pre>

    sum(d.gtf.gene$Strand == "+") / length(d.gtf.gene$Strand)

    [1] 0.5016231
	</pre>
	</details>
<br>

6.  What is the median and mean length of the exons found on chromosome
    3R in the data set?
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
    
        d.gtf3R <- d.gtf[d.gtf$Chromosome == "3R",]
        exon.position <- d.gtf3R[d.gtf3R$Feature == "exon",c("Start", "End")]   
        median(abs(exon.position$Start - exon.position$End))
        mean(abs(exon.position$Start - exon.position$End))
    
        [1] 251
        [1] 468.6693
	</pre>
	</details>
<br>

7.  Do the same calculations for the chromosomes 2L, 2R, 3L, 4, X and Y
    using a for loop.
	<details>
	<summary>:key: Click to see how</summary>
	<pre>
    
             chr <- c("2L", "2R", "3L", "4", "X", "Y")
             for (i in chr) {
                  d.gtf.tmp <- d.gtf[d.gtf$Chromosome == i,]
                  exon.position <- d.gtf.tmp[d.gtf.tmp$Feature == "exon", c("Start", "End")]   
                  exon.med <- median(abs(exon.position$Start - exon.position$End))
                  exon.mean <- mean(abs(exon.position$Start - exon.position$End))
                  txt <- sprintf("The median and mean exon length for %s is %g and %g, respectively", i, exon.med, exon.mean)
                  print(txt)
        }
    
        [1] "The median and mean exon length for 2L is 279 and 502.617, respectively"
        [1] "The median and mean exon length for 2R is 225 and 437.187, respectively"
        [1] "The median and mean exon length for 3L is 255 and 502.116, respectively"
        [1] "The median and mean exon length for 4 is 198 and 429.573, respectively"
        [1] "The median and mean exon length for X is 257 and 526.301, respectively"
        [1] "The median and mean exon length for Y is 410.5 and 657.055, respectively"
	</pre>
	</details>
<br>


