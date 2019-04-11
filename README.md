# Global liveability indicators project#

This (proposed) repository contains documentation and processes used in the global liveability indicators ('Lancet series') project, 2019.

### How do I get set up? ###

* install [Git](https://git-scm.com/downloads) and [Docker](https://www.docker.com/products/docker-desktop)

* git clone https://carlhiggs@bitbucket.org/carlhiggs/ind_global.git

* set up analysis environment container, based on OSMnx

```
cd ./process/docker
docker build -t ind_global .
cd ../..
```

* set up spatial database container, based on Postgis

```
docker pull mdillon/postgis
```


* run postgis server container

```
docker run --name=postgis -d -e POSTGRES_USER=postgres -e POSTGRES_PASS=password -e POSTGRES_DBNAME=ind_global  -p 127.0.0.1:5433:5432 -e pg_data:/var/lib/postgresql mdillon/postgis
```

* run analysis environment from Bash

```
docker run --rm -it -u 0 --name ind_global --net=host -v %cd%:/home/jovyan/work ind_global /bin/bash 
```

### Contact ###

carl.higgs@rmit.edu.au

liu.shiqi@husky.neu.edu

g.boeing@northeastern.edu

