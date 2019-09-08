
In this workshop you will use [Python igraph][1] to analyse a gene expression network. To get all the
necessary software you can use the [conda environment file](../environment.yml). See the quick conda 
[instructions below](#conda-instructions).


#### Accessing the workshop notebook

After downloading the conda *environment.yml*, create the conda environment by running
```
	conda env create -f environment.yml -p top-env
	conda activate top-env
```

After this you can simply launch jupyter by typing `jupyter-notebook` in 
terminal. At the end, run `conda deactivate` to close the environment. For more details see [here][5].  

If you prefer to do it manually, you can:
1. Install Python and Jupyter
- [Python 3.7.4](https://www.python.org/downloads/)
- [Jupyter 6.0.0](https://jupyter-notebook.readthedocs.io/en/stable/)
2. Install [pip][6]
3. Install igraph dependencies. You can see installation instructions [on GitHub][1].
4. Install the required packages 
```
pip3 install pandas numpy cairo python-igraph seaborn matplotlib leidenalg scipy matplotlib gseapy pycairo glpk scikit-learn
```

#### Accessing the data
Retrieve the data [from the data folder](data/). You will start with the file [data/gene_expression.tsv](data/gene_expression.tsv), which contains the [TPMs][7] of 843 genes, and 48 samples.

#### Python igraph

Your environment file already contains igraph for Python. However, you may find some bugs:
- `AttributeError: 'bytes' object has no attribute 'encode'` [see example bug][2]
- Inconsistent naming when plotting multiple graphs in Jupyter [see example bug][3]

**Fix:** replace a few lines in the file `/top-env/lib/python3.7/site-packages/igraph/__init__.py` by doing [this][4].


#### Databases

The resources below present some well-known databases for [PPIs](#ppis), [Gene Regulatory Networks](#gene-regulatory-networks), [Metabolic](#metabolic) and [mixed interactions](#mixed).

**Collections**  
- [NAR Database issue][13] - a collection of databases by topic

**PPIs**  
- [Database of Interacting Proteins][12]
- [EBI Intact database](http://string-db.org/)
- [Human protein reference database](http://www.hprd.org/)
- [Human protein interaction database](http://wilab.inha.ac.kr/hpid/webforms/intro.aspx)
- [Human reference interactome](http://interactome.baderlab.org/)
- [String](https://string-db.org/cgi/input.pl) 

**Metabolic**  
- [Metabolic Atlas]
- [KEGG][15]
- [MetaCyc][14]
- [Reactome][8]
- [Virtual Metabolic Human][9]


**Mixed**  
- [BioCyc][10] - pathway and genome databases for many model organisms
- [BioGRID](https://thebiogrid.org/) - genetic, protein, chemical, and post-translational modifications
- [Inetmodels](http://inetmodels.com/) - gene-gene, gene-metabolite, and other tissue-specific and disease networks
- [IntAct](https://www.ebi.ac.uk/intact/) - mixed molecular interactions from literature curation or user submission
- [NDex][11] - a database for network exchange. Contains many reference networks including **NCI's Pathway Interaction Database**
- [Stitch](http://stitch.embl.de/) - chemical-protein interaction networks

**networks**  
- [JASPAR](http://jaspar.genereg.net/)
- [TRANSFAC](http://genexplain.com/transfac/) - paid


[1]: https://github.com/igraph/python-igraph
[2]: https://github.com/igraph/python-igraph/issues/88#issuecomment-275945879
[3]: https://github.com/igraph/python-igraph/issues/243#issue-484047476
[4]: https://github.com/igraph/python-igraph/pull/148/files
[5]: ../conda_instructions.md
[6]: https://pip.readthedocs.io/en/latest/installing/
[7]: https://www.rna-seqblog.com/rpkm-fpkm-and-tpm-clearly-explained/
[8]: http://www.reactome.org
[9]: https://www.vmh.life/#home
[10]: http://biocyc.org/
[11]: https://home.ndexbio.org/index/
[12]: https://dip.doe-mbi.ucla.edu/dip/Main.cgi
[13]: http://www.oxfordjournals.org/nar/database/c
[14]: https://metacyc.org/
[15]: https://www.genome.jp/kegg/
[16]: https://www.metabolicatlas.org/