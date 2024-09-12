#!/bin/bash
# Activate the conda environment
source /opt/conda/bin/activate deepLearningDataIntegration

#Add metadata to jupyter notebook to select deepLearningDataIntegration kernel from startup
jq '.metadata.kernelspec = {"display_name": "Python (deepLearningDataIntegration)", "language": "python", "name": "deepLearningDataIntegration"}' /home/jovyan/lab/DeepLearningDataIntegration.ipynb > tmp.$$.json && mv tmp.$$.json /home/jovyan/lab/DeepLearningDataIntegration.ipynb

# Start the Jupyter Notebook server
exec jupyter notebook --allow-root --notebook-dir=/home/jovyan/lab
