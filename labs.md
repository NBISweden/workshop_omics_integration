---
layout: default
title:  'Labs'
---

#### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Lab instructions

##### Environments
For the [network topology lab](#network-topology-lab), [network visualization lab](#network-visualization-lab), [metabolic modeling lab](#metabolic-modeling-lab), and [GSA-lab](#gsa-lab) you will need a single conda environment.

1. Download the conda environment
```
# Linux
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/environments/env-merged_nets_linux.yaml
# MacOSX
curl -o env-merged_nets.yaml https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/environments/env-merged_nets.yaml
```

2. Create the environment
```
#Linux
conda env create -n envnets -f env-merged_nets_linux.yaml
#MacOSX
conda env create -n envnets -f env-merged_nets.yaml
```

3. Activate the environment
```
conda activate envtopology
```

From this point, follow the instructions below in each respective session. At the end deactivate the environment with `conda deactivate`.


##### Network topology lab

1. Download the data
```
#Linux
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/met_genes.tsv
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/proteinatlas.tsv
#MacOSX
curl -o met_genes.tsv https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/met_genes.tsv
curl -o proteinatlas.tsv https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/data/proteinatlas.tsv
```

2. Download the jupyter notebook
```
# Linux
wget https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/lab.ipynb
# MacOSX
curl -o lab.ipynb https://raw.githubusercontent.com/NBISweden/workshop_omics_integration/master/session_topology/lab.ipynb
```

3. Activate the environment and start the jupyter notebook
```
jupyter-notebook
```

If you get an error `Not a directory: 'xdg-settings'` please [check this for a solution](https://github.com/jupyter/notebook/issues/3746#issuecomment-444957821).