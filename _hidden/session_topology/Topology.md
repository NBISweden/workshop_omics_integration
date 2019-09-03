

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

# Comparison of centrality measures
- [CINNA in R](https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-018-0598-2)


[1]: https://github.com/igraph/python-igraph
[2]: https://github.com/igraph/python-igraph/issues/88#issuecomment-275945879
[3]: https://github.com/igraph/python-igraph/issues/243#issue-484047476
[4]: https://github.com/igraph/python-igraph/pull/148/files