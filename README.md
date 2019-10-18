# Bangkok Liveability #

This repository contains the processes used to create preliminary dataset resources in the  Bangkok liveability (2019) indicators project. It is based on scripts developed from the HLC national liveability indicators (2017-19) project.

### How do I get set up? ###

* install [Git](https://git-scm.com/downloads) and [Docker](https://www.docker.com/products/docker-desktop)

* git clone https://carlhiggs@bitbucket.org/carlhiggs/ind_bangkok.git

* set up analysis environment container, based on OSMnx

```
cd ./process/docker
docker build -t ind_bangkok .
cd ../..
```

* set up spatial database container, based on Postgis

```
docker pull cityseer/postgis
```


* run postgis server container

```
docker run --name=pg_spatial -d -e PG_USER=hlc -e PG_PASSWORD=password -e DB_NAME=ind_bangkok -p 127.0.0.1:5433:5432 --restart=unless-stopped --volume=/var/lib/pg_spatial:/postgresql/11/main cityseer/postgis:latest
```

* run analysis environment from Bash

```
docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 
```

### To process ###

The scripts are run sequentially, after collating project data resources and defining these as well as study region and project parameters in the project set up file  _project_configuration.xlsx.

00_create_database.py
01_create_study_region.py
02_create_osm_resources.py
03_create_network_resources.py
04_create_sample_points.py
05_compile_destinations.py
06_open_space_areas_setup.py

### Contact ###

carl.higgs@rmit.edu.au
