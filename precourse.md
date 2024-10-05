---
layout: default
title:  Pre-course
---

#### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Programming with R and Python {#programming-with-r-and-python}
***

This workshop will comprise both lectures and hands-on exercises. While you will be able to follow all exercises from the html files, we recommend that you prepare by 

1. [Familiarizing yourself with basic R and Python](#programming-with-r-and-python)
2. [Installing the containers](#-docker-instructions).

If you are interested you can go through the [additional reading materials][5].

#### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Programming with R and Python
***

The course will be taught using both R and Python depending on the tools available. While you will be able to follow all lectures and exercises conceptually, it is helpful if you are familiar with basic usage of both programming languages:
- [R (part_1)](https://swcarpentry.github.io/r-novice-inflammation/)
- [R (part_2)](http://swcarpentry.github.io/r-novice-gapminder/)
- [Python (part_1)](https://swcarpentry.github.io/python-novice-inflammation/)
- [Python (part_2)](http://swcarpentry.github.io/python-novice-gapminder/)

You should also be familiar with basic command line input (`mkdir`, `cd`, `ls`, `cp`, `mv`).

#### <img border="0" src="https://www.svgrepo.com/show/303231/docker-logo.svg" width="25" height="25"> Docker instructions
***

To reproduce all analyses you will need to:
- [Install Docker](https://docs.docker.com/get-docker/);
- [Download the latest Github repository](#download-the-github-repository);
- [Create the containers](#create-the-containers);
- [Launch rstudio or jupyter](#launch-rstudio-or-jupyter);
- [Stop the containers](#stop-the-containers)

##### Download the Github repository
Download and unzip the github repository [from here](https://github.com/NBISweden/workshop_omics_integration/) or run:  
```
wget -qO- https://github.com/NBISweden/workshop_omics_integration/archive/refs/heads/main.zip | bsdtar -xvf-
mv workshop_omics_integration-main workshop_omics_integration
``` 

Note that you download it manually you should name the unziped folder as `workshop_omics_integration`. All the subsequent commands should be run in the parent of this directory.


##### Create the containers

At this point you need to create the two containers for all Rstudio or Jupyter notebooks. In a directory containing the unzip folder `workshop_omics_integration/`, create the containers by either:

<details>
  <summary markdown="span">**> Download image from Dockerhub** (recommended)</summary>

  Pull and start the images. Remember to replace `<yourpassword>` with your password, and `/path/to/your/` with the path to your directory. If you want to use the current working directory, use `$(pwd)` in MacOS/Linux and `$(PWD}` in Windows powershell.

  ```
  ########### Rstudio image ###########
  # Your user is 'rstudio' (without the quotes)
  sudo docker run -d --rm -p 8787:8787 \
    -e PASSWORD=<yourpassword> \ 
    -v /path/to/your/workshop_omics_integration:/home/rstudio/workshop_omics_integration/ \
    ruibenfeitas/rstudio:30_08_2021
  
  ########### Jupyter image ###########
  # Your user is 'jovyan' (without the quotes)
  sudo docker run -d --rm -p 8888:8888 \
    -e JUPYTER_TOKEN=<yourpassword> \
    -v /path/to/your/workshop_omics_integration/:/home/jovyan/workshop_omics_integration/ \
    ruibenfeitas/jupyter:30_08_2021
  ```
</details>


<details>
  <summary markdown="span">**> Download the dockerfiles from github**</summary>

On github you will find the dockerfiles necessary from the github repository, under `workshop_omics_integration/docker/` (you need the files `Dockerfile_jupyter`, `Dockerfile_rstudio`, `docker-compose.yml` and `environment_jupyter`). [Install docker compose](https://docs.docker.com/compose/install/) and then:

```
## copy the dockerfiles found in the downloaded directory to the directory above
cp -r /path/to/your/workshop_omics_integration/docker/* /path/to/your/
```

Build and start the containers
```
docker-compose up -d --build
```
</details>





##### Launch RStudio or Jupyter

Ensure you have followed all the instructions above and that your containers are running. If you have followed the instructions from the recommended solution you can simply access either RStudio or Jupyter from your browser with:
- `localhost:8888` to launch jupyter
- `localhost:8787` to launch rstudio

All notebooks are found within the folder `workshop_omics_integration/`. If you want to verify that your containers are running use `docker ps`.

##### Stop the containers
To stop the containers write `docker stop [container name]`.


[2]: https://datacarpentry.org/genomics-r-intro/
[3]: https://datacarpentry.org/python-ecology-lesson/
[4]: https://nbisweden.github.io/workshop-python/ht19/
[5]: reading_materials.md
[6]: https://nbisweden.github.io/workshop-r/
