cd..
docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g --net=host -v %cd%:/home/jovyan/work/ ind_bangkok /bin/bash 
