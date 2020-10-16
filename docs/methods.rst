Methods
=======

With the project requirements met, software installed, code and project directories retrieved, input data downloaded, and project configured with a study region and indicators defined, we are now ready to commence analysis!  

To launch the ind_bangkok computational environment on a Windows 10 computer, type `ind_bangkok` at the command line in the ind_bangkok project's root directory.  This will launch into the Spatial indicator framework software environment, at a unix shell (command line) prompt. 

Once the container has loaded, type `cd process` to move into the process folder. This contains text files containing code which are used to complete various tasks.

There are two kinds of processing files, those which relate to setting up the resources required in order to calculate indicators and which are numbered sequentially, and those which draw upon the resources previously set up in order to calculate indicators or output their associated documentation and which have an underscore prefix.

Setting up resources
~~~~~~~~~~~~~~~~~~~~

These scripts are intended to be run sequentially.  However, if accessibility indicators are not required it may be sufficient to just run the first three scripts to establish the database, study region boundaries, and population statistics which linkage or raster indicators may draw upon.

The scripts are run by typing `python <script> <study region>`; for example

.. code-block:: text

   python 00_create_database.py bangkok
   
However, as Bangkok is the default study region, its name may be omitted and the program will assume that this is the study region being referred to and configure the code accordingly.

**00\_create\_database.py**

Initialises a PostgreSQL database and related settings for creation of liveability indicators for a particular study region.

**01\_create\_study\_region.py**

Establishes study region boundaries and associated population resources, as defined in the `Parameters` and `Resources` worksheets in `\_project\_configuration.xlsx` for this study region.

**02\_create\_population.py**

This imports area level population estimates (as defined in the `Parameters` and `Resources` worksheets in `\_project\_configuration.xlsx`) into the project database and produces basic population map file outputs which will be included in the final report documentation.


Optional resource setup for accessibility analyses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**03\_create\_osm\_resources.py**


Collate OSM resources for specified study region, as defined in the `Parameters` and `Resources` worksheets in `\_project\_configuration.xlsx`.

**04\_create\_network\_resources.py**

Derive a walkable network for pedestrians derived from OpenStreetMap data using OSMnx 

**05\_open\_space\_areas\_setup.py**

Prepare a dataset of areas of open space (public parks and squares), derived from OpenStreetMap data, as configured in the `osm\_open\_space` worksheet in the `\_project\_configuration.xlsx` file.

**06\_create\_sample\_points.py**

Create sample points at regular intervals along the pedestrian street network for use in sampling accessibility to destinations.

**07\_compile\_destinations.py**

Compile a schema of destination features either using custom data, or OpenStreetMap.  Custom destination data sources are defined in the `Resources` worksheet in `\_project\_configuration.xlsx` with `purpose` of "destinations" and `type` equal to the `variable\_name` of the destination's corresponding accessibility indicator they are to be used for measuring.  OpenStreetMap destinations are defined in the `osm\_destinations` worksheet in `\_project\_configuration.xlsx` file.

**08\_accessibility\_analysis.py**

Undertake accessibility analysis within threshold distance for defined destination access indicators.  The threshold distance is defined using the `resolution` parameter in the `Resources` worksheet in the `\_project\_configuration.xlsx` file for a row with `purpose` of "indicator" and `type` of "access".
    
Creating indicators
~~~~~~~~~~~~~~~~~~~
        
The following code files each collate resources in the database and output map files (images, and interactive html files) which may be used in reporting, and CSV data files for upload to the web portal.  These are saved to a study region specific folder located within the project `output` directory, drawing on the indicator measure definitions established in the `Resources` worksheet in the  `\_project\_configuration.xlsx` file.
        
**\_create\_linkage\_indicators.py**

Running this command will process resource rows with purpose of 'indicator' and type of 'linkage' which have a defined data source and method.  The linkage data set should have an identifier corresponding to the boundary data.  There are a number of settings which can be used to determine how the indicator is to be calculated (e.g. it may be linked directly, or used to derive a rate per sqkm or per amount of population or households, or all of these).  If more than one value exists per linkage area in the dataset, there is the option of how to aggregate these (e.g. count, sum, average).  In addition, linkage indicators may be formed as a function of multiple columns (e.g. a ratio or sum of two fields for a particular area).

**\_create\_raster\_indicators.py**

Create indicators from raster data sources based on aggregation to polygon area boundaries, defined in the `Resources` section of configuration file.

**\_create\_accessibility\_indicators.py**
    
Create indicators based on previously run accessibility analyses

Comparison plots
~~~~~~~~~~~~~~~~

**\_render\_plots.py**
    
Scatterplots and barplots of indicator results across regions can be generated as a supplement to maps for viewing results.  This is achieved by setting the value of the `plot` column in the `Resources` worksheet for a particular defined indicator to an area extent (e.g. "district" or "subdistrict").  If `regions\_of\_interest` has been defined in the `Parameters` worksheet, the generated scatterplots will have label annotations for these regions if they correspond to values matching the `regions\_of\_interest\_variable`.
    
Creating documentation
~~~~~~~~~~~~~~~~~~~~~~

**\_create\_documentation.py**

Following calculation of indicators, which generates a set of outputs for the study region in the project `output` folder, documentation for project progress to date may be generated in html and PDF format drawing upon individual indicator outputs using the command:

.. code-block:: text

   python _create_documentation.py bangkok
   
There is an optional `technical\_documentation` parameter in the `Parameters` worksheet of the configuration file, which may be set to True or False to determine whether the Technical documentation section detailing software installation, running, and methods will be included, or not.

Outputting indicators for the Healthy, Liveable Bangkok webportal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When the scripts described in the `Creating indicators` section above are run, 
