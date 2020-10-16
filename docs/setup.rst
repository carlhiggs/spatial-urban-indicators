Project configuration
=====================

Before commencing analysis, the project must be configured using the Excel file located relative to the project directory (.) at `./process/_project_configuration.xlsx`.

In addition to containing project and study region specific parameters which are used by the scripted process, it also provides a a catalogue of project resources.

The content of the `Parameters` and `Resources` sheets is used to respectively determine the overall project settings, and how specific indicator measures are calculated.

Parameters
~~~~~~~~~~

New study regions can be added as columns in the `Parameters` worksheet, by copying an existing study region (e.g. Bangkok, or Bang Phlat) and modifying the parameter values as required.  Some parameters are technical and unlikely to be used, however descriptions of each have been provided, and the parameters most likely to require modification have been highlighted.  Each study region must have a unique lower case name with no spaces or special characters in the column heading, as this is used as a code to refer to the study region during processing and assignment of resources for the region.

Resources
~~~~~~~~~

The `Resources` sheet provides a catalog of project resources (rows) aligned with specific usage (for example, for calculating a specific indicator) including key details required for processing including, provenance, currency, licence requirements, storage location, and any usage notes. 

The main role of this sheet if for adding new indicator measures as rows in the `Resources` worksheet.  Each column field may be customised to determine the kind of indicator.  Customisable column attributes are detailed in full in the `About` worksheet, however include:

 - its `dimension` and `category` according to the Bangkok liveability framework, and matching the definitions in the `Bangkok context definitions` worksheet.
 - `indicator_measure` is the plain language name of the indicator 
 - `region` is the study region (as defined in `Parameters` under `full_locale`, e.g. "Bangkok") for the indicator
 - `type` is the type of indicator this will be, primarily determined by its data source: 'linkage' (linkage of area level estimates using an Excel spreadsheet with standard formatting), 'raster' (area summary of a raster dataset such as satellite imagery), or accessibility (percent of population with estimated access to an amenity based on network analysis using either OpenStreetMap or custom spatial data)
 - the location of the `data_file` to be used relative to the project directory
 - the `areas` to be summarised (using seperately defined resources with `purpose` of "boundaries")
 - and other attributes including metadata on methods and data source details, and how to map the indicator measures

Usage examples for how to prepare each of the three types of indicator (linkage, raster, and accessibility) will be provided in the webinar resource.  
