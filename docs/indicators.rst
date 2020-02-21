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

District and changwat boundaries were constructed through geometrical union of the constituent subdistricts they were aligned with.  Boundaries at all three scales (subdistrict, district, changwat) were imported into the project database and used as analysis areas when constructing other indicators, as required.  The area in square kilometres of each analysis area's polygonal extent was recorded.   The changwat (province) of Bangkok was used to define the Bangkok metropolitan study region extent.  A ten kilometre buffer extending beyond this is used when conducting analyses of access to resources, so that access to destinations outside the study region would be accounted for peri-urban regions when undertaking network analysis.  



.. only:: html

    .. raw:: html

        <figure>
        <img alt="Bangkok study region" src="./../png/bangkok_01_study_region.png">
        <figcaption>Bangkok study region.         <a href="./../html/bangkok_01_study_region.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_01_study_region.png
       :width: 70%
       :align: center

       Bangkok study region




Population and communities
~~~~~~~~~~~~~~~~~~~~~~~~~~

Population statistics targetting Bangkok in 2018 were received from the Bangkok Metropolitan Administration, indexed by subdistrict. Fields included total population, sex strata, household, number of communities, and population in communities.  

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


Population per km²
------------------





.. only:: html

    .. raw:: html

        <figure>
        <img alt="Population per km², by district" src="./../png/bangkok_02_population_district_population_per_sqkm.png">
        <figcaption>Population per km², by district.         <a href="./../html/bangkok_02_population_district_population_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_population_per_sqkm.png
       :width: 70%
       :align: center

       Population per km², by district







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Population per km², by subdistrict" src="./../png/bangkok_02_population_subdistrict_population_per_sqkm.png">
        <figcaption>Population per km², by subdistrict.         <a href="./../html/bangkok_02_population_subdistrict_population_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_population_per_sqkm.png
       :width: 70%
       :align: center

       Population per km², by subdistrict




Households per km²
------------------





.. only:: html

    .. raw:: html

        <figure>
        <img alt="Households per km², by district" src="./../png/bangkok_02_population_district_households_per_sqkm.png">
        <figcaption>Households per km², by district.         <a href="./../html/bangkok_02_population_district_households_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_households_per_sqkm.png
       :width: 70%
       :align: center

       Households per km², by district







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Households per km², by subdistrict" src="./../png/bangkok_02_population_subdistrict_households_per_sqkm.png">
        <figcaption>Households per km², by subdistrict.         <a href="./../html/bangkok_02_population_subdistrict_households_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_households_per_sqkm.png
       :width: 70%
       :align: center

       Households per km², by subdistrict




Communities per km²
-------------------





.. only:: html

    .. raw:: html

        <figure>
        <img alt="Communities per km², by district" src="./../png/bangkok_02_population_district_communities_per_sqkm.png">
        <figcaption>Communities per km², by district.         <a href="./../html/bangkok_02_population_district_communities_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_communities_per_sqkm.png
       :width: 70%
       :align: center

       Communities per km², by district







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Communities per km², by subdistrict" src="./../png/bangkok_02_population_subdistrict_communities_per_sqkm.png">
        <figcaption>Communities per km², by subdistrict.         <a href="./../html/bangkok_02_population_subdistrict_communities_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_communities_per_sqkm.png
       :width: 70%
       :align: center

       Communities per km², by subdistrict




Population in communities per km²
---------------------------------


Aligns with Sustainable Development Goals: 11.




.. only:: html

    .. raw:: html

        <figure>
        <img alt="Population in communities per km², by district" src="./../png/bangkok_02_population_district_population_in_communities_per_sqkm.png">
        <figcaption>Population in communities per km², by district.         <a href="./../html/bangkok_02_population_district_population_in_communities_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_population_in_communities_per_sqkm.png
       :width: 70%
       :align: center

       Population in communities per km², by district




Aligns with Sustainable Development Goals: 11.




.. only:: html

    .. raw:: html

        <figure>
        <img alt="Population in communities per km², by subdistrict" src="./../png/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.png">
        <figcaption>Population in communities per km², by subdistrict.         <a href="./../html/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.png
       :width: 70%
       :align: center

       Population in communities per km², by subdistrict




Population not in communities per km²
-------------------------------------





.. only:: html

    .. raw:: html

        <figure>
        <img alt="Population not in communities per km², by district" src="./../png/bangkok_02_population_district_population_not_in_communities_per_sqkm.png">
        <figcaption>Population not in communities per km², by district.         <a href="./../html/bangkok_02_population_district_population_not_in_communities_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_district_population_not_in_communities_per_sqkm.png
       :width: 70%
       :align: center

       Population not in communities per km², by district







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Population not in communities per km², by subdistrict" src="./../png/bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm.png">
        <figcaption>Population not in communities per km², by subdistrict.         <a href="./../html/bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_population_not_in_communities_per_sqkm.png
       :width: 70%
       :align: center

       Population not in communities per km², by subdistrict




City problems
~~~~~~~~~~~~~


Fire incidence
--------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with IDs. 

**Data source**: Fire and Rescue Department, BMA

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190809

**Licence**: none specified

**Date type**: table

**Scale / Resolution**: area summary

**Data location relative to project folder**: ./data/Thai/_from BMA/20190809/transfer_1673010_files_4a5fe795/Fire Incidence in Bangkok 2018_kn8919.xlsx


Fire incidence (BMA, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (BMA, 2018), by district" src="./../png/bangkok_ind_district_fire_incidence.png">
        <figcaption>Fire incidence (BMA, 2018), by district.         <a href="./../html/bangkok_ind_district_fire_incidence.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence.png
       :width: 70%
       :align: center

       Fire incidence (BMA, 2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) by population src="./../png/plots/district_fire_incidence_population.png" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) by population per sqkm src="./../png/plots/district_fire_incidence_population_per_sqkm.png" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018), ranked in ascending order src="./../png/plots/district_fire_incidence.png">
            </div>
       <figcaption>Figures for สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) with regard to Fire Incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/plots/district_fire_incidence.png
       :width: 100%
       :align: center

       Districts ranked in ascending order by สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) with regard to Fire Incidence.




Fire incidence (BMA, 2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (BMA, 2018) per km², by district" src="./../png/bangkok_ind_district_fire_incidence_rate_area.png">
        <figcaption>Fire incidence (BMA, 2018) per km², by district.         <a href="./../html/bangkok_ind_district_fire_incidence_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence_rate_area.png
       :width: 70%
       :align: center

       Fire incidence (BMA, 2018) per km², by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per km² by population src="./../png/plots/district_fire_incidence_rate_area_population.png" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per km² by population per sqkm src="./../png/plots/district_fire_incidence_rate_area_population_per_sqkm.png" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per km², ranked in ascending order src="./../png/plots/district_fire_incidence_rate_area.png">
            </div>
       <figcaption>Figures for สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per km² with regard to Fire Incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/plots/district_fire_incidence_rate_area.png
       :width: 100%
       :align: center

       Districts ranked in ascending order by สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per km² with regard to Fire Incidence.




Fire incidence (BMA, 2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (BMA, 2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_fire_incidence_rate_population.png">
        <figcaption>Fire incidence (BMA, 2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_fire_incidence_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence_rate_population.png
       :width: 70%
       :align: center

       Fire incidence (BMA, 2018) per 10,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 population by population src="./../png/plots/district_fire_incidence_rate_population_population.png" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 population by population per sqkm src="./../png/plots/district_fire_incidence_rate_population_population_per_sqkm.png" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 population, ranked in ascending order src="./../png/plots/district_fire_incidence_rate_population.png">
            </div>
       <figcaption>Figures for สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 population with regard to Fire Incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/plots/district_fire_incidence_rate_population.png
       :width: 100%
       :align: center

       Districts ranked in ascending order by สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 population with regard to Fire Incidence.




Fire incidence (BMA, 2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (BMA, 2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_fire_incidence_rate_household.png">
        <figcaption>Fire incidence (BMA, 2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_fire_incidence_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence_rate_household.png
       :width: 70%
       :align: center

       Fire incidence (BMA, 2018) per 10,000 household, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 household by population src="./../png/plots/district_fire_incidence_rate_household_population.png" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 household by population per sqkm src="./../png/plots/district_fire_incidence_rate_household_population_per_sqkm.png" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 household, ranked in ascending order src="./../png/plots/district_fire_incidence_rate_household.png">
            </div>
       <figcaption>Figures for สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 household with regard to Fire Incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/plots/district_fire_incidence_rate_household.png
       :width: 100%
       :align: center

       Districts ranked in ascending order by สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 household with regard to Fire Incidence.




Flood risk
----------

Data at subdistrict level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: Department of Drainage and Sewerage , BMA 

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190809

**Licence**: none specified

**Date type**: float

**Scale / Resolution**: area summary

**Notes**: units of intensity  - mm?

**Data location relative to project folder**: ./data/Thai/_from BMA/20190809/transfer_1673010_files_4a5fe795/BKK indicator_flood_kn 63019.xlsx


Average days of flooding across 14 main road flood areas (BMA, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average number of days of flooding recorded for 14 main road flood areas was taken for each analysis area.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of flooding across 14 main road flood areas (BMA, 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_days_flood.png">
        <figcaption>Average days of flooding across 14 main road flood areas (BMA, 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_days_flood.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_days_flood.png
       :width: 70%
       :align: center

       Average days of flooding across 14 main road flood areas (BMA, 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of flooding across 14 main road flood areas (BMA, 2018), by district" src="./../png/bangkok_ind_district_main_road_flood_days_flood.png">
        <figcaption>Average days of flooding across 14 main road flood areas (BMA, 2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_days_flood.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_days_flood.png
       :width: 70%
       :align: center

       Average days of flooding across 14 main road flood areas (BMA, 2018), by district




Average days of rain across 14 main road flood areas (BMA, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average number of days of rain recorded for 14 main road flood areas was taken for each analysis area.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of rain across 14 main road flood areas (BMA, 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_days_rain.png">
        <figcaption>Average days of rain across 14 main road flood areas (BMA, 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_days_rain.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_days_rain.png
       :width: 70%
       :align: center

       Average days of rain across 14 main road flood areas (BMA, 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of rain across 14 main road flood areas (BMA, 2018), by district" src="./../png/bangkok_ind_district_main_road_flood_days_rain.png">
        <figcaption>Average days of rain across 14 main road flood areas (BMA, 2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_days_rain.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_days_rain.png
       :width: 70%
       :align: center

       Average days of rain across 14 main road flood areas (BMA, 2018), by district




Average maximum intensity across 14 main road flood areas (BMA, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average maximum intensity recorded for 14 main road flood areas was taken for each analysis area.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average maximum intensity across 14 main road flood areas (BMA, 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_intensity.png">
        <figcaption>Average maximum intensity across 14 main road flood areas (BMA, 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_intensity.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_intensity.png
       :width: 70%
       :align: center

       Average maximum intensity across 14 main road flood areas (BMA, 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average maximum intensity across 14 main road flood areas (BMA, 2018), by district" src="./../png/bangkok_ind_district_main_road_flood_intensity.png">
        <figcaption>Average maximum intensity across 14 main road flood areas (BMA, 2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_intensity.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_intensity.png
       :width: 70%
       :align: center

       Average maximum intensity across 14 main road flood areas (BMA, 2018), by district




Main road flood area location count (BMA, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations.png">
        <figcaption>Main road flood area location count (BMA, 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018), by district" src="./../png/bangkok_ind_district_main_road_flood_locations.png">
        <figcaption>Main road flood area location count (BMA, 2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018), by district




Main road flood area location count (BMA, 2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations_rate_area.png">
        <figcaption>Main road flood area location count (BMA, 2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations_rate_area.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018) per km², by district" src="./../png/bangkok_ind_district_main_road_flood_locations_rate_area.png">
        <figcaption>Main road flood area location count (BMA, 2018) per km², by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations_rate_area.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018) per km², by district




Main road flood area location count (BMA, 2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations_rate_population.png">
        <figcaption>Main road flood area location count (BMA, 2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations_rate_population.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_main_road_flood_locations_rate_population.png">
        <figcaption>Main road flood area location count (BMA, 2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations_rate_population.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018) per 10,000 population, by district




Main road flood area location count (BMA, 2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations_rate_household.png">
        <figcaption>Main road flood area location count (BMA, 2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations_rate_household.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (BMA, 2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_main_road_flood_locations_rate_household.png">
        <figcaption>Main road flood area location count (BMA, 2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations_rate_household.png
       :width: 70%
       :align: center

       Main road flood area location count (BMA, 2018) per 10,000 household, by district




Vulnerable flood area count (BMA, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas.png">
        <figcaption>Vulnerable flood area count (BMA, 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018), by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas.png">
        <figcaption>Vulnerable flood area count (BMA, 2018), by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018), by district




Vulnerable flood area count (BMA, 2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_area.png">
        <figcaption>Vulnerable flood area count (BMA, 2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_area.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018) per km², by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas_rate_area.png">
        <figcaption>Vulnerable flood area count (BMA, 2018) per km², by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas_rate_area.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018) per km², by district




Vulnerable flood area count (BMA, 2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_population.png">
        <figcaption>Vulnerable flood area count (BMA, 2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_population.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas_rate_population.png">
        <figcaption>Vulnerable flood area count (BMA, 2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas_rate_population.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018) per 10,000 population, by district




Vulnerable flood area count (BMA, 2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_household.png">
        <figcaption>Vulnerable flood area count (BMA, 2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_household.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (BMA, 2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas_rate_household.png">
        <figcaption>Vulnerable flood area count (BMA, 2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas_rate_household.png
       :width: 70%
       :align: center

       Vulnerable flood area count (BMA, 2018) per 10,000 household, by district




Sentinel-5P NRTI NO2: Near Real-Time Nitrogen Dioxide
-----------------------------------------------------

Google Earth Engine was used to process Sentinel 5p data from the Copernicus satellite detailing total vertical column of NO2 (ratio of the slant column density of NO2 and the total air mass factor), taking the annual average from 13 October 2017 (commencement of the S5P monitoring mission) to 12 October 2018.  

**Data source**: Copernicus Sentinel Data processed using Google Earth Engine

**URL**: https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_NO2

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20191009

**Licence**: Free, full and open access for lawful usage, with attribution

**Licence URL**: https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice

**Spatial reference (EPSG code)**: 4326.0

**Date type**: raster:float64

**Scale / Resolution**: 10

**Notes**: Free access, but must acknowledge Copernicus Sentinel, year of data and if it has been modified.  Requires processing, as data is in half hourly updates.

**Data location relative to project folder**: ./data/International/Google EarthEngine/copernicus_s5p_nrti_l3_no2-mean_col_num_density_20171013_20181012.tif


Annual average NO2 (Copernicus, 2017-18)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total vertical column of NO2 is a measure of air pollution, however it is based on tropospheric and stratospheric presence of NO2 and measured in mmol per square metre; in contrast, health guidelines for exposure are usually based on ground monitoring of NO2, recorded in parts per billion.  As a spatially continuous measure, annual average NO2 is useful for indicating areas of relatively intense pollution and may be compared with ground based measures (ie. from monitoring stations) as well as longitudinally to monitor change over time.  For mapping purposes, NO2 was scaled as 1-e6 mmol per square metre (ie. divided by 0.000001).






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Annual average NO2 (Copernicus, 2017-18), by subdistrict" src="./../png/bangkok_ind_subdistrict_no2_2017_18_mean.png">
        <figcaption>Annual average NO2 (Copernicus, 2017-18), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_no2_2017_18_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_no2_2017_18_mean.png
       :width: 70%
       :align: center

       Annual average NO2 (Copernicus, 2017-18), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Annual average NO2 (Copernicus, 2017-18), by district" src="./../png/bangkok_ind_district_no2_2017_18_mean.png">
        <figcaption>Annual average NO2 (Copernicus, 2017-18), by district.         <a href="./../html/bangkok_ind_district_no2_2017_18_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_no2_2017_18_mean.png
       :width: 70%
       :align: center

       Annual average NO2 (Copernicus, 2017-18), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Air quality by population src="./../png/plots/district_no2_2017_18_mean_population.png" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Air quality by population per sqkm src="./../png/plots/district_no2_2017_18_mean_population_per_sqkm.png" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Air quality, ranked in ascending order src="./../png/plots/district_no2_2017_18_mean.png">
            </div>
       <figcaption>Figures for Air quality with regard to Annual Average No2 (1-E6 Mmol/M²; 2017-18) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/plots/district_no2_2017_18_mean.png
       :width: 100%
       :align: center

       Districts ranked in ascending order by Air quality with regard to Annual Average No2 (1-E6 Mmol/M²; 2017-18).




Air quality
-----------

Data from monitoring stations were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with IDs for districts containing the monitoring stations.  Point locations for monitoring stations were acquired from monitoring station geojson data retrieved from http://air4thai.pcd.go.th and aligned with the supplied data.

**Data source**: From article (Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019) citing data sourced from Thai Pollution Control Department websites http://air4thai.pcd.go.th and http://aqmthai.com/public_report.php

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190809

**Licence**: none specified

**Date type**: integer

**Scale / Resolution**: area summary

**Citation**: Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019

**Notes**: From article (Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019) citing data sourced from Thai Pollution Control Department websites http://air4thai.pcd.go.th and http://aqmthai.com/public_report.php

**Data location relative to project folder**: ./data/Thai/_from BMA/20190809/transfer_1673010_files_4a5fe795/air quality in Bangkok 2019 kn 7719.xlsx


Monitoring stations (PCD, 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Monitoring stations (PCD, 2019), by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations.png">
        <figcaption>Monitoring stations (PCD, 2019), by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations.png
       :width: 70%
       :align: center

       Monitoring stations (PCD, 2019), by district




Monitoring stations (PCD, 2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Monitoring stations (PCD, 2019) per km², by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations_rate_area.png">
        <figcaption>Monitoring stations (PCD, 2019) per km², by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations_rate_area.png
       :width: 70%
       :align: center

       Monitoring stations (PCD, 2019) per km², by district




Monitoring stations (PCD, 2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Monitoring stations (PCD, 2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations_rate_population.png">
        <figcaption>Monitoring stations (PCD, 2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations_rate_population.png
       :width: 70%
       :align: center

       Monitoring stations (PCD, 2019) per 10,000 population, by district




Monitoring stations (PCD, 2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Monitoring stations (PCD, 2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations_rate_household.png">
        <figcaption>Monitoring stations (PCD, 2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations_rate_household.png
       :width: 70%
       :align: center

       Monitoring stations (PCD, 2019) per 10,000 household, by district




Number of days PM 2.5 exceeds Thai standard (50 µg/m³; January 2019, PCD)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average number of days PM 2.5 levels exceeded Thai standards during January 2019 were recorded for each analysis area, based on monitoring station records.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of days PM 2.5 exceeds Thai standard (50 µg/m³; January 2019, PCD), by district" src="./../png/bangkok_ind_district_pm2p5_days_exceeding_thai_standard.png">
        <figcaption>Number of days PM 2.5 exceeds Thai standard (50 µg/m³; January 2019, PCD), by district.         <a href="./../html/bangkok_ind_district_pm2p5_days_exceeding_thai_standard.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pm2p5_days_exceeding_thai_standard.png
       :width: 70%
       :align: center

       Number of days PM 2.5 exceeds Thai standard (50 µg/m³; January 2019, PCD), by district




Number of days PM 2.5 exceeds WHO standard (25 µg/m³; January 2019, PCD)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average number of days PM 2.5 levels exceeded WHO standards during January 2019 were recorded for each analysis area, based on monitoring station records.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of days PM 2.5 exceeds WHO standard (25 µg/m³; January 2019, PCD), by district" src="./../png/bangkok_ind_district_pm2p5_days_exceeding_who_standard.png">
        <figcaption>Number of days PM 2.5 exceeds WHO standard (25 µg/m³; January 2019, PCD), by district.         <a href="./../html/bangkok_ind_district_pm2p5_days_exceeding_who_standard.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pm2p5_days_exceeding_who_standard.png
       :width: 70%
       :align: center

       Number of days PM 2.5 exceeds WHO standard (25 µg/m³; January 2019, PCD), by district




Canal water quality
-------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  The data comprised sample point records of canal water quality for 130 canals where Dissolved Oxygen (DO) less than 2 amount 130 canals (224 storage points).  Data were cleaned for processing and aligned with area IDs. 

**Data source**: Department of Drainage and Sewerage, BMA

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190617

**Licence**: none specified

**Date type**: float

**Scale / Resolution**: area summary

**Data location relative to project folder**: ./data/Thai/_from BMA/20190617/canal water quality 2018_final.xlsx


Canal water storage BOD (mg/L), 2018
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average milligrams of biochemical oxygen demand  per litre (BOD mg/L) recorded at sample points within each analysis area was recorded.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage BOD (mg/L), 2018, by district" src="./../png/bangkok_ind_district_water_quality_bod.png">
        <figcaption>Canal water storage BOD (mg/L), 2018, by district.         <a href="./../html/bangkok_ind_district_water_quality_bod.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_bod.png
       :width: 70%
       :align: center

       Canal water storage BOD (mg/L), 2018, by district




Canal water storage with < 2 mg/L DO, 2018
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage with < 2 mg/L DO, 2018, by district" src="./../png/bangkok_ind_district_water_quality_canals_poor.png">
        <figcaption>Canal water storage with < 2 mg/L DO, 2018, by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor.png
       :width: 70%
       :align: center

       Canal water storage with < 2 mg/L DO, 2018, by district




Canal water storage with < 2 mg/L DO, 2018 per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage with < 2 mg/L DO, 2018 per km², by district" src="./../png/bangkok_ind_district_water_quality_canals_poor_rate_area.png">
        <figcaption>Canal water storage with < 2 mg/L DO, 2018 per km², by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor_rate_area.png
       :width: 70%
       :align: center

       Canal water storage with < 2 mg/L DO, 2018 per km², by district




Canal water storage with < 2 mg/L DO, 2018 per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage with < 2 mg/L DO, 2018 per 10,000 population, by district" src="./../png/bangkok_ind_district_water_quality_canals_poor_rate_population.png">
        <figcaption>Canal water storage with < 2 mg/L DO, 2018 per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor_rate_population.png
       :width: 70%
       :align: center

       Canal water storage with < 2 mg/L DO, 2018 per 10,000 population, by district




Canal water storage with < 2 mg/L DO, 2018 per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage with < 2 mg/L DO, 2018 per 10,000 household, by district" src="./../png/bangkok_ind_district_water_quality_canals_poor_rate_household.png">
        <figcaption>Canal water storage with < 2 mg/L DO, 2018 per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor_rate_household.png
       :width: 70%
       :align: center

       Canal water storage with < 2 mg/L DO, 2018 per 10,000 household, by district




Canal water storage DO (mg/L), 2018
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average milligrams of dissolved oxygen per litre (DO mg/L) recorded at sample points within each analysis area was recorded.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage DO (mg/L), 2018, by district" src="./../png/bangkok_ind_district_water_quality_do.png">
        <figcaption>Canal water storage DO (mg/L), 2018, by district.         <a href="./../html/bangkok_ind_district_water_quality_do.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_do.png
       :width: 70%
       :align: center

       Canal water storage DO (mg/L), 2018, by district




Quality of life
~~~~~~~~~~~~~~~


Vital diseases
--------------

Data at {area} level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: Department of Health, BMA

**Publication year**: 2018

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190617

**Licence**: none specified

**Date type**: integer

**Scale / Resolution**: area summary

**Data location relative to project folder**: ./data/Thai/_from BMA/20190617/vital diseases HC BMA 2018.xlsx


Health centres (combined, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres.png">
        <figcaption>Health centres (combined, 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres.png
       :width: 70%
       :align: center

       Health centres (combined, 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018), by district" src="./../png/bangkok_ind_district_health_centres.png">
        <figcaption>Health centres (combined, 2018), by district.         <a href="./../html/bangkok_ind_district_health_centres.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres.png
       :width: 70%
       :align: center

       Health centres (combined, 2018), by district




Health centres (combined, 2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres_rate_area.png">
        <figcaption>Health centres (combined, 2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres_rate_area.png
       :width: 70%
       :align: center

       Health centres (combined, 2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018) per km², by district" src="./../png/bangkok_ind_district_health_centres_rate_area.png">
        <figcaption>Health centres (combined, 2018) per km², by district.         <a href="./../html/bangkok_ind_district_health_centres_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres_rate_area.png
       :width: 70%
       :align: center

       Health centres (combined, 2018) per km², by district




Health centres (combined, 2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres_rate_population.png">
        <figcaption>Health centres (combined, 2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres_rate_population.png
       :width: 70%
       :align: center

       Health centres (combined, 2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_health_centres_rate_population.png">
        <figcaption>Health centres (combined, 2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_health_centres_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres_rate_population.png
       :width: 70%
       :align: center

       Health centres (combined, 2018) per 10,000 population, by district




Health centres (combined, 2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres_rate_household.png">
        <figcaption>Health centres (combined, 2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres_rate_household.png
       :width: 70%
       :align: center

       Health centres (combined, 2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centres (combined, 2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_health_centres_rate_household.png">
        <figcaption>Health centres (combined, 2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_health_centres_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres_rate_household.png
       :width: 70%
       :align: center

       Health centres (combined, 2018) per 10,000 household, by district




Vital diseases (combined, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for all vital diseases (mental and behavioural disorders, hypertension, and diabetes) were summed across each analysis area.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_combined_diseases.png">
        <figcaption>Vital diseases (combined, 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_combined_diseases.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_combined_diseases.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018), by district" src="./../png/bangkok_ind_district_outpatients_combined_diseases.png">
        <figcaption>Vital diseases (combined, 2018), by district.         <a href="./../html/bangkok_ind_district_outpatients_combined_diseases.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_combined_diseases.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018), by district




Vital diseases (combined, 2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for all vital diseases (mental and behavioural disorders, hypertension, and diabetes) were summed across each analysis area.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_area.png">
        <figcaption>Vital diseases (combined, 2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_area.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018) per km², by district" src="./../png/bangkok_ind_district_outpatients_combined_diseases_rate_area.png">
        <figcaption>Vital diseases (combined, 2018) per km², by district.         <a href="./../html/bangkok_ind_district_outpatients_combined_diseases_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_combined_diseases_rate_area.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018) per km², by district




Vital diseases (combined, 2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for all vital diseases (mental and behavioural disorders, hypertension, and diabetes) were summed across each analysis area.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_population.png">
        <figcaption>Vital diseases (combined, 2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_population.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_outpatients_combined_diseases_rate_population.png">
        <figcaption>Vital diseases (combined, 2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_outpatients_combined_diseases_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_combined_diseases_rate_population.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018) per 10,000 population, by district




Vital diseases (combined, 2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for all vital diseases (mental and behavioural disorders, hypertension, and diabetes) were summed across each analysis area.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_household.png">
        <figcaption>Vital diseases (combined, 2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_combined_diseases_rate_household.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vital diseases (combined, 2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_outpatients_combined_diseases_rate_household.png">
        <figcaption>Vital diseases (combined, 2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_outpatients_combined_diseases_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_combined_diseases_rate_household.png
       :width: 70%
       :align: center

       Vital diseases (combined, 2018) per 10,000 household, by district




Diabetes outpatients (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for diabetes were summed across each analysis area.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_diabetes.png">
        <figcaption>Diabetes outpatients (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_diabetes.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_diabetes.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018), by district" src="./../png/bangkok_ind_district_outpatients_diabetes.png">
        <figcaption>Diabetes outpatients (2018), by district.         <a href="./../html/bangkok_ind_district_outpatients_diabetes.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_diabetes.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018), by district




Diabetes outpatients (2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for diabetes were summed across each analysis area.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_diabetes_rate_area.png">
        <figcaption>Diabetes outpatients (2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_diabetes_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_diabetes_rate_area.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018) per km², by district" src="./../png/bangkok_ind_district_outpatients_diabetes_rate_area.png">
        <figcaption>Diabetes outpatients (2018) per km², by district.         <a href="./../html/bangkok_ind_district_outpatients_diabetes_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_diabetes_rate_area.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018) per km², by district




Diabetes outpatients (2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for diabetes were summed across each analysis area.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_diabetes_rate_population.png">
        <figcaption>Diabetes outpatients (2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_diabetes_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_diabetes_rate_population.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_outpatients_diabetes_rate_population.png">
        <figcaption>Diabetes outpatients (2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_outpatients_diabetes_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_diabetes_rate_population.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018) per 10,000 population, by district




Diabetes outpatients (2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for diabetes were summed across each analysis area.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_diabetes_rate_household.png">
        <figcaption>Diabetes outpatients (2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_diabetes_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_diabetes_rate_household.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Diabetes outpatients (2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_outpatients_diabetes_rate_household.png">
        <figcaption>Diabetes outpatients (2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_outpatients_diabetes_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_diabetes_rate_household.png
       :width: 70%
       :align: center

       Diabetes outpatients (2018) per 10,000 household, by district




Hypertension outpatients (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for hypertension were summed across each analysis area.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_hypertension.png">
        <figcaption>Hypertension outpatients (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_hypertension.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_hypertension.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018), by district" src="./../png/bangkok_ind_district_outpatients_hypertension.png">
        <figcaption>Hypertension outpatients (2018), by district.         <a href="./../html/bangkok_ind_district_outpatients_hypertension.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_hypertension.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018), by district




Hypertension outpatients (2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for hypertension were summed across each analysis area.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_hypertension_rate_area.png">
        <figcaption>Hypertension outpatients (2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_hypertension_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_hypertension_rate_area.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018) per km², by district" src="./../png/bangkok_ind_district_outpatients_hypertension_rate_area.png">
        <figcaption>Hypertension outpatients (2018) per km², by district.         <a href="./../html/bangkok_ind_district_outpatients_hypertension_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_hypertension_rate_area.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018) per km², by district




Hypertension outpatients (2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for hypertension were summed across each analysis area.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_hypertension_rate_population.png">
        <figcaption>Hypertension outpatients (2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_hypertension_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_hypertension_rate_population.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_outpatients_hypertension_rate_population.png">
        <figcaption>Hypertension outpatients (2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_outpatients_hypertension_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_hypertension_rate_population.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018) per 10,000 population, by district




Hypertension outpatients (2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for hypertension were summed across each analysis area.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_hypertension_rate_household.png">
        <figcaption>Hypertension outpatients (2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_hypertension_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_hypertension_rate_household.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Hypertension outpatients (2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_outpatients_hypertension_rate_household.png">
        <figcaption>Hypertension outpatients (2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_outpatients_hypertension_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_hypertension_rate_household.png
       :width: 70%
       :align: center

       Hypertension outpatients (2018) per 10,000 household, by district




Mental and behavioural disorder outpatients (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for mental and behavioural disorders were summed across each analysis area.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_mental_health.png">
        <figcaption>Mental and behavioural disorder outpatients (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_mental_health.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_mental_health.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018), by district" src="./../png/bangkok_ind_district_outpatients_mental_health.png">
        <figcaption>Mental and behavioural disorder outpatients (2018), by district.         <a href="./../html/bangkok_ind_district_outpatients_mental_health.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_mental_health.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018), by district




Mental and behavioural disorder outpatients (2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for mental and behavioural disorders were summed across each analysis area.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_mental_health_rate_area.png">
        <figcaption>Mental and behavioural disorder outpatients (2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_mental_health_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_mental_health_rate_area.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018) per km², by district" src="./../png/bangkok_ind_district_outpatients_mental_health_rate_area.png">
        <figcaption>Mental and behavioural disorder outpatients (2018) per km², by district.         <a href="./../html/bangkok_ind_district_outpatients_mental_health_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_mental_health_rate_area.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018) per km², by district




Mental and behavioural disorder outpatients (2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for mental and behavioural disorders were summed across each analysis area.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_mental_health_rate_population.png">
        <figcaption>Mental and behavioural disorder outpatients (2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_mental_health_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_mental_health_rate_population.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_outpatients_mental_health_rate_population.png">
        <figcaption>Mental and behavioural disorder outpatients (2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_outpatients_mental_health_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_mental_health_rate_population.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018) per 10,000 population, by district




Mental and behavioural disorder outpatients (2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Outpatient numbers for mental and behavioural disorders were summed across each analysis area.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_outpatients_mental_health_rate_household.png">
        <figcaption>Mental and behavioural disorder outpatients (2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_outpatients_mental_health_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_outpatients_mental_health_rate_household.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Mental and behavioural disorder outpatients (2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_outpatients_mental_health_rate_household.png">
        <figcaption>Mental and behavioural disorder outpatients (2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_outpatients_mental_health_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_outpatients_mental_health_rate_household.png
       :width: 70%
       :align: center

       Mental and behavioural disorder outpatients (2018) per 10,000 household, by district




Relaxing areas
~~~~~~~~~~~~~~


Fraction of Vegetation Cover
----------------------------

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

**Data location relative to project folder**: ./data/International/EC-JRC/Copernicus/subset_0_of_c_gls_FCOVER-RT6_201812200000_GLOBE_PROBAV_V2.tif


Vegetation Percent (Copernicus, 2018; mean)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The estimated percentage of vegetation cover within each analysis area was calculated by first scaling the raster grid cell values by 100/250 ( a scale factor of 0.4) and then taking the mean (average) of all intersecting grid cells.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (Copernicus, 2018; mean), by subdistrict" src="./../png/bangkok_ind_subdistrict_vegetation_pct_mean.png">
        <figcaption>Vegetation Percent (Copernicus, 2018; mean), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vegetation_pct_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_pct_mean.png
       :width: 70%
       :align: center

       Vegetation Percent (Copernicus, 2018; mean), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (Copernicus, 2018; mean), by district" src="./../png/bangkok_ind_district_vegetation_pct_mean.png">
        <figcaption>Vegetation Percent (Copernicus, 2018; mean), by district.         <a href="./../html/bangkok_ind_district_vegetation_pct_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_pct_mean.png
       :width: 70%
       :align: center

       Vegetation Percent (Copernicus, 2018; mean), by district




Vegetation Percent (Copernicus, 2018; standard deviation)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The estimated standard deviation of percentage of vegetation cover within each analysis area was calculated by first scaling the raster grid cell values by 100/250 ( a scale factor of 0.4) and then taking the standard deviation of all intersecting grid cells.  This is a measure of the degree to wich estimates vary across a particular area, and is a useful contextual measure to accompany the average vegetation percent for the area.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (Copernicus, 2018; standard deviation), by subdistrict" src="./../png/bangkok_ind_subdistrict_vegetation_pct_sd.png">
        <figcaption>Vegetation Percent (Copernicus, 2018; standard deviation), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vegetation_pct_sd.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_pct_sd.png
       :width: 70%
       :align: center

       Vegetation Percent (Copernicus, 2018; standard deviation), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (Copernicus, 2018; standard deviation), by district" src="./../png/bangkok_ind_district_vegetation_pct_sd.png">
        <figcaption>Vegetation Percent (Copernicus, 2018; standard deviation), by district.         <a href="./../html/bangkok_ind_district_vegetation_pct_sd.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_pct_sd.png
       :width: 70%
       :align: center

       Vegetation Percent (Copernicus, 2018; standard deviation), by district




Social condition
~~~~~~~~~~~~~~~~


Food entrepreneurs
------------------

Data comprising counts of restaurants, supermarkets, minimarts, stalls and markets for each district were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: BMA

**Publication year**: 2019

**Target year**: 2018

**Acquisition date (yyyymmdd)**: 20190820

**Licence**: none specified

**Date type**: integer

**Scale / Resolution**: area summary

**Data location relative to project folder**: ./data/Thai/_from BMA/20190820/transfer_1682928_files_504fdeaf/Num of food entrepreneur in Bangkok 2019 -kn15819.xlsx


Number of markets (BMA, 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (BMA, 2019), by district" src="./../png/bangkok_ind_district_markets.png">
        <figcaption>Number of markets (BMA, 2019), by district.         <a href="./../html/bangkok_ind_district_markets.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets.png
       :width: 70%
       :align: center

       Number of markets (BMA, 2019), by district




Number of markets (BMA, 2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (BMA, 2019) per km², by district" src="./../png/bangkok_ind_district_markets_rate_area.png">
        <figcaption>Number of markets (BMA, 2019) per km², by district.         <a href="./../html/bangkok_ind_district_markets_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_rate_area.png
       :width: 70%
       :align: center

       Number of markets (BMA, 2019) per km², by district




Number of markets (BMA, 2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (BMA, 2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_markets_rate_population.png">
        <figcaption>Number of markets (BMA, 2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_markets_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_rate_population.png
       :width: 70%
       :align: center

       Number of markets (BMA, 2019) per 10,000 population, by district




Number of markets (BMA, 2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (BMA, 2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_markets_rate_household.png">
        <figcaption>Number of markets (BMA, 2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_markets_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_rate_household.png
       :width: 70%
       :align: center

       Number of markets (BMA, 2019) per 10,000 household, by district




Number of minimarts (BMA, 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (BMA, 2019), by district" src="./../png/bangkok_ind_district_minimarts.png">
        <figcaption>Number of minimarts (BMA, 2019), by district.         <a href="./../html/bangkok_ind_district_minimarts.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts.png
       :width: 70%
       :align: center

       Number of minimarts (BMA, 2019), by district




Number of minimarts (BMA, 2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (BMA, 2019) per km², by district" src="./../png/bangkok_ind_district_minimarts_rate_area.png">
        <figcaption>Number of minimarts (BMA, 2019) per km², by district.         <a href="./../html/bangkok_ind_district_minimarts_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_rate_area.png
       :width: 70%
       :align: center

       Number of minimarts (BMA, 2019) per km², by district




Number of minimarts (BMA, 2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (BMA, 2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_minimarts_rate_population.png">
        <figcaption>Number of minimarts (BMA, 2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_minimarts_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_rate_population.png
       :width: 70%
       :align: center

       Number of minimarts (BMA, 2019) per 10,000 population, by district




Number of minimarts (BMA, 2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (BMA, 2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_minimarts_rate_household.png">
        <figcaption>Number of minimarts (BMA, 2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_minimarts_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_rate_household.png
       :width: 70%
       :align: center

       Number of minimarts (BMA, 2019) per 10,000 household, by district




Number of restaurants (BMA, 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (BMA, 2019), by district" src="./../png/bangkok_ind_district_restaurants.png">
        <figcaption>Number of restaurants (BMA, 2019), by district.         <a href="./../html/bangkok_ind_district_restaurants.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants.png
       :width: 70%
       :align: center

       Number of restaurants (BMA, 2019), by district




Number of restaurants (BMA, 2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (BMA, 2019) per km², by district" src="./../png/bangkok_ind_district_restaurants_rate_area.png">
        <figcaption>Number of restaurants (BMA, 2019) per km², by district.         <a href="./../html/bangkok_ind_district_restaurants_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_rate_area.png
       :width: 70%
       :align: center

       Number of restaurants (BMA, 2019) per km², by district




Number of restaurants (BMA, 2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (BMA, 2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_restaurants_rate_population.png">
        <figcaption>Number of restaurants (BMA, 2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_restaurants_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_rate_population.png
       :width: 70%
       :align: center

       Number of restaurants (BMA, 2019) per 10,000 population, by district




Number of restaurants (BMA, 2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (BMA, 2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_restaurants_rate_household.png">
        <figcaption>Number of restaurants (BMA, 2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_restaurants_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_rate_household.png
       :width: 70%
       :align: center

       Number of restaurants (BMA, 2019) per 10,000 household, by district




Number of stalls (BMA, 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (BMA, 2019), by district" src="./../png/bangkok_ind_district_stalls.png">
        <figcaption>Number of stalls (BMA, 2019), by district.         <a href="./../html/bangkok_ind_district_stalls.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls.png
       :width: 70%
       :align: center

       Number of stalls (BMA, 2019), by district




Number of stalls (BMA, 2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (BMA, 2019) per km², by district" src="./../png/bangkok_ind_district_stalls_rate_area.png">
        <figcaption>Number of stalls (BMA, 2019) per km², by district.         <a href="./../html/bangkok_ind_district_stalls_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_rate_area.png
       :width: 70%
       :align: center

       Number of stalls (BMA, 2019) per km², by district




Number of stalls (BMA, 2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (BMA, 2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_stalls_rate_population.png">
        <figcaption>Number of stalls (BMA, 2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_stalls_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_rate_population.png
       :width: 70%
       :align: center

       Number of stalls (BMA, 2019) per 10,000 population, by district




Number of stalls (BMA, 2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (BMA, 2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_stalls_rate_household.png">
        <figcaption>Number of stalls (BMA, 2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_stalls_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_rate_household.png
       :width: 70%
       :align: center

       Number of stalls (BMA, 2019) per 10,000 household, by district




Number of supermarkets (BMA, 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (BMA, 2019), by district" src="./../png/bangkok_ind_district_supermarkets.png">
        <figcaption>Number of supermarkets (BMA, 2019), by district.         <a href="./../html/bangkok_ind_district_supermarkets.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets.png
       :width: 70%
       :align: center

       Number of supermarkets (BMA, 2019), by district




Number of supermarkets (BMA, 2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (BMA, 2019) per km², by district" src="./../png/bangkok_ind_district_supermarkets_rate_area.png">
        <figcaption>Number of supermarkets (BMA, 2019) per km², by district.         <a href="./../html/bangkok_ind_district_supermarkets_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_rate_area.png
       :width: 70%
       :align: center

       Number of supermarkets (BMA, 2019) per km², by district




Number of supermarkets (BMA, 2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (BMA, 2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_supermarkets_rate_population.png">
        <figcaption>Number of supermarkets (BMA, 2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_supermarkets_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_rate_population.png
       :width: 70%
       :align: center

       Number of supermarkets (BMA, 2019) per 10,000 population, by district




Number of supermarkets (BMA, 2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (BMA, 2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_supermarkets_rate_household.png">
        <figcaption>Number of supermarkets (BMA, 2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_supermarkets_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_rate_household.png
       :width: 70%
       :align: center

       Number of supermarkets (BMA, 2019) per 10,000 household, by district



