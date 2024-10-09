FROM jupyter/minimal-notebook:latest
LABEL org.opencontainers.image.source=https://github.com/scilifelabdatacentre/serve-images

ARG SERVE_BRANCH=develop
WORKDIR /home/jovyan

COPY requirements.txt /tmp
COPY *.yml /tmp
COPY lab /home/jovyan/lab
COPY start-script.sh /usr/local/bin/start-script.sh

# Switch to root user to perform installations
USER root
RUN apt-get update && apt-get install curl -y --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install pip requirements as root
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install mamba
RUN conda install -n base -c conda-forge mamba

# Install datasci environment
RUN mamba env create -f /tmp/datasci_env.yml && conda clean --all --yes

# Install igraph environment
RUN mamba env create -f /tmp/igraph_env.yml && conda clean --all --yes

# Install gseapy environment
RUN mamba env create -f /tmp/gseapy_env.yml && conda clean --all --yes

# Activate conda environment
RUN echo "conda activate datasci" >> /etc/profile.d/conda.sh

# Install ipykernel in the datasci environment and create a kernel spec
RUN /opt/conda/envs/datasci/bin/pip install ipykernel && \
    /opt/conda/envs/datasci/bin/python -m ipykernel install --name datasci --display-name "Python (datasci)"

# Install ipykernel in the igraph environment and create a kernel spec
RUN /opt/conda/envs/igraph/bin/pip install ipykernel && \
    /opt/conda/envs/igraph/bin/python -m ipykernel install --name igraph --display-name "Python (igraph)"

# Install ipykernel in the gseapy environment and create a kernel spec
RUN /opt/conda/envs/gseapy/bin/pip install ipykernel && \
    /opt/conda/envs/gseapy/bin/python -m ipykernel install --name gseapy --display-name "Python (gseapy)"

# Create a data directory
RUN mkdir -p /home/jovyan/lab/data
# Install git to clone the repository
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/NBISweden/workshop_omics_integration.git /tmp/repo && \
    cp -r /tmp/repo/session_topology/lab/data/* /home/jovyan/lab/data/ && \
    rm -rf /tmp/repo

# Fix permissions and make the script executable
RUN chown -R jovyan:users /opt/conda /home/jovyan/.cache /home/jovyan/lab && \
    chmod -R a+rwx /home/jovyan/lab && \
    chmod +x /usr/local/bin/start-script.sh

# Switch back to the non-root user
USER jovyan

# Set default conda environment
ENV PATH /opt/conda/envs/datasci/bin:$PATH

# Disable Jupyter token authentication
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.token = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.ip = '0.0.0.0'" >> /home/jovyan/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.open_browser = False" >> /home/jovyan/.jupyter/jupyter_notebook_config.py

# Set the startup script as the entrypoint
ENTRYPOINT ["/usr/local/bin/start-script.sh"]
