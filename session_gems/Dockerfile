# Base image
FROM jupyter/minimal-notebook:latest
LABEL org.opencontainers.image.source=https://github.com/scilifelabdatacentre/serve-images

ARG SERVE_BRANCH=develop
WORKDIR /home/jovyan

# Copy necessary files
COPY requirements.txt /tmp
COPY gems_env.yml /tmp
COPY lab /home/jovyan/lab
COPY start-script.sh /usr/local/bin/start-script.sh

# Switch to root user for installations
USER root

# Install system dependencies including Java
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git openjdk-11-jre && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Clone data folder from GitHub
RUN git clone --depth=1 --filter=blob:none --sparse https://github.com/NBISweden/workshop_omics_integration.git /tmp/repo && \
    cd /tmp/repo && \
    git sparse-checkout set session_gems/lab/data && \
    mv session_gems/lab/data /home/jovyan/lab/data && \
    rm -rf /tmp/repo

# Install pip requirements
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install mamba
RUN conda install -n base -c conda-forge mamba

# Create conda environment (with Python 3.8)
RUN mamba env create -f /tmp/gems_env.yml && conda clean --all --yes

# Activate conda environment (Python 3.8)
RUN echo "source activate gems" > ~/.bashrc && \
    echo "conda activate gems" >> ~/.bashrc

# Install ipykernel in the conda environment
RUN /opt/conda/envs/gems/bin/pip install ipykernel && \
    /opt/conda/envs/gems/bin/python -m ipykernel install --name gems --display-name "Python (gems)"

# Fix permissions and make the script executable
RUN chown -R jovyan:users /opt/conda /home/jovyan/.cache /home/jovyan/lab && \
    chmod -R a+rwx /home/jovyan/lab && \
    chmod +x /usr/local/bin/start-script.sh

# Switch back to the non-root user
USER jovyan

# Set default conda environment
ENV PATH /opt/conda/envs/gems/bin:$PATH

# Disable Jupyter token authentication
RUN /opt/conda/envs/gems/bin/jupyter notebook --generate-config && \
    echo "c.NotebookApp.token = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

# Set the startup script as the entrypoint
ENTRYPOINT ["/usr/local/bin/start-script.sh"]