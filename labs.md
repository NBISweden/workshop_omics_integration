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
- **Machine learning Day 1**  
Create the environment:  
```
#Linux
conda env create -n envml -f environments/env-ml_linux.yaml
#MacOSX
conda env create -n envml -f environments/env-ml.yaml
```

Activate the environment
```
conda activate envml
```

From this point, follow the instructions below in each respective session. At the end deactivate the environment with `conda deactivate`.

- **Machine learning Day 2**  
Create the environment:  
```
#Linux
conda env create -n envml_day2 -f environments/env-ml_day2_linux.yaml
#MacOSX
conda env create -n envml_day2 -f environments/env-ml_day2.yaml
```

Activate the environment
```
conda activate envml_day2
```

From this point, follow the instructions below in each respective session. At the end deactivate the environment with `conda deactivate`.


- **Network topology, visualization, metabolic modeling and GSA labs (days 3-5)**   
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

##### Day 1: Supervised integration and feature selection
After activating the environment as above, launch Rstudio with `rstudio &`. 

In MacOSX, you also need to install [XQuartz](https://www.xquartz.org/). If you get errors related with `rgl` after launching mixomics, please install it:
```
install.packages('session_ml/rgl_0.100.54.tgz', repos = NULL, type="source", dependencies = TRUE)
```

- **Supervised integration:**  
data, [Rmd](./session_ml/SupervisedOMICsIntegration/supervised_omics_integr_CLL.Rmd) and [.html](./session_ml/SupervisedOMICsIntegration/supervised_omics_integr_CLL.html) are within folder `session_ml/SupervisedOMICsIntegration/`.

- **Feature selection:**  
data, [Rmd](./session_ml/FeatureSelectionIntegrOMICs/OmicsIntegration_FeatureSelection.Rmd) and [.html](./session_ml/FeatureSelectionIntegrOMICs/OmicsIntegration_FeatureSelection.html) are within folder `session_ml/FeatureSelectionIntegrOMICs/`.

##### Day 2: Unsupervised integration, dimensionality reduction, deep learning, single-cell omics integration
After activating the environment as above, open the `.Rmd` below by launching Rstudio with `rstudio &` or the jupyter notebooks with `jupyter-notebook`.

- **Unsupervised integration:**  
data, [Rmd](./session_ml/UnsupervisedOMICsIntegration/UnsupervisedOMICsIntegration.Rmd) and [.html](./session_ml/UnsupervisedOMICsIntegration/UnsupervisedOMICsIntegration.html) are within folder `session_ml/UnsupervisedOMICsIntegration/`.

- **Dimensionality reduction:**  
data, [Rmd](./session_ml/DimReductSingleCell/OmicsIntegration_DimensionReduction.Rmd) and [.html](./session_ml/DimReductSingleCell/OmicsIntegration_DimensionReduction.html) are within folder `session_ml/DimReductSingleCell/`.

- **UMAP for data integration**  
data, [jupyter notebook](./session_ml/UMAP_integration/UMAP_DataIntegration.ipynb) and [.html](./session_ml/UMAP_integration/UMAP_DataIntegration.html) are within folder `session_ml/UMAP_integration/`. Note that the data needs to be decompressed before running the notebook:
```
gunzip scRNAseq.csv.gz
gunzip scProteomics.csv.gz
```

- **Deep learning:**  
data, [jupyter notebook](./session_ml/DeepLearningDataIntegration/DeepLearningDataIntegration.ipynb) and [.html](./session_ml/DeepLearningDataIntegration/DeepLearningDataIntegration.html) are within folder `session_ml/DeepLearningDataIntegration/`.

- **Single cell:**  
[jupyter notebook](./session_ml/SingleCell/SingleCell_OmicsIntegration.Rmd) and [.html](./session_ml/SingleCell/SingleCell_OmicsIntegration.html) are within the folder `session_ml/SingleCell`). Data for this lab can be downloaded [from here](https://drive.google.com/file/d/1hBeh2L5PC-T87YObCmJv4Qcm59IqkkOf/view?usp=sharing).


##### Day 3: Network topology
After creating and activating the environment, launch jupyter
```
jupyter-notebook
```
Inside jupyter, open the file `/session_topology/lab.ipynb`.

##### Day 4: GEM structure and simulation with Cobrapy
After activating the `envnets` environment, launch jupyter
```
jupyter-notebook
```
Inside jupyter, open the file `/session_gems/COBRApy_tutorial.ipynb`.

##### Day 5: GEM-based gene set analysis
After activating the `envnets` environment, launch jupyter
```
jupyter-notebook
```
Inside jupyter, open the file `/session_gems/GEM_GSC_extraction.ipynb`.

When you are done with the `GEM_GSC_extraction.ipynb` notebook, close jupyter.

Open the `/session_gems/GEM_GSA.html` file in the browser of your choice (Chrome, Firefox, etc.), and follow the instructions provided in that document.


