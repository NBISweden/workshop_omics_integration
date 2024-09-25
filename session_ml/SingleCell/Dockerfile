FROM ubuntu:20.04 AS base

ARG RSTUDIO_ARCH="amd64"
ARG RSTUDIO_VERSION="2023.12.1+402"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set locale configs
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Install useful Linux packages and cleanup
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -yq update \
    && apt-get -yq install --no-install-recommends \
      curl \
      wget \
      dpkg-sig \
      libpq5 \
      psmisc \
      sudo \
      lsb-release \
      libclang-dev \
      locales \
      ca-certificates \
      libxml2 \ 
      libodbc1 \
      libglpk-dev \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda and Mamba
RUN curl -LOs https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -bfp /usr/local/miniconda3 \
    && rm Miniconda3-latest-Linux-x86_64.sh \
    && /usr/local/miniconda3/bin/conda install -n base -c conda-forge mamba \
    && ln -s /usr/local/miniconda3/bin/mamba /usr/local/bin/mamba

# Set up environment
ENV PATH="/usr/local/miniconda3/bin:${PATH}"

# Install R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && echo 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/' >> /etc/apt/sources.list \
    && apt-get -yq update \
    && apt-get -yq install --no-install-recommends \
    r-base \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \ 
    && apt-get autoremove -yq && apt-get autoclean -yq

# Install necessary libraries for GLIBCXX_3.4.29
RUN apt-get -yq update \
    && apt-get -yq install --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:ubuntu-toolchain-r/test \
    && apt-get -yq update \
    && apt-get -yq install --no-install-recommends \
    libstdc++6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# INSTALL R packages using Mamba
COPY SingleCell_env.yml /tmp/SingleCell_env.yml
RUN mamba env create -f /tmp/SingleCell_env.yml && rm /tmp/SingleCell_env.yml

# Install R packages that are not available via conda (SeuratData)
RUN R -e "install.packages('remotes', repos='http://cran.us.r-project.org')"
RUN R -e "remotes::install_github('satijalab/seurat-data')"

# Download required files to the data directory
RUN mkdir -p /home/jovyan/lab/data \
    && wget --no-check-certificate -O /home/jovyan/lab/data/scatacseq_activity_matrix.txt "https://drive.google.com/uc?export=download&id=1hBeh2L5PC-T87YObCmJv4Qcm59IqkkOf&confirm=t" \
    && wget -O /home/jovyan/lab/data/atac_v1_pbmc_10k_singlecell.csv "https://cf.10xgenomics.com/samples/cell-atac/1.0.1/atac_v1_pbmc_10k/atac_v1_pbmc_10k_singlecell.csv" \
    && wget -O /home/jovyan/lab/data/atac_v1_pbmc_10k_filtered_peak_bc_matrix.h5 "https://cf.10xgenomics.com/samples/cell-atac/1.0.1/atac_v1_pbmc_10k/atac_v1_pbmc_10k_filtered_peak_bc_matrix.h5" \
    && wget -O /home/jovyan/lab/data/pbmc_10k_v3.rds "https://www.dropbox.com/s/3f3p5nxrn5b3y4y/pbmc_10k_v3.rds?dl=1"

# Download and install RStudio Server
RUN curl -sL "https://download2.rstudio.org/server/focal/${RSTUDIO_ARCH}/rstudio-server-${RSTUDIO_VERSION//+/-}-${RSTUDIO_ARCH}.deb" -o /tmp/rstudio-server.deb && \
    echo "64044984a5791690586e21bf4411019ed3dccaf32a69e0838090762f3eba8da0  /tmp/rstudio-server.deb" | sha256sum -c - && \
    dpkg -i /tmp/rstudio-server.deb && \
    rm -f /tmp/rstudio-server.deb && \
    echo "lock-type=advisory" > /etc/rstudio/file-locks \
    && echo "www-frame-origin=same" >> /etc/rstudio/rserver.conf

# Common environment variables
ENV USER=jovyan
ENV GROUP=users
ENV PASSWORD=default
ENV DISABLE_AUTH=1
ENV UID=1000
ENV HOME=/home/${USER}
ENV R_HOME=usr/lib/R

RUN useradd -s /bin/bash -N -u ${UID} -l ${USER} \
    && mkdir -p ${HOME} \
    && echo "${USER}:password123" | chpasswd \
    && chown -R ${USER}:${GROUP} ${HOME} \
    && chown -R ${USER}:${GROUP} /etc/rstudio/ \
    && chown -R ${USER}:${GROUP} /var/run/rstudio-server/ \
    && chown -R ${USER}:${GROUP} /usr/lib/rstudio-server/ \
    && chown -R ${USER}:${GROUP} /var/lib/rstudio-server/

# R needs TZ set
RUN echo "TZ=Etc/UTC" >> ${R_HOME}/etc/Renviron.site

# Set default CRAN repo to RSPM (it has pre-compiled R packages, increasing user install speed)
RUN echo 'options(repos=c(CRAN="https://packagemanager.rstudio.com/all/__linux__/focal/latest"))' >> ${R_HOME}/etc/Rprofile.site \
 && echo 'options(HTTPUserAgent=sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version$platform, R.version$arch, R.version$os)))' >> ${R_HOME}/etc/Rprofile.site

WORKDIR ${HOME}

COPY run.sh /etc/run.sh
RUN chmod +x /etc/run.sh
COPY lab ${HOME}/lab
RUN chown -R ${USER}:${GROUP} ${HOME}/lab \
    && chmod -R u+w ${HOME}/lab

USER ${USER}
EXPOSE 8787

ENTRYPOINT ["/etc/run.sh"]
