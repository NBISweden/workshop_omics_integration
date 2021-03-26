---
layout: default
title:  Pre-course
---

{::options parse_block_html="true" /}

#### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Programming with R and Python  
***

The course will be taught using both R and Python depending on the tools available. While you will be able to follow all lectures and exercises conceptually, you should be familiar with basic usage of both programming languages as these are **requirements for the course**:  
- R (part_1): [https://swcarpentry.github.io/r-novice-inflammation/](https://swcarpentry.github.io/r-novice-inflammation/)
- R (part_2): [http://swcarpentry.github.io/r-novice-gapminder/](http://swcarpentry.github.io/r-novice-gapminder/)
- Python (part_1):[https://swcarpentry.github.io/python-novice-inflammation/](https://swcarpentry.github.io/python-novice-inflammation/)
- Python (part_2): [http://swcarpentry.github.io/python-novice-gapminder/](http://swcarpentry.github.io/python-novice-gapminder/)

You should be familiar with dataframe, matrix, vector manipulation, functions and (in python) methods.  

You should also be familiar with basic command line input (`mkdir`, `cd`, `ls`, `cp`, `mv`).

#### <img border="0" src="https://www.svgrepo.com/show/26916/book.svg" width="15" height="15"> Additional reading materials  
***

For additional information on some of the topics that we will discuss, refer to the [reading materials][5].

#### <img border="0" src="https://hackernoon.com/hn-images/1*rW03Wtue71AKfxnx6XN_iQ.png" width="50" height="50"> Conda Instructions
***

During this workshop, you will use conda environments to run the exercises. This is because conda environments allow all users to have the same computing environment, i.e. package versions. This enforces reproducibility for you to run this material without the need to re-install or change your local versions. See and graphical example below:

<img border="0" src="https://nbisweden.github.io/excelerate-scRNAseq/logos/conda_illustration.png" width="600">

[Conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) are a self-contained directory that you can use in order to reproduce all your results.

Briefly, you need to:  

[1. Install Conda and Mamba](#1-download-and-install-conda-and-mamba)  
[2. Install git and clone the repository](#2-install-git-clone-the-repository)  
[3. Create and activate the environment](#3-create-and-activate-the-environment)  
[4. Launch RStudio or Jupyter](#4-launch-rstudio-or-jupyter)  
[5. Deactivate the environment after running your analyses](#5-deactivate-the-environment)  

You can [read more](https://nbis-reproducible-research.readthedocs.io/en/latest/conda/) about Conda environments and other important concepts to help you make your research reproducible.

<br/>

##### 1. Download and install Conda and Mamba

Start by installing Conda. We suggest installing **Miniconda3** and NOT Anaconda. After [installing Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).


<details>
  <summary markdown="span">**On Mac OS X**</summary>
  <img border="0" src="https://logos-download.com/wp-content/uploads/2020/06/Apple_Mac_OS_Logo-700x670.png" width="30" height="30">

  First, make sure you have Xcode and CommandLineTools installed and updated to latest version (in AppStore). If you have not already installed CommadLineTools, go to a terminal window and run:

  ```
  xcode-select --install
  ```

  First download the latest version of Miniconda3 and run it to install.

  ```
  curl -o Miniconda3-latest-MacOSX-x86_64.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
  sh Miniconda3-latest-MacOSX-x86_64.sh
  ```

  Follow the instructions on screen, scrolling down, pressing ENTER and replying `yes` when necessary. Install it in the default directory. Restart your terminal window to apply modifications. After restarting, you can type the command below to install Mamba:

  ```
  conda init
  conda install -n base -c conda-forge mamba
  ```

</details>


<details>
  <summary markdown="span">**On Ubuntu**</summary>
  <img border="0" src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR2rSSpKVBohI4AXgBaUjFVYqO73ou2l9AOXw&usqp=CAU" width="30" height="30">

  First download the latest version of Miniconda3 and run it to install.

  ```
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  sh Miniconda3-latest-Linux-x86_64.sh
  ```

  Follow the instructions on screen replying `yes` when necessary. Restart your terminal window to apply modifications. After restarting, you can type the command below to install Mamba:

  ```
  conda init
  conda install -n base -c conda-forge mamba
  ```

</details>


<details>
  <summary markdown="span">**On Windows 10**</summary>
  <img border="0" src="https://seeklogo.com/images/W/windows-10-icon-logo-5BC5C69712-seeklogo.com.png" width="30" height="30">

  Unfortunately, not all packages available on conda are compatible with windows machines. The good news is that Windows 10 offers native linux support via the Windows Subsystem for Linux (WSL2). This allows you to run linux/bash commands from within windows without the need of a virtual machine nor a dual-boot setup (i.e. having 2 operating systems). However, WSL does not offer a complete support for graphical interfaces (such as RStudio in our case), so we need additional steps to make that happen.

  1. On Windows 10, install the WSL if you don't have it. Follow the instructions here:
[https://docs.microsoft.com/en-us/windows/wsl/install-win10](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

  2. Once you have that installed, you can download and install MobaXterm (which is the enhanced terminal with graphical capacity):
[https://mobaxterm.mobatek.net](https://mobaxterm.mobatek.net)  
It is recommended that you INSTALL the program and not use the portable version.

  3. Inside MobaXterm, you will probably will see that your WSL is already listed on the left panel as an available connection. Just double-click it and you will be accessing it via MobaXterm. If by any chance you don't see it there, close MobaXterm and go to the WSL terminal, because probably the WSL is not allowing SSH connections. You can follow this [link](https://www.illuminiastudios.com/dev-diaries/ssh-on-windows-subsystem-for-linux/) for the instructions on how to do it. You need to complete until the step `Start or restart the SSH service`, while the further steps are optional, but might be useful.

  4. Inside MobaXterm, download Conda with the command:

  ```
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  ```

  5. Inside MobaXterm, type the commands below to install Conda. Follow the instructions for the installation there.

  ```
  cd ~/Downloads
  sh Miniconda3-latest-Linux-x86_64.sh
  ```

  6. Inside MobaXterm, Follow the instructions on screen replying `yes` when necessary. Restart your terminal window to apply modifications. After restarting, you can type the command below to install Mamba:

  ```
  conda init
  conda install -n base -c conda-forge mamba
  ```

  7. Inside MobaXterm, type the commands below to install the X-server graphical packages that will be used to launch RStudio.
[https://docs.anaconda.com/anaconda/install/linux/](https://docs.anaconda.com/anaconda/install/linux/)

  ```
  sudo apt-get update
  sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
  ```

  8. Close and open all application and Inside MobaXterm, you will probably will see that your WSL is already listed on the left panel as an available connection. Just double-click it and you will be accessing it via MobaXterm.

</details>


<details>
  <summary markdown="span">**On VirtualBox**</summary>
  <img border="0" src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Virtualbox_logo.png" width="30" height="30">

  If by any means you see that the installations are not working as it should on your computer, you can try to create a virtual machine to run UBUNTU and install everything there. But please keep this alternative as the last temporary resourse, as we recommend troubleshooting the installation o the up-mentioned methods.

  1. Download and install on your machine VIRTUALBOX
[https://www.virtualbox.org](https://www.virtualbox.org)

  2. Download the ISO disk of UBUNTU
[https://ubuntu.com/download/desktop](https://ubuntu.com/download/desktop)

  3. On VIRTUALBOX, click on `Settings` (yellow engine) > `General` > `Advanced` and make sure that both settings **Shared Clipboard** and **Drag'n'Drop** are set to `Bidirectional`.

  4. Completely close VIRTUALBOX and start it again to apply changes.

  5. On VIRTUALBOX, create a machine called Ubuntu and add the image above
  - set the memory to the maximum allowed in the GREEN bar
  - set the hard disk to be dynamic allocated
  - all other things can be default

  6. Proceed with the Ubuntu installation as recommended. You can set to do "Minimal Installation" and deactivate to get updates during installation.

  7. Inside Ubuntu, open TERMINAL and type the commands below to install the X-server graphical packages that will be used to launch RStudio.
[https://docs.anaconda.com/anaconda/install/linux/](https://docs.anaconda.com/anaconda/install/linux/)

  ```
  sudo apt-get update
  sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
  ```

  8. Inside UBUNTU, Download conda:

  ```
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  ```

  9. Inside UBUNTU, open the TERMINAL and type the commands below. Follow the instructions for the installation there.

  ```
  cd ~/Downloads
  sh Miniconda3-latest-Linux-x86_64.sh
  ```

  10. Close Terminal to apply the CONDA updates.

</details>

<br/>



##### 2. Install git clone the repository
Throughout the course we'll be using scripts and environments found in our github repository. After installing mamba, install git and clone the repository:
```
mamba install -c anaconda git #install
mkdir ~/Desktop/course
cd ~/Desktop/course
git clone git@github.com:NBISweden/workshop_omics_integration.git .
```

All environments are contained inside the folder `/environments/`


##### 3. Create and activate the environment
For each day you will have to create a different environment:
**Day 1**  

```
#Linux
mamba env create -n envday1 -f environments/env-ml_linux.yaml

#MacOSX
mamba env create -n envday1 -f environments/env-ml.yaml
```

**Day 2**  

```
#Linux
mamba env create -n envday2 -f environments/env-ml_day2_linux.yaml

#MacOSX
mamba env create -n envday2 -f environments/env-ml_day2.yaml
```

**Days 3-5**   

```
#Linux
mamba env create -n envdays35 -f environments/env-merged_nets_linux.yaml

#MacOSX
mamba env create -n envdays35 -f environments/env-merged_nets.yaml
```

Activate the environments with `mamba activate [environment name]`. For instance  

```
mamba activate envday1
```

#### 4. Launch RStudio or Jupyter
Depending on the exercise, you'll have to run scripts in either RStudio or Jupyter. You can launch these with  

```
rstudio &
```

or

```
jupyter-notebook &
```

#### 5. Deactivate the environment after running your analyses
After you've ran all your analyses, you can deactivate the environment by typing:  

```
mamba deactivate
```



[2]: https://datacarpentry.org/genomics-r-intro/
[3]: https://datacarpentry.org/python-ecology-lesson/
[4]: https://nbisweden.github.io/workshop-python/ht19/
[5]: reading_materials.md
[6]: https://nbisweden.github.io/workshop-r/