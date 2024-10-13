#!/bin/bash
# Activate the conda environment
source /opt/conda/bin/activate nmf
# Start the Jupyter Notebook server
exec jupyter notebook --allow-root --notebook-dir=/home/jovyan/lab
