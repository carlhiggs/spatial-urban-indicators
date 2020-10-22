# Bangkok Liveability #

This repository contains the processes used to create preliminary dataset resources in the  Bangkok liveability (2019) indicators project. It is based on scripts developed from the HLC national liveability indicators (2017-19) project.

### How do I get set up? ###

Please see the technical documentation pdf and webinar for full directions.

* install [Git](https://git-scm.com/downloads) and [Docker](https://www.docker.com/products/docker-desktop)

* git clone https://carlhiggs@bitbucket.org/carlhiggs/ind_bangkok.git

* set up analysis environment container, based on OSMnx

```
dock pull carlhiggs/ind_bangkok
```

* set up spatial database container, based on Postgis

```
docker pull cityseer/postgis
```


* run postgis server container

The user can either run the `initialise_database` batch script from the project directory, or,

```
docker run --name=pg_spatial -d -e PG_USER=hlc -e PG_PASSWORD=password -e DB_NAME=ind_bangkok -p 127.0.0.1:5433:5432 --restart=unless-stopped --volume=/var/lib/pg_spatial:/postgresql/11/main cityseer/postgis:latest
```

* run analysis environment from Bash

The user can either run the `ind_bangkok` batch script from the project directory, or,

```
docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 
```

### To process ###

The scripts are run sequentially, after collating project data resources and defining these as well as study region and project parameters in the project set up file  _project_configuration.xlsx.

### Contact ###

carl.higgs@rmit.edu.au
