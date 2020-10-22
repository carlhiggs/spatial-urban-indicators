# Bangkok Liveability #

This repository contains the processes used to create preliminary dataset resources in the Bangkok liveability (2019) indicators project.

### How do I get set up? ###

Please see the seperately available technical documentation pdf and webinar for full directions.

* install [Git](https://git-scm.com/downloads), [Docker](https://www.docker.com/products/docker-desktop) , and if required Windows Sub-system for Linux and Ubuntu

* git clone https://carlhiggs@bitbucket.org/carlhiggs/ind_bangkok.git


#### setup and run postgis database server container (at project commencement; else run 'docker start pg_spatial' if container has stopped) ####

The user can either run the `initialise_database` batch script from the project directory, or,

```
docker pull cityseer/postgis
docker run --name=pg_spatial -d -e PG_USER=hlc -e PG_PASSWORD=password -e DB_NAME=ind_bangkok -p 127.0.0.1:5433:5432 --restart=unless-stopped --volume=/var/lib/pg_spatial:/postgresql/11/main cityseer/postgis:latest
```

#### setup and run analysis environment ####

The user can either run the `ind_bangkok` batch script from the project directory, or,

```
docker pull carlhiggs/ind_bangkok
docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 
```

### To process ###

 - Collate project data resources and define these as well as study region and project parameters in the project set up file  _project_configuration.xlsx
 - The initial set up scripts in the `process` folder are run sequentially using the syntax `python script.py study_region` (if study region is not specified, the default is 'bangkok')
 - Subsequently, scripts to create indicators,plots or documentation may be run as required using the same syntax

### Contact ###

carl.higgs@rmit.edu.au
