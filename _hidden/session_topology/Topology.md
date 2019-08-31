

...[Leiden algorithm](https://leidenalg.readthedocs.io/en/latest/reference.html#optimiser) vs Louvain

add iris:

from sklearn import datasets
iris=datasets.load_iris()
iris.data


# Python igraph

Installation of Python's igraph in OSX can be done using

    pip3 install python-igraph

For Windows and Linux, please [see the official instructions on GitHub][1].

You may find some bugs namely:
- `AttributeError: 'bytes' object has no attribute 'encode'` [see example bug][2]
- Inconsistent naming when plotting multiple graphs in Jupyter [see example bug][3]
These are fixed by replacing a few lines in the `/igraph/drawing/__init__.py`. See [this for a fix][4]

Unfortunately, the current conda version (`0.7.1.post7`) still contains these bugs and they need to be manually fixed.

# Databases

The resources below present several well-known databases for [PPIs](#ppis), [Gene Regulatory Networks](#gene-regulatory-networks), [Metabolic](#metabolic) and [mixed interactions](#mixed). This is far from being an exaustive list.



# PPIs

- [EBI Intact database](http://string-db.org/)
- [Human protein reference database](http://www.hprd.org/)
- [Human protein interaction database](http://wilab.inha.ac.kr/hpid/webforms/intro.aspx)
- [Human reference interactome](http://interactome.baderlab.org/)
- [Molecular Interaction Database - MINT](http://string-db.org/)
- [String](https://string-db.org/cgi/input.pl) 

# Metabolic
- [KEGG](https://www.genome.jp/kegg/)
- [MetaCyc](https://metacyc.org/)


# Mixed

- [BioGRID](https://thebiogrid.org/) - genetic, protein, chemical, and post-translational modifications
- [Inetmodels](http://inetmodels.com/) - gene-gene, gene-metabolite, and other tissue-specific and disease networks
- [IntAct](https://www.ebi.ac.uk/intact/) - mixed molecular interactions from literature curation or user submission
- [Stitch](http://stitch.embl.de/) - chemical-protein interaction networks

# Gene regulatory networks

- [JASPAR](http://jaspar.genereg.net/)
- [TRANSFAC](http://genexplain.com/transfac/) - paid



[1]: https://github.com/igraph/python-igraph
[2]: https://github.com/igraph/python-igraph/issues/88#issuecomment-275945879
[3]: https://github.com/igraph/python-igraph/issues/243#issue-484047476
[4]: https://github.com/igraph/python-igraph/pull/148/files