Indicators
==========


Study region boundaries
~~~~~~~~~~~~~~~~~~~~~~~

Bangkok subdistrict boundary data (BMA, 2019) were topologically corrected using GRASS and QGIS, to ensure polygon boundaries did not have gaps or overlaps.  Boundaries were matched with alternate spellings in both Thai and English for corresponding regions found in data from other organisations  and datasets  (e.g. NSO, HDX) in order to facilitate data linkage.   The final boundary layer was returned to BMA and agreed upon for usage. 

**Data source**: BangkokGIS (BMA)

**URL**: http://www.bangkokgis.com/bangkokgis_2008/userfiles/files/download/shapefile/administration/BMASubDistrict_Polygon.rar

**Publication year**: 2018

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190725

**Licence**: none specified

**Spatial reference (EPSG code)**: 32647.0

**Date type**: vector

**Scale / Resolution**: subdistrict

**Notes**: English names not provided; these have been derived using manual linkage with data from HDX subdistricts and population data provided by BMA, with verification from Kornsupha Nitvimol of BMA.

**Data location relative to project folder**: ./data/Bangkok_subdistricts_BMA_HLC_derived_20190805_cleaned_final.gpkg:subdistricts


Population and communities
~~~~~~~~~~~~~~~~~~~~~~~~~~

Population statistics targetting Bangkok in 2018 were received from the BMA, indexed by subdistrict. Fields included total population, sex strata, household, number of communities, and population in communities.  

**Data source**: BMA

**URL**: http://www.bangkok.go.th

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190805

**Licence**: none specified

**Scale / Resolution**: subdistrict

**Notes**: Derived population layer based on data received from Korn Nitviminol (BMA) via e-mail on 5 August 2019

**Data location relative to project folder**: ./data/Bangkok_subdistrict_population_BMA_HLC_derived_20190808.csv

Population data were linked with boundaries using corresponding subdistrict ID numbers.  Density measures were calculated using population statistics relative to analysis area size.  A derived 'population not in communities' indicator was also calculated, representing the disjunct between total population and the recorded population in communities.


Indicators
^^^^^^^^^^


Population per sqkm
-------------------


.. _bangkok_02_population_district_population_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_district_population_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population per sqkm" src="./../png/bangkok_02_population_district_population_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_population_per_sqkm.png




.. _bangkok_02_population_subdistrict_population_per_sqkm:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_subdistrict_population_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population per sqkm" src="./../png/bangkok_02_population_subdistrict_population_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_population_per_sqkm.png




Households per sqkm
-------------------


.. _bangkok_02_population_district_households_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_district_households_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Households per sqkm" src="./../png/bangkok_02_population_district_households_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_households_per_sqkm.png




.. _bangkok_02_population_subdistrict_households_per_sqkm:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_subdistrict_households_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Households per sqkm" src="./../png/bangkok_02_population_subdistrict_households_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_households_per_sqkm.png




Communities per sqkm
--------------------


.. _bangkok_02_population_district_communities_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_district_communities_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Communities per sqkm" src="./../png/bangkok_02_population_district_communities_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_communities_per_sqkm.png




.. _bangkok_02_population_subdistrict_communities_per_sqkm:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_subdistrict_communities_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Communities per sqkm" src="./../png/bangkok_02_population_subdistrict_communities_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_communities_per_sqkm.png




Population in communities per sqkm
----------------------------------


.. _bangkok_02_population_district_population_in_communities_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_district_population_in_communities_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population in communities per sqkm" src="./../png/bangkok_02_population_district_population_in_communities_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_population_in_communities_per_sqkm.png




.. _bangkok_02_population_subdistrict_population_in_communities_per_sqkm:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population in communities per sqkm" src="./../png/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.png




Population not in communities per sqkm
--------------------------------------


.. _bangkok_02_population_district_population_not_in_communities_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_district_population_not_in_communities_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_02_population_district_population_not_in_communities_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_population_not_in_communities_per_sqkm.png




.. _bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm.png




Fraction of Vegetation Cover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A modelled fraction of vegetation cover (FCOVER, V2) 1km grid data product based on Copernicus satellite imagery targetting 20 December 2018 was downloaded in NetCDF (.nc) format.  Using the ESA SNAP software, a GeoTiff (.tif) excerpt was taken for the Bangkok region.  Band 1 of this satellite data product represents the fraction of vegetation cover.  Data values ranging from 0 to 250 are to be transformed to a 0 to 1 range to represent the fraction of vegetation cover within each grid portion.  Cell values of 255 represent no data, and were excluded.

**Data source**: Copernicus Service Information

**URL**: https://land.copernicus.eu/global/products/fcover

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190913

**Licence**: Free, full and open access for lawful usage, with attribution

**Licence URL**: https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice

**Spatial reference (EPSG code)**: 4326.0

**Date type**: raster:float64

**Scale / Resolution**: 1000

**Data location relative to project folder**: ./data/ESA/Copernicus/subset_0_of_c_gls_FCOVER-RT6_201812200000_GLOBE_PROBAV_V2.tif


Indicators
^^^^^^^^^^


Vegetation Percent (Copernicus, 2018; mean)
-------------------------------------------

The estimated percentage of vegetation cover within each analysis area was calculated by first scaling the raster grid cell values by 100/250 ( a scale factor of 0.4) and then taking the mean (average) of all intersecting grid cells.


.. _bangkok_ind_subdistrict_vegetation_pct_mean:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_vegetation_pct_mean.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_vegetation_pct_mean.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_pct_mean.png




.. _bangkok_ind_district_vegetation_pct_mean:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_vegetation_pct_mean.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_vegetation_pct_mean.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_pct_mean.png




Vegetation Percent (Copernicus, 2018; standard deviation)
---------------------------------------------------------

The estimated standard deviation of percentage of vegetation cover within each analysis area was calculated by first scaling the raster grid cell values by 100/250 ( a scale factor of 0.4) and then taking the standard deviation of all intersecting grid cells.  This is a measure of the degree to wich estimates vary across a particular area, and is a useful contextual measure to accompany the average vegetation percent for the area.


.. _bangkok_ind_subdistrict_vegetation_pct_sd:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_vegetation_pct_sd.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_vegetation_pct_sd.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_pct_sd.png




.. _bangkok_ind_district_vegetation_pct_sd:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_vegetation_pct_sd.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_vegetation_pct_sd.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_pct_sd.png




Vital diseases
~~~~~~~~~~~~~~

Data at subdistrict level were prepared by Korn Nitvimol (BMA) and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: Department of Health, BMA

**Publication year**: 2018

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190617

**Licence**: none specified

**Date type**: integer

**Scale / Resolution**: points in subdistricts

**Notes**: A count of health centers (as provided by Korn Nitviminol of BMA)

**Data location relative to project folder**: ./data/_from BMA/20190617/vital diseases HC BMA 2018.xlsx


Indicators
^^^^^^^^^^


health centres (combined, 2018)
-------------------------------

The count of health centers within each analysis area was calculated, based on the supplied data.


.. _bangkok_ind_subdistrict_health_centres:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_health_centres.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_health_centres.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres.png




.. _bangkok_ind_district_health_centres:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_health_centres.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_health_centres.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres.png




mental and behavioural disorder outpatients (2018)
--------------------------------------------------

Outpatient numbers for mental and behavioural disorders were summed across each analysis area.


.. _bangkok_ind_subdistrict_outpatients_mental_health:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_outpatients_mental_health.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_outpatients_mental_health.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_mental_health.png




.. _bangkok_ind_district_outpatients_mental_health:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_outpatients_mental_health.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_outpatients_mental_health.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_mental_health.png




hypertension outpatients (2018)
-------------------------------

Outpatient numbers for hypertension were summed across each analysis area.


.. _bangkok_ind_subdistrict_outpatients_hypertension:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_outpatients_hypertension.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_outpatients_hypertension.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_hypertension.png




.. _bangkok_ind_district_outpatients_hypertension:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_outpatients_hypertension.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_outpatients_hypertension.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_hypertension.png




diabetes outpatients (2018)
---------------------------

Outpatient numbers for diabetes were summed across each analysis area.


.. _bangkok_ind_subdistrict_outpatients_diabetes:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_outpatients_diabetes.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_outpatients_diabetes.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_diabetes.png




.. _bangkok_ind_district_outpatients_diabetes:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_outpatients_diabetes.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_outpatients_diabetes.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_diabetes.png




vital diseases (combined, 2018)
-------------------------------

Outpatient numbers for all vital diseases (mental and behavioural disorders, hypertension, and diabetes) were summed across each analysis area.


.. _bangkok_ind_subdistrict_outpatients_combined_diseases:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_outpatients_combined_diseases.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_outpatients_combined_diseases.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_combined_diseases.png




.. _bangkok_ind_district_outpatients_combined_diseases:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_outpatients_combined_diseases.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_outpatients_combined_diseases.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_combined_diseases.png




Canal water quality
~~~~~~~~~~~~~~~~~~~

Data at district level were prepared by Korn Nitvimol (BMA) and supplied as an Excel workbook.  The data comprised sample point records of canal water quality for 130 canals where Dissolved Oxygen (DO) less than 2 amount 130 canals (224 storage points).  Data were cleaned for processing and aligned with area IDs. 

**Data source**: Department of Drainage and Sewerage, BMA

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190617

**Licence**: none specified

**Date type**: float

**Scale / Resolution**: points in districts

**Notes**: Canal water quality monitoring data received from Korn Nitviminol (BMA) on 17 June 2019

**Data location relative to project folder**: ./data/_from BMA/20190617/canal water quality 2018_final.xlsx


Indicators
^^^^^^^^^^


Canal water storage DO (mg/L), 2018
-----------------------------------

The average milligrams of dissolved oxygen per litre (DO mg/L) recorded at sample points within each analysis area was recorded.


.. _bangkok_ind_district_water_quality_do:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_water_quality_do.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_water_quality_do.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_do.png




Canal water storage BOD (mg/L), 2018
------------------------------------

The average milligrams of biochemical oxygen demand  per litre (DO mg/L) recorded at sample points within each analysis area was recorded.


.. _bangkok_ind_district_water_quality_bod:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_water_quality_bod.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_water_quality_bod.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_bod.png




Canal water storage with < 2 mg/L DO, 2018
------------------------------------------

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.


.. _bangkok_ind_district_water_quality_canals_poor:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_water_quality_canals_poor.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_water_quality_canals_poor.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor.png




Fire incidence
~~~~~~~~~~~~~~

Data at district level were prepared by Korn Nitvimol (BMA) and supplied as an Excel workbook.  Data were cleaned for processing and aligned with IDs. 

**Data source**: Fire and Rescue Department, BMA

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190809

**Licence**: none specified

**Date type**: table

**Scale / Resolution**: district

**Data location relative to project folder**: ./data/_from BMA/20190809/transfer_1673010_files_4a5fe795/Fire Incidence in Bangkok 2018_kn8919.xlsx


Indicators
^^^^^^^^^^


Fire incidence (BMA, 2018)
--------------------------

The number of fire occurences recorded for each analysis area within 2018 was recorded.


.. _bangkok_ind_fire_incidence:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_fire_incidence.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_fire_incidence.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_fire_incidence.png




Flood risk
~~~~~~~~~~

Data at subdistrict level were prepared by Korn Nitvimol (BMA) and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: Department of Drainage and Sewerage , BMA 

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190809

**Licence**: none specified

**Date type**: float

**Scale / Resolution**: locations in subdistricts

**Data location relative to project folder**: ./data/_from BMA/20190809/transfer_1673010_files_4a5fe795/BKK indicator_flood_kn 63019.xlsx


Indicators
^^^^^^^^^^


Main road flood area location count (BMA, 2018)
-----------------------------------------------

The count of main road flood areas associated with each analysis area was recorded.


.. _bangkok_ind_subdistrict_main_road_flood_locations:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations.png




.. _bangkok_ind_district_main_road_flood_locations:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_main_road_flood_locations.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_main_road_flood_locations.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations.png




Average days of rain across 14 main road flood areas (BMA, 2018)
----------------------------------------------------------------

The average number of days of rain recorded for 14 main road flood areas was taken for each analysis area.


.. _bangkok_ind_subdistrict_main_road_flood_days_rain:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_main_road_flood_days_rain.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_main_road_flood_days_rain.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_days_rain.png




.. _bangkok_ind_district_main_road_flood_days_rain:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_main_road_flood_days_rain.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_main_road_flood_days_rain.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_days_rain.png




Average maximum intensity across 14 main road flood areas (BMA, 2018)
---------------------------------------------------------------------

The average maximum intensity recorded for 14 main road flood areas was taken for each analysis area.


.. _bangkok_ind_subdistrict_main_road_flood_intensity:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_main_road_flood_intensity.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_main_road_flood_intensity.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_intensity.png




.. _bangkok_ind_district_main_road_flood_intensity:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_main_road_flood_intensity.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_main_road_flood_intensity.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_intensity.png




Average days of flooding across 14 main road flood areas (BMA, 2018)
--------------------------------------------------------------------

The average number of days of flooding recorded for 14 main road flood areas was taken for each analysis area.


.. _bangkok_ind_subdistrict_main_road_flood_days_flood:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_main_road_flood_days_flood.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_main_road_flood_days_flood.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_days_flood.png




.. _bangkok_ind_district_main_road_flood_days_flood:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_main_road_flood_days_flood.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_main_road_flood_days_flood.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_days_flood.png




Vulnerable flood area count (BMA, 2018)
---------------------------------------

The count of vulnerable flood areas associated with each analysis area was recorded.


.. _bangkok_ind_subdistrict_vulnerable_flood_areas:

**subdistrict**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas.png




.. _bangkok_ind_district_vulnerable_flood_areas:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_vulnerable_flood_areas.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_vulnerable_flood_areas.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas.png




Air quality
~~~~~~~~~~~

Data from monitoring stations were prepared by Korn Nitvimol (BMA) and supplied as an Excel workbook.  Data were cleaned for processing and aligned with IDs for districts containing the monitoring stations.  Point locations for monitoring stations were acquired from monitoring station geojson data retrieved from http://air4thai.pcd.go.th and aligned with the supplied data.

**Data source**: From article (Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019) citing data sourced from Thai Pollution Control Department websites http://air4thai.pcd.go.th and http://aqmthai.com/public_report.php

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190809

**Licence**: none specified

**Date type**: integer

**Scale / Resolution**: locations in districts

**Citation**: Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019

**Notes**: From article (Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019) citing data sourced from Thai Pollution Control Department websites http://air4thai.pcd.go.th and http://aqmthai.com/public_report.php

**Data location relative to project folder**: ./data/_from BMA/20190809/transfer_1673010_files_4a5fe795/air quality in Bangkok 2019 kn 7719.xlsx


Indicators
^^^^^^^^^^


monitoring stations (PCD, 2019)
-------------------------------

The count of monitoring stations in each analysis area was recorded.


.. _bangkok_ind_district_pcd_monitoring_stations:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_pcd_monitoring_stations.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_pcd_monitoring_stations.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations.png




Number of days PM 2.5 exceeds Thai standard (50 µg/m³; January 2019, PCD)
-------------------------------------------------------------------------

The average number of days PM 2.5 levels exceeded Thai standards during January 2019 were recorded for each analysis area, based on monitoring station records.


.. _bangkok_ind_district_pm2p5_days_exceeding_thai_standard:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_pm2p5_days_exceeding_thai_standard.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_pm2p5_days_exceeding_thai_standard.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pm2p5_days_exceeding_thai_standard.png




Number of days PM 2.5 exceeds WHO standard (25 µg/m³; January 2019, PCD)
------------------------------------------------------------------------

The average number of days PM 2.5 levels exceeded WHO standards during January 2019 were recorded for each analysis area, based on monitoring station records.


.. _bangkok_ind_district_pm2p5_days_exceeding_who_standard:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_pm2p5_days_exceeding_who_standard.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_pm2p5_days_exceeding_who_standard.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pm2p5_days_exceeding_who_standard.png




Food entrepreneurs
~~~~~~~~~~~~~~~~~~

Data comprising counts of restaurants, su[permarkets, minimarts, stalls and markets for each district were prepared by Korn Nitvimol (BMA) and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: Department of Environment and Sanitation, BMA

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190820

**Licence**: none specified

**Date type**: integer

**Scale / Resolution**: locations in districts

**Data location relative to project folder**: ./data/_from BMA/20190820/transfer_1682928_files_504fdeaf/Num of food entrepreneur in Bangkok 2019 -kn15819.xlsx


Indicators
^^^^^^^^^^


Number of restaurants (BMA, 2019)
---------------------------------

The number of restaurants within each analysis area was recorded.


.. _bangkok_ind_district_restaurants:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_restaurants.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_restaurants.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants.png




Number of restaurants per 10,000 population (BMA, 2019)
-------------------------------------------------------

The number of restaurants per 10,000 population within each analysis area was divided by the population within that area divided by 10,000 and then recorded.


.. _bangkok_ind_district_restaurants_per_10k_population:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_restaurants_per_10k_population.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_restaurants_per_10k_population.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_per_10k_population.png




Number of restaurants per square kilometre (BMA, 2019)
------------------------------------------------------

The number of restaurants per square kilometre within each analysis area was divided by the size of the area in square kilometres and then recorded.


.. _bangkok_ind_district_restaurants_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_restaurants_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_restaurants_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_per_sqkm.png




Number of supermarkets (BMA, 2019)
----------------------------------

The number of supermarkets within each analysis area was recorded.


.. _bangkok_ind_district_supermarkets:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_supermarkets.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_supermarkets.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets.png




Number of supermarkets per 10,000 population (BMA, 2019)
--------------------------------------------------------

The number of supermarkets per 10,000 population within each analysis area was divided by the population within that area divided by 10,000 and then recorded.


.. _bangkok_ind_district_supermarkets_per_10k_population:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_supermarkets_per_10k_population.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_supermarkets_per_10k_population.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_per_10k_population.png




Number of supermarkets per square kilometre (BMA, 2019)
-------------------------------------------------------

The number of supermarkets per square kilometre within each analysis area was divided by the size of the area in square kilometres and then recorded.


.. _bangkok_ind_district_supermarkets_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_supermarkets_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_supermarkets_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_per_sqkm.png




Number of minimarts (BMA, 2019)
-------------------------------

The number of minimarts within each analysis area was recorded.


.. _bangkok_ind_district_minimarts:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_minimarts.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_minimarts.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts.png




Number of minimarts per 10,000 population (BMA, 2019)
-----------------------------------------------------

The number of minimarts per 10,000 population within each analysis area was divided by the population within that area divided by 10,000 and then recorded.


.. _bangkok_ind_district_minimarts_per_10k_population:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_minimarts_per_10k_population.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_minimarts_per_10k_population.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_per_10k_population.png




Number of minimarts per square kilometre (BMA, 2019)
----------------------------------------------------

The number of minimarts per square kilometre within each analysis area was divided by the size of the area in square kilometres and then recorded.


.. _bangkok_ind_district_minimarts_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_minimarts_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_minimarts_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_per_sqkm.png




Number of stalls (BMA, 2019)
----------------------------

The number of stalls within each analysis area was recorded.


.. _bangkok_ind_district_stalls:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_stalls.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_stalls.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls.png




Number of stalls per 10,000 population (BMA, 2019)
--------------------------------------------------

The number of stalls per 10,000 population within each analysis area was divided by the population within that area divided by 10,000 and then recorded.


.. _bangkok_ind_district_stalls_per_10k_population:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_stalls_per_10k_population.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_stalls_per_10k_population.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_per_10k_population.png




Number of stalls per square kilometre (BMA, 2019)
-------------------------------------------------

The number of stalls per square kilometre within each analysis area was divided by the size of the area in square kilometres and then recorded.


.. _bangkok_ind_district_stalls_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_stalls_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_stalls_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_per_sqkm.png




Number of markets (BMA, 2019)
-----------------------------

The number of markets within each analysis area was recorded.


.. _bangkok_ind_district_markets:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_markets.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_markets.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets.png




Number of markets per 10,000 population (BMA, 2019)
---------------------------------------------------

The number of markets per 10,000 population within each analysis area was divided by the population within that area divided by 10,000 and then recorded.


.. _bangkok_ind_district_markets_per_10k_population:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_markets_per_10k_population.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_markets_per_10k_population.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_per_10k_population.png




Number of markets per square kilometre (BMA, 2019)
--------------------------------------------------

The number of markets per square kilometre within each analysis area was divided by the size of the area in square kilometres and then recorded.


.. _bangkok_ind_district_markets_per_sqkm:

**district**


.. only:: html

    .. raw:: html

        <a href="./../html/bangkok_ind_district_markets_per_sqkm.html" target="_blank">Open interactive map in new tab</a><br>        <img alt="Population not in communities per sqkm" src="./../png/bangkok_ind_district_markets_per_sqkm.png">

.. only:: latex

    .. image:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_per_sqkm.png



