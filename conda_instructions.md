# Getting started

In this workshop you will use the classroom computers, so you'll have all the necessary software installed
and ready to run everything.  

Briefly, conda allows users to run pieces of code just like the developer created them.

<img src="img/conda_illustration.png" width="800">

If you want to install the same software on your own laptop after the course, you can follow the 
instructions below to do so. These rely on [Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html), a self-contained directory that 
you can use in order to reproduce all your results.

Briefly, you need to:  

1. Install Conda and download the `.yaml` file
2. Create and activate the environment
3. Deactivate the environment after running your analyses

You can [read more](https://nbis-reproducible-research.readthedocs.io/en/latest/conda/) about Conda environments and other important concepts to help you make your research reproducible.


**Install Conda and download the environment file**

You should start by installing Conda. We suggest installing either Miniconda, or Anaconda if storage is 
not an issue. After [installing Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), 
download one of the Conda environment files and put it in your working folder. You will be using one of the following:

- [env-machine-learning.yml][2]
- [env-networks.yml][3]
- [env-modeling.yml][4]

**Create and activate the environment**

In terminal, `cd` to your working folder and create an environment called `project_myproject` from the 
`environment.yaml` file:

```
conda env create -p project_myproject -f environment.yaml
```

This may take several minutes to run, and at the end you should see something like this:

```
##Preparing transaction: done
##Verifying transaction: done
##Executing transaction: done
###
### To activate this environment, use
###
###     $ conda activate /my/file/path/project_myproject
###
### To deactivate an active environment, use
###
###     $ conda deactivate
```

You then need to activate your environment, like so:

```
conda activate project_myproject
```

This enables you to run any of the software that was installed into your environment; from this point on you can run any of the contents from the course. For instance, you can directly launch RStudio by typing `rstudio`.

**Deactivate the environment**

After you've ran all your analyses, deactivate the environment by typing `conda deactivate`.

[2]: env-machine-learning.yml
[3]: env-networks.yml
[4]: env-modeling.yml

