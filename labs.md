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

***Environments*** - we have merged the environments for many notebooks down to 4 environments. 
- Data pre-processing (linux: `env-preprocessing_linux.yaml` | macOS: `env-preprocessing.yaml`)
- Supervised Integration & Feature selection (linux: `env-ml_linux.yaml` | macOS: `env-ml.yaml`)
- Meta analysis (linux | macOS `/session_meta/renv.lock`)
- All remaining notebooks (linux `env-ml_nets_linux.yaml` | MacOS `env-ml_nets.yaml`)

### Day 1 notebooks

- Data pre-processing ([html](https://nbisweden.github.io/workshop_omics_integration/session_preprocessing/preprocessing.html)): `/session_preprocessing/preprocessing.ipynb`
    
- Supervised Omics Integration ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/SupervisedOMICsIntegration/supervised_omics_integr_CLL.html)): `/session_ml/SupervisedOMICsIntegration/supervised_omics_integr_CLL/supervised_omics_integr_CLL.Rmd`

- Feature selection ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/FeatureSelectionIntegrOMICs/OmicsIntegration_FeatureSelection.html)): `session_ml/FeatureSelectionIntegrOMICs/OmicsIntegration_FeatureSelection.Rmd`
    
-  Unsupervised Omics Integration ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/UnsupervisedOMICsIntegration/UnsupervisedOMICsIntegration.html)): `session_ml/UnsupervisedOMICsIntegration/UnsupervisedOMICsIntegration.Rmd`



### Day 2 notebooks

- Dimensionality reduction and clustering ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/DimReductSingleCell/OmicsIntegration_DimensionReduction.html)): `session_ml/DimReductSingleCell/OmicsIntegration_DimensionReduction.Rmd`



- Deep Learning ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/DeepLearningDataIntegration/DeepLearningDataIntegration.html)): `session_ml/DeepLearningDataIntegration/DeepLearningDataIntegration.ipynb`
    
- Single cell ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/SingleCell/SingleCell_OmicsIntegration.html)): `session_ml/SingleCell/SingleCell_OmicsIntegration.Rmd`

- UMAP for integration ([html](https://nbisweden.github.io/workshop_omics_integration/session_ml/UMAP_DataIntegration/UMAP_DataIntegration.html)): `session_ml/UMAP_DataIntegration/UMAP_DataIntegration.ipynb`

### Day 3 notebooks

- Network topology ([html](https://nbisweden.github.io/workshop_omics_integration/session_topology/lab.html)): `/session_topology/lab.ipynb`

- Network meta-analysis ([html](https://nbisweden.github.io/workshop_omics_integration/session_meta/lab_meta-analayses-v2.html)): `/session_meta/lab_meta-analyses-v2.Rmd`
    
    
### Day 4 notebooks

- SNF and Matrix Factorization: TBD
    
- Genome-scale metabolic modeling ([html](https://nbisweden.github.io/workshop_omics_integration/session_gems/lab.html)): `/session_gems/lab.ipynb`

### Day 5 notebooks

- Gene set analysis and reporter features ([html](https://nbisweden.github.io/workshop_omics_integration/session_gsa/GEM_GSA.html)): `/session_gsa/GEM_GSA.Rmd`
