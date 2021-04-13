docker pull carlhiggs/ind_bangkok
git pull
docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g --net=host -v %cd%:/home/jovyan/work carlhiggs/ind_bangkok /bin/bash 
