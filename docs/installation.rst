Installation
============

To install and run the tools required to calculate the Bangkok liveability indicators, we must ensure the project dependencies are met.  This involves the installation of several open source software packages.  

`to do: refine these installation directions`

On a computer running Windows 10, we first set up `Windows subsystem for linux`_ by running the following in PowerShell in Administrator mode:

.. code-block:: text
   :linenos:

   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux

Now, we install `Ubuntu`_ as per the instructions at this link.  Ubuntu provides us with a command line operating system for some of the open source software we will be using.

Now, we install `Docker`_, a tool which helps to install a raft of other required software, all at once while helping to ensure compatibility between different software versions.

(now there is the tricky bit to do with project directory and data structure... A git repository sorts out the folder structure, but how about the data?  Should we host it somewhere? Git LFS?  We'll gloss over this for now)

With these pre-requisites met, we can open up cmd.exe or PowerShell to the ind_bangkok project directory and at the command line type the following to change directory to the Docker set up script, run this and return to the main script directory:

.. code-block:: text
   :linenos: 
   
   cd ./process/docker
   docker build -t ind_bangkok .
   cd ../..

The above step which sets up an isolated 'container' or computational environment with software for spatial analysis and visualisation will take some time.  This container is called 'ind_bangkok'. Once successfully complete, we can set up a seperate spatial database container (`PostgreSQL with PostGIS and PgRouting`_):

.. code-block:: text
   
   docker pull cityseer/postgis
   
To initialise the running of the spatial database in the background on your system you can execute the following:

.. code-block:: text

   docker run --name=pg_spatial -d -e PG_USER=hlc -e PG_PASSWORD=huilhuil!42 -e DB_NAME=ind_bangkok -p 127.0.0.1:5433:5432  --restart=unless-stopped --volume=/var/lib/pg_spatial:/postgresql/11/main cityseer/postgis:latest

We are now ready to commence analysis!  To launch the ind_bangkok computational environment, type `ind_bangkok` in the ind_bangkok project's root directory.  Then type `cd process` to move into the script folder.

Other operations
~~~~~~~~~~~~~~~~

# connect to database
psql -p 5433 -h host.docker.internal -U postgres
# database back up
pg_dump postgresql://postgres:'huilhuil!42'@host.docker.internal:5433/li_bangkok_2018 > li_bangkok_2018.sql


# run analysis environment as Bash command prompt (as root)
docker run --rm -it -u 0 --name ind_bangkok --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 

# run analysis environment as Bash command prompt (as jovyan; ie. the default Jupyter notebook user)
docker run --rm -it -u jovyan --name ind_bangkok --shm-size 2g --net=host -v %cd%:/home/jovyan/work ind_bangkok /bin/bash 

# run analysis environment as Jupyter Lab (note - not yet conversing properly with database)
docker run --rm -it --name ind_bangkok -p 8888:8888  -p 5433:5433 -v %cd%:/home/jovyan/work ind_bangkok

Resources
~~~~~~~~~
.. _Windows subsystem for linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Ubuntu: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0
.. _Docker: https://www.docker.com/products/docker-desktop
.. _PostgreSQL with PostGIS and PgRouting: https://hub.docker.com/r/cityseer/postgis/):