FROM ubuntu:20.04 AS base

ARG RSTUDIO_ARCH="amd64"
ARG RSTUDIO_VERSION="2024.04.2-764"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set locale configs
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Install useful Linux packages and cleanup
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -yq update \
    && apt-get -yq install \
      curl \
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
      libssl-dev \
      libxml2-dev \
      libcurl4-gnutls-dev \
      libpq-dev \
      libz-dev \
      make \
      gcc \
      ca-certificates \
      gettext \
      libexpat1-dev \
      dh-autoreconf \
      libcurl3-gnutls \
      python3-pip \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen \
    && rm -rf /var/lib/apt/lists/*

# Install R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && echo 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/' >> /etc/apt/sources.list \
    && apt-get -yq update \
    && apt-get -yq install \
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
    && apt-get -yq install \
    libstdc++6 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Download and compile Git from source
RUN curl -L https://github.com/git/git/archive/v2.37.3.tar.gz | tar xz && \
    cd git-2.37.3 && \
    make prefix=/usr/local all && \
    make prefix=/usr/local install

# Clean up packages that were only needed for building
RUN apt-get remove -y dh-autoreconf libz-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /git-2.37.3

# Set git to be used
RUN git --version

# Install Miniconda
RUN curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && bash Miniconda3-latest-Linux-x86_64.sh -bfp /usr/local/miniconda3 \
    && rm Miniconda3-latest-Linux-x86_64.sh

# Set up environment
ENV PATH="/usr/local/miniconda3/bin:$PATH"

COPY UnsupervisedOMICsIntegration_env.yml /tmp/UnsupervisedOMICsIntegration_env.yml
RUN conda env update -n base -f /tmp/UnsupervisedOMICsIntegration_env.yml
# Clean up Conda cache to reduce image size
RUN conda clean -afy

# Download and install RStudio Server
RUN curl -sL "https://download2.rstudio.org/server/focal/${RSTUDIO_ARCH}/rstudio-server-${RSTUDIO_VERSION//+/-}-${RSTUDIO_ARCH}.deb" -o /tmp/rstudio-server.deb && \
    echo "bca4cccfabac87af2a54584f48a9751107c7dac82c845f397dc616bc02b27b4a /tmp/rstudio-server.deb" | sha256sum -c - && \
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

WORKDIR ${HOME}
COPY run.sh /etc/run.sh
RUN chmod +x /etc/run.sh
COPY lab ${HOME}/lab

RUN mkdir -p /home/jovyan/lab/data
RUN apt-get update && apt-get install -y git && \
git clone https://github.com/NBISweden/workshop_omics_integration.git /tmp/repo && \
cd /tmp/repo && \
find session_ml/UnsupervisedOMICsIntegration -name "*.txt" -exec mv {} /home/jovyan/lab/data/ \; && \
rm -rf /tmp/repo

RUN chown -R ${USER}:${GROUP} ${HOME}/lab \
    && chmod -R u+w ${HOME}/lab

USER ${USER}
EXPOSE 8787

ENTRYPOINT ["/etc/run.sh"]
