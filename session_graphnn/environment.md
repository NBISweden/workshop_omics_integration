```
# run on the docker desktop terminal
# pull ubuntu image from the docker hub
$ docker pull ubuntu
# spin a container based on ubuntu
$ docker run -it -p 8888:8888 -v C:\data\work\Dropbox\work_sync\compbio\projects\course_iomics:/home/lab --name course_iomics ubuntu
# update apt and install wget, then conda
$ cd /home/ubuntu
$ apt update
$ apt install wget
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
# install to /root/miniconda3
# say yes to updating the bash profile
# exit and reopen the shell to get the miniconda hooks
$ exit
$ bash
# optional: in case conda base is not initialized call this to run it
$ eval "$(/root/miniconda3/bin/conda shell.bash hook)"
# upgrade conda
$ conda update -n base -c conda-forge conda
$ conda config --add channels defaults
# jupyter install, can be left for later
$ conda install jupyterlab
$ jupyter lab --ip 0.0.0.0 --port 8888 --no-browser --allow-root
#Access the notebook through your desktops browser on http://localhost:8888 The notebook will prompt you for a token which was generated when you create the notebook. But one of the last link in the output will have the token in its POST message
# install datasci env (for topology session, part 1 lab)
$ conda create -n datasci
$ conda create --name datasci python=3.12
$ conda activate datasci
$ conda install jupyterlab
$ conda install scipy pandas numpy
$ conda install scikit-learn statsmodels
$ conda install matplotlib seaborn
#problems:
# matplotlib needs downgrade
$ conda list matplotlib
$ conda search matplotlib
$ conda install matplotlib<3.9.0
$ conda install matplotlib=3.8.4
# removing teh env
conda env list
conda env remove --name datasci
# install igraph
conda create --name igraph python=3.12
$ conda activate igraph
$ conda install -c conda-forge jupyterlab
$ conda install -c conda-forge python-igraph
$ conda install conda-forge::pycairo
$ conda install conda-forge::leidenalg
$ conda install pandas
#install gseapy
conda create -n gseapy python=3.12
conda activate gseapy
conda install anaconda::pip
pip install gseapy
conda install jupyterlab
#install graphnn
conda create --name graphnn python=3.12
conda activate graphnn
conda install jupyterlab
conda install pytorch::pytorch
# conda install pyg -c pyg #didnt work, issues with glibc
pip install torch_geometric
# conda install scikit-learn
# conda install matplotlib
conda install pandas
pip install snfpy
conda install scikit-learn
conda install matplotlib
conda install conda-forge::pytorch_cluster
```
```
jupyter lab --ip 0.0.0.0 --port 8888 --no-browser --allow-root
```