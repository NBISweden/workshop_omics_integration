---
layout: default
title:  'Labs'
---

#### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Lab instructions

##### Topology lab

1. Download the data
```
#Linux
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/met_genes.tsv
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/proteinatlas.tsv

#MacOSX
curl -o met_genes.tsv https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/met_genes.tsv
curl -o proteinatlas.tsv https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/proteinatlas.tsv
```

2. Download the conda environment and jupyter notebook
```
# Linux
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/env-topology.yaml
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/lab.ipynb

# MacOSX
curl -o env-topology.yaml https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/env-topology.yaml
curl -o lab.ipynb https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/lab.ipynb
```

3. Create the environment, activate it, and start the jupyter notebook
```
conda env create -n envtopology -f env-topology.yaml
conda activate envtopology
jupyter-notebook
```

If you get an error `Not a directory: 'xdg-settings'` please [check this for a solution](https://github.com/jupyter/notebook/issues/3746#issuecomment-444957821).
