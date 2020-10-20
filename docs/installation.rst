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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The code for running the Bangkok liveability analyses is hosted in a Git repository.  At the time of writing (16 October 2020) this is hosted in a private Bitbucket online repository, and so for now access must be granted manually. The code is provided under an MIT licence however, and will be made officially public via GitHub in tandem with publication of project methods.

To retrieve the repository, in a command window in the parent directory to where you would like the project to be located type:

.. code-block:: text
   :linenos:

   git clone https://carlhiggs@bitbucket.org/carlhiggs/ind_bangkok.git 

This should create the project directory 'ind_bangkok' along with a series of subfolders, including the folders 'data' (in which the data retrieved in the following step should be stored), and 'process' which contains the code required to run the project analyses.

Initialise project spatial database
-----------------------------------

The project database is stored using a seperate Docker container which is used to run the SQL database software PostgreSQL with the spatial extension PostGIS.  This is the immediate location where indicators and spatial data are stored once processed.  Mapping programs like QGIS may connect to this database in order to map indicators, once processed. 

The database is set up by running the command `initialise_database` from the the Windows command line in the project's parent directory (the "ind_bangkok" folder).  This will most likely only need to be done once, at project commencement, after which the database docker image should persist locally when Docker is running.

This launches the `initialise_database.bat` batch file, which is a text document containing code which directs the computer to 

 - retrieve the `cityseer/postgis` Docker image
 - create a database container for running Postgis called `pg_spatial` with user 'hlc' and password 'huilhuil!42'.

The default username and password may be changed in the batch file before running using a text editor to edit it; however, if these are modified they should also be changed in the project configuration parameters, as described later in the setup process.

Launch the spatial analysis processing environment
--------------------------------------------------

With the software pre-requesites installed and running, and the code repository constructed in a project folder, the curated open source software framework for calculation of spatial indicators (the `ind_bangkok` "container") may be installed by typing and entering `ind_bangkok` from the project parent directory (the "ind_bangkok" folder) at the Windows command prompt.

This launches the `ind_bangkok.bat` batch file, which is a text document containing code which directs the computer to

 - pull the latest version of the project code
 - retrieve the latest version of the `carlhiggs/ind_bangkok` docker image, if not presently installed
 - launch the `ind_bangkok` docker container, which provides a Unix command prompt for running the project software

If you close the terminal window in which the the spatial analysis processing container is running, it remains active in the background as long as the Docker service is running (e.g. until the computer is shut down).  To return to the command prompt from the `ind_bangkok` container, but still leave it running, you can also press Ctrl+p+q .  To return to the container from the prompt you can enter `docker attach ind_bangkok`.  Finally, to stop the container altogether, you can enter `docker stop ind_bangkok`.

Data requirements
~~~~~~~~~~~~~~~~~

`The collated input data <https://cloudstor.aarnet.edu.au/plus/s/gMMftKTJahNMX2Q/download>`_ used to create the baseline suite of Bangkok liveability indicators has been uploaded to a private CloudStor data repository for the moment.  This contains international and Thai sourced data, including data provided directly by the Bangkok Metropolitan Administration.

At the time of writing, the data may be accessed from the provided link using the access word `BangkokLiveability@2020`

Once downloaded, the contents of the zipped folder should be extracted and located within the projects 'data' directory.

.. _Windows subsystem for linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Ubuntu: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0
.. _Git: https://git-scm.com/
.. _Docker: https://www.docker.com/products/docker-desktop
.. _PostgreSQL with PostGIS and PgRouting: https://hub.docker.com/r/cityseer/postgis/

Additional tips
~~~~~~~~~~~~~~~

 - Try to allocate at least 8Gb (> 8000mb) memory in the advanced settings of Docker Desktop (more than 2Gb, the default, is required; 8Gb works)

 - If you find the database has stopped (a warning will be raised when running the scripts that the database doesn't exist), try "docker start pg_spatial" to re-start it if you re-run 'initialise_database.bat', this will mean you will have to re-run code to re-create and re-build the database --- so that is probably something you only want to do at project commencement

 - Occasionally you might find that the Docker Desktop application doesn't run successfully the first time you launch it; if so, try restarting the application, and it will likely resolve the issue.
