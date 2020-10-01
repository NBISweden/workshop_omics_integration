---
layout: default
title:  'Labs'
---

#### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Lab instructions

##### Clone the course repository

Retrieve the entire repository including all datasets and notebooks.
```
git clone https://github.com/NBISweden/workshop_omics_integration.git
```

Change to the newly created directory
```
cd workshop_omics_integration
```

Inside you will find the following folders:  
- `session_ml/` - the machine learning sessions, days 1 and 2  
- `session_topology/` - the network topology analysis, day 3  
- `session_nmf/` - session on matrix factorization, SNF and recommender systems, day 4 morning  
- `session_gems/` - the genome-scale modeling session, day 4 afternoon and day 5 morning  
- `session_visualization/` - cytoscape session day 3 afternoon, circos and hive plots day 5  

You will need to create specific [conda environments as indicated below](#environments)  

##### Environments
- **Network topology, visualization, metabolic modeling and GSA labs**   
Create the environment
```
#Linux
conda env create -n envnets -f environments/env-merged_nets_linux.yaml
#MacOSX
conda env create -n envnets -f environments/env-merged_nets.yaml
```

Activate the environment
```
conda activate envnets
```

From this point, follow the instructions below in each respective session. At the end deactivate the environment with `conda deactivate`.

##### Network topology lab (day 3)
After creating and activating the environment, launch jupyter
```
jupyter-notebook
```
Inside jupyter, open the file `/session_topology/lab.ipynb`.