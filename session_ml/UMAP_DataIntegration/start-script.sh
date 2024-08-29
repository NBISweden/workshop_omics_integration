#!/bin/bash
# Activate the conda environment
source /opt/conda/bin/activate umap

#Add metadata to jupyter notebook to select umap kernel from startup
jq '.metadata.kernelspec = {"display_name": "Python (umap)", "language": "python", "name": "umap"}' /home/jovyan/lab/UMAP_DataIntegration.ipynb > tmp.$$.json && mv tmp.$$.json /home/jovyan/lab/UMAP_DataIntegration.ipynb

# Start the Jupyter Notebook server
exec jupyter notebook --allow-root --notebook-dir=/home/jovyan/lab
