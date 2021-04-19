---
layout: default
title:  'Labs'
---

### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Lab instructions

#### Clone the course repository

Retrieve the entire repository including all datasets and notebooks.
```
cd ~/Desktop/course
git clone git@github.com:NBISweden/workshop_omics_integration.git .
```

Inside you will find the following folders:
- `environments/` - all conda environments necessary for running notebooks
- `session_preprocessing/` - data pre-processing, prior to course start
- `session_ml/` - the machine learning sessions, days 1 and 2
- `session_topology/` - the network topology analysis, day 3 morning
- `session_meta/` - network meta-analysis, day 3 afternoon
- `session_nmf/` - session on matrix factorization, SNF and recommender systems, day 4 morning
- `session_gems/` - the genome-scale modeling session, day 4 afternoon
- `session_gsa/` - gene set and reporter feature, day 5 morning
- `.../` - remaining folders not necessary for running any of the contents

You will need to create specific [conda environments as indicated below](#environments).

#### Environments

See the [pre-course installation](./precourse.md), specifically [**3. Create and activate the environment**](./precourse.md#3-create-and-activate-the-environment).  
***Environments*** - we merged the environments for many notebooks down to 4 environments. 
- Data pre-processing (linux: `env-preprocessing_linux.yaml` | macOS: `env-preprocessing.yaml`)
- Supervised Integration & Feature selection (linux: `env-ml_linux.yaml` | macOS: `env-ml.yaml`)
- Meta analysis (linux | macOS `/session_meta/renv.lock`)
- All remaining notebooks (linux `env-ml_nets_linux.yaml` | MacOS `env-ml_nets.yaml`)

Alternatively, you can find smaller environments below.

##### Before the course: data pre-processing

- **Data pre-processing:**
    - environment macOS: `/environments/env-preprocessing.yaml` 
    - environment linux: `/environments/env-preprocessing_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_preprocessing/preprocessing.html)): `/session_preprocessing/preprocessing.ipynb`


##### Day 1: Supervised and Unsupervised integration
In MacOSX you need to install [XQuartz](https://www.xquartz.org/) if you get errors related with `rgl`:
```
install.packages('session_ml/rgl_0.100.54.tgz', repos = NULL, type="source", dependencies = TRUE)
```

- **Supervised integration:**
    - environment macOS: `/environments/env-ml.yaml`
    - environment linux: `/environments/env-ml_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/SupervisedOMICsIntegration/supervised_omics_integr_CLL.html)): `/session_ml/SupervisedOMICsIntegration/supervised_omics_integr_CLL/supervised_omics_integr_CLL.Rmd`

- **Feature selection:**
    - environment macOS: `/environments/env-ml.yaml`
    - environment linux: `/environments/env-ml_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/FeatureSelectionIntegrOMICs/OmicsIntegration_FeatureSelection.html)): `session_ml/FeatureSelectionIntegrOMICs/OmicsIntegration_FeatureSelection.Rmd`


- **Unsupervised integration:**
    - environment macOS: `/environments/env-ml_day2.yaml`
    - environment linux: `/environments/env-ml_day2_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/UnsupervisedOMICsIntegration/UnsupervisedOMICsIntegration.html)): `session_ml/UnsupervisedOMICsIntegration/UnsupervisedOMICsIntegration.Rmd`



##### Day 2: Unsupervised integration, dimensionality reduction, deep learning, single-cell omics integration
After activating the environment as above, open the `.Rmd` below by launching Rstudio with `rstudio &` or the jupyter notebooks with `jupyter-notebook`.

- **Dimensionality reduction:**
    - environment macOS: `/environments/env-ml_day2.yaml`
    - environment linux: `/environments/env-ml_day2_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/DimReductSingleCell/OmicsIntegration_DimensionReduction.html)): `session_ml/DimReductSingleCell/OmicsIntegration_DimensionReduction.Rmd`


- **UMAP for data integration:**
    - Note that the data needs to be decompressed before running the notebook `gunzip scRNAseq.csv.gz; gunzip scProteomics.csv.gz`
    - environment macOS: `/environments/env-ml_day2.yaml`
    - environment linux: `/environments/env-ml_day2_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/UMAP_DataIntegration/UMAP_DataIntegration.html)): `session_ml/UMAP_DataIntegration/UMAP_DataIntegration.ipynb`


- **Deep learning:**
    - environment macOS: `/environments/env-ml_day2.yaml`
    - environment linux: `/environments/env-ml_day2_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/DeepLearningDataIntegration/DeepLearningDataIntegration.html)): `session_ml/DeepLearningDataIntegration/DeepLearningDataIntegration.ipynb`


- **Single cell:**
    - environment macOS: `/environments/env-ml_day2.yaml`
    - environment linux: `/environments/env-ml_day2_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/SingleCell/SingleCell_OmicsIntegration.html)): `session_ml/SingleCell/SingleCell_OmicsIntegration.Rmd`


##### Day 3: Network topology
- **Network topology:**
    - environment macOS: `/environments/env-merged_nets.yaml`
    - environment linux: `/environments/env-merged_nets_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_topology/lab.html)): `/session_topology/lab.ipynb`


- **Meta analyses:**
    - environment macOS:`/session_meta/renv.lock`
    - environment linux:`/session_meta/renv.lock`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_meta/lab_meta-analayses-v2.html)): `/session_meta/lab_meta-analayses-v2.Rmd`


##### Day 4: GEM structure and simulation with Cobrapy
- **Genome-scale metabolic modeling:**
    - environment macOS: `/environments/env-merged_nets.yaml`
    - environment linux: `/environments/env-merged_nets_linux.yaml`
    - notebook ([html](https://nbisweden.github.io/workshop_omics_integration/session_gems/lab.html)): `/session_gems/lab.ipynb`


##### Day 5: Gene set and reporter analysis
- **Gene set analysis and reporter features:**
    - environment macOS: `/environments/env-merged_nets.yaml`
    - environment linux: `/environments/env-merged_nets_linux.yaml`
    - notebook: ([html](https://nbisweden.github.io/workshop_omics_integration/session_gsa/GEM_GSA.html)): `/session_gsa/GEM_GSA.Rmd`