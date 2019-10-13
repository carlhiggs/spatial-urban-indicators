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

With these pre-requisites met, we can open up the windows command prompt (cmd.exe) or PowerShell to the ind_bangkok project directory and set up the computational environment, set up the project database, and commence analysis.

Set up the computational environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the project directory, enter the following command:

.. code-block:: text
   
   _compile_docker.bat

The above step sets up an isolated 'container' or computational environment with software for spatial analysis and visualisation.  This will take some time.  This container is called 'ind_bangkok'.

Set up the project database
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A seperate Docker container is set up for running the project database and associate software (`PostgreSQL with PostGIS and PgRouting`_).  This is the immediate location where indicators and spatial data are stored once processed.  Mapping programs like QGIS may connect to this database in order to map indicators, once processed.

To set up the project database, enter the following command: 

.. code-block:: text
   
   docker pull cityseer/postgis

.. _Windows subsystem for linux: https://docs.microsoft.com/en-us/windows/wsl/install-win10
.. _Ubuntu: https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#0
.. _Docker: https://www.docker.com/products/docker-desktop
.. _PostgreSQL with PostGIS and PgRouting: https://hub.docker.com/r/cityseer/postgis/):