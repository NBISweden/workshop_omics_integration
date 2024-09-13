FROM jupyter/minimal-notebook:latest
LABEL org.opencontainers.image.source=https://github.com/scilifelabdatacentre/serve-images

ARG SERVE_BRANCH=develop
WORKDIR /home/jovyan

COPY requirements.txt /tmp
COPY deepLearningDataIntegration_env.yml /tmp
COPY lab /home/jovyan/lab
COPY start-script.sh /usr/local/bin/start-script.sh

# Switch to root user to perform installations
USER root
RUN apt-get update && apt-get install curl -y --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create data directory
RUN mkdir -p /home/jovyan/lab/data

# Download specific .txt files from GitHub
RUN curl -L https://github.com/NBISweden/workshop_omics_integration/blob/main/session_ml/DeepLearningDataIntegration/scATACseq.txt -o /home/jovyan/lab/data/scATACseq.txt && \
    curl -L https://github.com/NBISweden/workshop_omics_integration/blob/main/session_ml/DeepLearningDataIntegration/scBSseq.txt -o /home/jovyan/lab/data/scBSseq.txt && \
    curl -L https://github.com/NBISweden/workshop_omics_integration/blob/main/session_ml/DeepLearningDataIntegration/scRNAseq.txt -o /home/jovyan/lab/data/scRNAseq.txt && \
    curl -L https://github.com/NBISweden/workshop_omics_integration/blob/main/session_ml/DeepLearningDataIntegration/scRNAseq.txt -o /home/jovyan/lab/data/scRNAseq_CITEseq.txt
    
# Install pip requirements as root
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install mamba
RUN conda install -n base -c conda-forge mamba

# Create conda environment using mamba as root
RUN mamba env create -f /tmp/deepLearningDataIntegration_env.yml && conda clean --all --yes

# Activate conda environment
RUN echo "conda activate deepLearningDataIntegration" >> /etc/profile.d/conda.sh

# Install ipykernel in the conda environment and create a kernel spec
RUN /opt/conda/envs/deepLearningDataIntegration/bin/pip install ipykernel && \
    /opt/conda/envs/deepLearningDataIntegration/bin/python -m ipykernel install --name deepLearningDataIntegration --display-name "Python (deepLearningDataIntegration)"

# Fix permissions and make the script executable
RUN chown -R jovyan:users /opt/conda /home/jovyan/.cache /home/jovyan/lab && \
    chmod -R a+rwx /home/jovyan/lab && \
    find /home/jovyan/lab -type d -exec chmod a+rwx {} \; && \
    find /home/jovyan/lab -type f -exec chmod a+rw {} \; && \
    chmod +x /usr/local/bin/start-script.sh

# Switch back to the non-root user
USER jovyan

# Set default conda environment
ENV PATH /opt/conda/envs/deepLearningDataIntegration/bin:$PATH

# Disable Jupyter token authentication
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.token = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

# Set the startup script as the entrypoint
ENTRYPOINT ["/usr/local/bin/start-script.sh"]