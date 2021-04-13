cd../..
docker run --rm -it -u jovyan --name sui --shm-size 2g --net=host -v %cd%:/home/jovyan/work sui /bin/bash 
