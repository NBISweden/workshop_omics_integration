#!/bin/bash

# Activate Conda environment
export PATH="/usr/local/miniconda3/bin:$PATH"
source activate GEM_GSA_env

# using rstudio with non-root and `--auth-none=1` inexplicably requires USER to be set
echo -e "password123\n${PASSWORD}\n${PASSWORD}" | passwd

echo "Starting server..."

/usr/lib/rstudio-server/bin/rserver \
  --server-daemonize=0 \
  --server-working-dir=${HOME} \
  --server-user=${USER} \
  --www-address=0.0.0.0 \
  --www-port=8787 \
  --auth-none=${DISABLE_AUTH} \
  --rsession-which-r=$(which R)