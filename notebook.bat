docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g -p 8888:8888  -p 5433:5433 -v %cd%:/home/jovyan/work/ ind_bangkok /bin/bash