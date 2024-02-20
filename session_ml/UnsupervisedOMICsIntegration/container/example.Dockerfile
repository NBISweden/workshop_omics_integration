FROM rocker/tidyverse:4.3.0

ARG NCPUS=${NCPUS:--1}

COPY uoi /rocker_scripts/

RUN chmod +x /rocker_scripts/install_bioconductor.sh
RUN /rocker_scripts/install_bioconductor.sh

RUN Rscript /rocker_scripts/reticulate_install_bioconductor.R

## Make user rstudio owner of the Python environment dirs
RUN chgrp -R rstudio /opt/conda && \
    sudo chmod 770 -R /opt/conda
RUN chgrp -R rstudio /opt/venv && \
    sudo chmod 770 -R /opt/venv

RUN