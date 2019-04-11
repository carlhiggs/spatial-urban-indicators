# Bangkok Liveability #

This repository contains the processes used in the Bangkok Liveability indicators project, 2019.

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
docker pull mdillon/postgis
```


* run postgis server container

```
docker run --name=postgis -d -e POSTGRES_USER=postgres -e POSTGRES_PASS=huilhuil!42 -e POSTGRES_DBNAME=ind_bangkok  -p 127.0.0.1:5433:5432 -e pg_data:/var/lib/postgresql mdillon/postgis
```

* run analysis environment from Bash

```
docker run --rm -it -u 0 --name ind_bangkok --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 
```

### Contact ###

carl.higgs@rmit.edu.au
