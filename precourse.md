---
layout: default
title:  Pre-course
---

#### <img border="0" src="https://www.svgrepo.com/show/529862/server-path.svg" width="15" height="15"> Registration on SciLifeLab Serve
***

In order to be able to access the lab notebooks for this course you need to have access to [SciLifeLab Serve](https://serve.scilifelab.se). 

Please register with your university email address. In the registration form there is a field called “Do you require support?”, in here please write that you are registering to take part in the course OMICSINT_H24. Do not forget to also confirm your e-mail address by clicking on a link in the activation email. This needs to be done before Friday October 11 so that the SciLifeLab Serve admins can set up your account in the way that is required by the course.

#### <img border="0" src="https://www.svgrepo.com/show/26916/book.svg" width="15" height="15"> Preparation for the tutorial
***

This workshop will comprise both lectures and hands-on exercises. While you will be able to follow all exercises from the html files, we recommend that you prepare by 

1. [Familiarizing yourself with basic R and Python](#programming-with-r-and-python)
2. [Installing the containers](#docker-instructions).

If you are interested you can go through the [additional reading materials][5].

#### <img border="0" src="https://www.svgrepo.com/show/7421/computer.svg" width="25" height="25"> Programming with R and Python {#programming-with-r-and-python}
***

The course will be taught using both R and Python depending on the tools available. While you will be able to follow all lectures and exercises conceptually, it is helpful if you are familiar with basic usage of both programming languages:

- [R (part_1)](https://swcarpentry.github.io/r-novice-inflammation/)
- [R (part_2)](http://swcarpentry.github.io/r-novice-gapminder/)
- [Python (part_1)](https://swcarpentry.github.io/python-novice-inflammation/)
- [Python (part_2)](http://swcarpentry.github.io/python-novice-gapminder/)

You should also be familiar with basic command line input (`mkdir`, `cd`, `ls`, `cp`, `mv`).

#### <img border="0" src="https://www.svgrepo.com/show/303231/docker-logo.svg" width="25" height="25"> Docker instructions {#docker-instructions}
***

We have currently ran different tests and evaluations to make sure SciLifeLab Serve is roboust and functional during the course time. However, as a back up plan for running the notebooks in case that SciLifeLab Serve service was lagging, we have prepared docker images for different labs with all the necessary software installed. You can follow the instructions below to install the docker and run the notebooks locally.

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (optional)
- [Clone the Github repository for the course](https://github.com/NBISweden/workshop_omics_integration/tree/OMICSINT_H24) (optional)

##### Pull docker images

At this point you need to create the two containers for all Rstudio or Jupyter notebooks. In a directory containing the unzip folder `workshop_omics_integration/`, create the containers by either:

<details>
  <summary markdown="span">**> Download image from Dockerhub** </summary>

  Select the approprtiate lab from [dockerhub repo](https://hub.docker.com/repository/docker/rasoolsnbis/omicsint_h24/tags), pull and run the images.

  ```
  ########### For example for GSA and UMAP labs ###########
  # cd to your desired directory
  docker pull rasoolsnbis/omicsint_h24:session_gsa_amd_v.h24.a1ae0fc
  docker pull rasoolsnbis/omicsint_h24:session_ml_umap_data_integration_amd_v.h24.b327560adfd4536832cbc2fe7451468ee55b6188

  # for Jupyter lab use the following command
  docker run --rm --platform=linux/amd64 -d -p 8888:8888/tcp rasoolsnbis/omicsint_h24:session_ml_umap_data_integration_amd_v.h24.b327560adfd4536832cbc2fe7451468ee55b6188

  # for Rstudio lab use the following command
  docker run --rm --platform=linux/amd64 -d -p 8787:8787/tcp rasoolsnbis/omicsint_h24:session_gsa_amd_v.h24.a1ae0fc
  ```
</details>

##### Launch RStudio or Jupyter

Ensure you have followed all the instructions above and that your containers are running. If you have followed the instructions, you can simply access either RStudio or Jupyter from your browser with:
- `localhost:8888` to launch jupyter
- `localhost:8787` to launch rstudio

If you want to verify that your containers are running use `docker ps`.

##### Stop the containers
To stop the containers write `docker stop [container name]`.


[2]: https://datacarpentry.org/genomics-r-intro/
[3]: https://datacarpentry.org/python-ecology-lesson/
[4]: https://nbisweden.github.io/workshop-python/ht19/
[5]: reading_materials.html
[6]: https://nbisweden.github.io/workshop-r/

[Back to Homepage](https://nbisweden.github.io/workshop_omics_integration/)
