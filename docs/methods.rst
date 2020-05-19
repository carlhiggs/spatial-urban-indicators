Methods
=======

   
Commence analysis
~~~~~~~~~~~~~~~~~

We are now ready to commence analysis!  To launch the ind_bangkok computational environment, type `ind_bangkok` in the ind_bangkok project's root directory, the project 'process' folder or from the docker container directory ('process/docker').  

Once the container has loaded, type `cd process` to move into the process folder. This contains text files containing code which are used to complete various tasks.

There are two kinds of processing files, those which relate to setting up the resources required in order to calculate indicators, and those which draw upon the resources previously set up in order to calculate indicators or output their associated documentation.

Setting up resources
--------------------

.. automodule:: 00_create_database
    :members:
    
.. automodule:: 01_create_study_region
    :members:
    
.. automodule:: 02_create_population
    :members:
    
.. automodule:: 03_create_osm_resources
    :members:
    
.. automodule:: 04_create_network_resources
    :members:
    
.. automodule:: 05_open_space_areas_setup
    :members:
    
.. automodule:: 06_create_sample_points
    :members:
    
.. automodule:: 07_compile_destinations
    :members:
    
.. automodule:: 08_accessibility_analysis
    :members:

    
Creating indicators
-------------------
    
.. automodule:: _create_linkage_indicators
    :members:
    
.. automodule:: _create_raster_indicators
    :members:
    
.. automodule:: _create_accessibility_indicators
    :members:
    
Creating documentation
----------------------

.. automodule:: _create_documentation
    :members:

Other utilities
---------------

.. automodule:: _utils
    :members: