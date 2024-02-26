FROM ubuntu:20.04 as base

ARG RSTUDIO_ARCH="amd64"
ARG RSTUDIO_VERSION=2022.12.0+353

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Set locale configs
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

# Install useful Linux packages and cleanup
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get -yq update \
    && apt-get -yq install --no-install-recommends \
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
ENV PATH="/usr/local/miniconda3/envs:${PATH}"

# Install R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && echo 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/' >> /etc/apt/sources.list \
    && apt-get -yq update \
    && apt-get -yq install --no-install-recommends \
    r-base \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \ 
    && apt-get autoremove -yq && apt-get autoclean -yq

# INSTALL R packages using Mamba
COPY environment.yml /tmp/environment.yml
RUN mamba env create -f /tmp/environment.yml \
    && rm /tmp/environment.yml


RUN curl -sL "https://download2.rstudio.org/server/bionic/${RSTUDIO_ARCH}/rstudio-server-${RSTUDIO_VERSION//+/-}-${RSTUDIO_ARCH}.deb" -o /tmp/rstudio-server.deb \
 && gpg --keyserver keys.gnupg.net --keyserver pgp.surfnet.nl --recv-keys 3F32EE77E331692F \
 && dpkg-sig --verify /tmp/rstudio-server.deb \
 && dpkg -i /tmp/rstudio-server.deb \
 && rm -f /tmp/rstudio-server.deb \
 && echo "lock-type=advisory" > /etc/rstudio/file-locks \
 && echo "www-frame-origin=same" >> /etc/rstudio/rserver.conf

# Common environment variables
ENV USER jovyan
ENV GROUP users
ENV PASSWORD default
ENV DISABLE_AUTH 1
ENV UID 1000
ENV HOME /home/$USER
ENV R_HOME usr/lib/R

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
RUN echo 'options(repos=c(CRAN="https://packagemanager.rstudio.com/all/__linux__/focal/latest"))' >>  ${R_HOME}/etc/Rprofile.site \
 && echo 'options(HTTPUserAgent=sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version$platform, R.version$arch, R.version$os)))' >> ${R_HOME}/etc/Rprofile.site


WORKDIR $HOME

COPY run.sh /etc/run.sh
RUN chmod +x /etc/run.sh
COPY lab /home/jovyan/lab
RUN chmod +x /home/jovyan/lab

USER ${USER}
EXPOSE 8787

ENTRYPOINT ["/etc/run.sh"]