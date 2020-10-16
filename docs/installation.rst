Installation
============

To install and run the software framework for calculation and output of the Bangkok liveability indicators in a variety of formats, the user must first ensure that the following software, code, and data requirements are met.  

Software requirements
~~~~~~~~~~~~~~~~~~~~~

Windows subsystem for linux (WSL)
---------------------------------

On a computer running Windows 10, we first set up `Windows subsystem for linux`_ (WSL) by running the following in PowerShell in Administrator mode:

.. code-block:: text
   :linenos:

   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

Optionally, the user may install the newer version of WSL2 by following the additional directions provided at the link above.  Once ready, the computer should be restarted.

Ubuntu
------

`Ubuntu`_ may be installed for Windows as per the instructions at this link.  Ubuntu provides a command line operating system for installing and running the open source software suite curated for this project.

Git
---

`Git`_ is software used for distribution and version tracking of software projects.  Please download and install this software for your platform from the provided link.  This is required in order to retrieve the Bangkok liveability code.

Docker
------

`Docker`_ is a tool which facilitates installation of a raft of other required software, all at once while helping to ensure compatibility between different software versions.  Follow the provided link to download the version of Docker Desktop appropriate for your platform.

When ever the project is to be run, Docker Desktop must be running as a background service on the user's computer.  If Docker is running, there should be the icon of a whale in the user's taskbar on Windows 10; if the cursor is hovered over this, it should say, 'Docker Desktop is running'.

Spatial indicator framework for Healthy, Liveable Bangkok
---------------------------------------------------------

With the above software successfully installed and running, the curated open source software framework for calculation of spatial indicators may be installed by entering the following from a Windows command prompt:

.. code-block:: text
   :linenos:

   docker pull carlhiggs/ind_bangkok

The above command is also included in the project analysis code, the installation of which is described in the following section.

Spatial database
----------------

The project database is stored using a seperate Docker container which is used to run the SQL database software PostgreSQL with the spatial extension PostGIS.  This is the immediate location where indicators and spatial data are stored once processed.  Mapping programs like QGIS may connect to this database in order to map indicators, once processed. 

The bangkok database is set up by running the following from the command line:

.. code-block:: text
   :linenos:

   docker pull cityseer/postgis
   docker run --name=pg_spatial -d -e PG_USER=hlc -e PG_PASSWORD=huilhuil!42 -e DB_NAME=ind_bangkok -p 127.0.0.1:5433:5432 --restart=unless-stopped --volume=/var/lib/pg_spatial:/postgresql/11/main cityseer/postgis:latest

The password in the above command is `huilhuil!42` as this is the default specified in the project configuration.  It may be changed, but if so, should also be changed in the project configuration parameters, as described later in the setup process.

Code requirements
~~~~~~~~~~~~~~~~~

The code for running the Bangkok liveability analyses is hosted in a Git repository.  At the time of writing (16 October 2020) this is hosted in a private Bitbucket online repository, and so for now access must be granted manually. The code is provided under an MIT licence however, and will be made officially public via GitHub in tandem with publication of project methods.

To retrieve the repository, in a command window in the parent directory to where you would like the project to be located type:

.. code-block:: text
   :linenos:

   git clone https://carlhiggs@bitbucket.org/carlhiggs/ind_bangkok.git 

This should create the project directory 'ind_bangkok' along with a series of subfolders, including the folders 'data' (in which the data retrieved in the following step should be stored), and 'process' which contains the code required to run the project analyses.

Data requirements
~~~~~~~~~~~~~~~~~

`The collated input data <https://cloudstor.aarnet.edu.au/plus/s/gMMftKTJahNMX2Q>`_ used to create the baseline suite of Bangkok liveability indicators has been uploaded to a private CloudStor data repository for the moment.  This contains international and Thai sourced data, including data provided directly by the Bangkok Metropolitan Administration.

At the time of writing, the data may be accessed from the provided link using the access word: BangkokLiveability@2020

Once downloaded, the contents of the zipped folder should be extracted and located within the projects 'data' directory.

.. _Windows subsystem for linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Ubuntu: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0
.. _Git: https://git-scm.com/
.. _Docker: https://www.docker.com/products/docker-desktop
.. _PostgreSQL with PostGIS and PgRouting: https://hub.docker.com/r/cityseer/postgis/