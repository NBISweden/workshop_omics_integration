FROM jupyter/minimal-notebook:latest
LABEL org.opencontainers.image.source=https://github.com/scilifelabdatacentre/serve-images

ARG SERVE_BRANCH=develop
WORKDIR /home/jovyan

COPY requirements.txt /tmp
COPY umap_env.yml /tmp
COPY lab /home/jovyan/lab
COPY start-script.sh /usr/local/bin/start-script.sh

# Switch to root user to perform installations
USER root
RUN apt-get update && apt-get install curl -y --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/jovyan/lab/data

# Clone the repository and checkout only .txt files from the UMAP_DataIntegration folder
RUN git clone --depth=1 --filter=blob:none --sparse https://github.com/NBISweden/workshop_omics_integration.git /tmp/repo && \
    cd /tmp/repo && \
    git sparse-checkout init --cone && \
    git sparse-checkout set session_ml/UMAP_DataIntegration && \
    find session_ml/UMAP_DataIntegration -name "*.txt" -exec mv {} /home/jovyan/lab/data/ \; && \
    rm -rf /tmp/repo

# Install pip requirements as root
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install mamba
RUN conda install -n base -c conda-forge mamba

# Create conda environment using mamba as root
RUN mamba env create -f /tmp/umap_env.yml && conda clean --all --yes

# Activate conda environment
RUN echo "conda activate umap" >> /etc/profile.d/conda.sh

# Install ipykernel in the conda environment and create a kernel spec
RUN /opt/conda/envs/umap/bin/pip install ipykernel && \
    /opt/conda/envs/umap/bin/python -m ipykernel install --name umap --display-name "Python (umap)"

# Fix permissions and make the script executable
RUN chown -R jovyan:users /opt/conda /home/jovyan/.cache /home/jovyan/lab && \
    chmod -R a+rwx /home/jovyan/lab && \
    find /home/jovyan/lab -type d -exec chmod a+rwx {} \; && \
    find /home/jovyan/lab -type f -exec chmod a+rw {} \; && \
    chmod +x /usr/local/bin/start-script.sh

# Switch back to the non-root user
USER jovyan

# Set default conda environment
ENV PATH /opt/conda/envs/umap/bin:$PATH

# Disable Jupyter token authentication
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.token = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

# Set the startup script as the entrypoint
ENTRYPOINT ["/usr/local/bin/start-script.sh"]