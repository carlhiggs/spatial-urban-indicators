Data structure
==============

Indicator data are output in a series of formats as a result of running the Bangkok Liveability scripted process.  These are represented by a series of folders for each output format.  

Documentation
~~~~~~~~~~~~~

The 'docs' folder contains a project documentation website which may be accessed by opening the file index.html in a web browser.  In addition, a PDF version of the project documentation is also generated in the project output folder.

CSV
~~~

The 'csv' folder contains comma seperated values (CSV) files for those indicators which have been processed to date. In each file, indicator data is referenced by an area level identifier. These may be used for uploading data to the proposed indicator portal, linking up with geojson boundaries for mapping.

Geojson
~~~~~~~

The 'geojson' folder contains geojson files which may be used to represent the spatial boundaries of province, subdistrict and district areas for Bangkok.  These are intended to be used for mapping and linkage purposes with the proposed indicator portal.  They are pre-associated with population and community statistics.

Geopackage
~~~~~~~~~~

The 'gpkg' folder contains a geopackage file which is a database containing spatial boundaries and linkage files.  Province, subdistrict and district boundaries associated with population and community indicators are included, as well as additional indicator tables which can be joined on via linkage on using the area ID variables.  These can be used for mapping, for example using the open source software package QGIS.

HTML
~~~~

Interactive 'preview' web maps of indicators are produced at district and subdistrict level as stand-alone html files.  Named according to the indicators they depict, these files may be opened in a web browser such as Chrome or Firefox. On hover, in addition to the specific indicator the file relates to additional population and community statistics are displayed.  There are two different kinds of base maps (simple, and OpenStreetMap), which may also be switched off to display the map with a plain background.  There is also an optional layer for place names.  

In a future update, it is planned to add improved mapping for categorical data or data with only two values.

PDF
~~~

This folder is currently empty.  The generation of higher quality PDF versions of maps is planned for a future release of the Bangkok Liveability software, however this is for a later update.

PNG
~~~

These are static maps of indicators, with legend, attribution, scale and a basic basemap of the study region.