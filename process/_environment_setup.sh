# set up analysis environment container, based on OSMnx
cd ./process/docker
docker build -t ind_bangkok .
cd ../..

# set up spatial database container, based on Postgis
#docker pull mdillon/postgis

# run postgis server container
# docker run --name=postgis -d -e POSTGRES_USER=postgres -e POSTGRES_PASS=huilhuil!42 -e POSTGRES_DBNAME=ind_bangkok  -p 127.0.0.1:5433:5432 -e pg_data:/var/lib/postgresql mdillon/postgis

# postgresql with postgis and pgrouting
docker pull cityseer/postgis
# run database
docker run --name=pg_spatial -d -e PG_USER=hlc -e PG_PASSWORD=huilhuil!42 -e DB_NAME=ind_bangkok -p 127.0.0.1:5433:5432  --restart=unless-stopped --volume=/var/lib/pg_spatial:/postgresql/11/main cityseer/postgis:latest
# connect to database
psql -p 5433 -h host.docker.internal -U postgres
# database back up
pg_dump postgresql://postgres:'huilhuil!42'@host.docker.internal:5433/li_bangkok_2018 > li_bangkok_2018.sql

# If you get an error like 'driver failed programming external connectivity on endpoint pg_spatial'
# try restarting the docker service (on Windows, right click the Docker icon and select 'restart')
# as per this post: https://stackoverflow.com/questions/49693353/error-response-from-daemon-driver-failed-programming-external-connectivity-on-e?rq=1
# This can occur if the Docker is not fully shutdown when the computer is turned off.
# As per this post: https://stackoverflow.com/questions/44414130/docker-on-windows-10-driver-failed-programming-external-connectivity-on-endpoin
# I had to do more:
##Simply restaring Docker didn't fix the problem for me on Windows 10.
##
##In my case, I resolved the problem with the exact steps below:
##
##1) Close "Docker Desktop"
##
##2) Run the commands below:
##
##net stop com.docker.service
##net start com.docker.service
##3) Launch "Docker Desktop" again

# run analysis environment as Bash command prompt (as root)
docker run --rm -it -u 0 --name ind_bangkok --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 

# run analysis environment as Bash command prompt (as jovyan; ie. the default Jupyter notebook user)
docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 

# run analysis environment as Jupyter Lab (note - not yet conversing properly with database)
docker run --rm -it --name ind_bangkok -p 8888:8888  -p 5433:5433 -v %cd%:/home/jovyan/work ind_bangkok

