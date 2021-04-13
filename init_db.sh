docker pull cityseer/postgis
docker run --name=pg_spatial -d -e PG_USER=sui -e PG_PASSWORD=sui -e DB_NAME=sui -p 127.0.0.1:5433:5432 --restart=unless-stopped --volume=/var/lib/pg_spatial:/postgresql/11/main cityseer/postgis:latest
