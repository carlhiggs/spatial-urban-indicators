# Spatial Urban Indicators #

A generalised framework for calculation, management and export of spatial indicators for urban environments.

This repository contains the code and project structure for using the Spatial Urban Indicators (sui) framework to calculate, manage and export spatial indicators for diverse urban environments using open or custom data sources.

### How do I get set up? ###

* install [Git](https://git-scm.com/downloads), [Windows Sub-system for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) and [Ubuntu](https://ubuntu.com/tutorials/ubuntu-on-windows#1-overview) (if required), and [Docker](https://www.docker.com/products/docker-desktop).

* run `git clone https://carlhiggs@bitbucket.org/carlhiggs/spatial-urban-indicators.git` to retrieve this repository, including project directory folder structure and code.

#### setup and run postgis database server container (at project commencement; else run 'docker start pg_spatial' if container has stopped) ####

The user can either run the `init_db` shell script from the project directory.

#### setup and run analysis environment ####

Run the `sui` shell script from the project directory.

### To process ###

 - Collate project data resources and define these as well as study region and project parameters in the project set up file  _project_configuration.xlsx
 - The initial set up scripts in the `process` folder are run sequentially using the syntax `python script.py study_region` (if study region is not specified, the default is 'bangkok')
 - Subsequently, scripts to create indicators, plots or documentation may be run as required using the same syntax

### Contact ###

carl.higgs@rmit.edu.au
