

Study region boundaries
~~~~~~~~~~~~~~~~~~~~~~~


data
||||

Bangkok subdistrict boundary data (BMA, 2019) were topologically corrected using GRASS and QGIS, to ensure polygon boundaries did not have gaps or overlaps.  Boundaries were matched with alternate spellings in both Thai and English for corresponding regions found in data from other organisations  and datasets  (e.g. NSO, HDX) in order to facilitate data linkage.   The final boundary layer was returned to BMA and agreed upon for usage. 

**Data source**: ``BangkokGIS (BMA)``

**URL**: ``http://www.bangkokgis.com/bangkokgis_2008/userfiles/files/download/shapefile/administration/BMASubDistrict_Polygon.rar``

**Publication year**: ``2018``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190725``

**Licence**: ``none specified``

**Spatial reference (EPSG code)**: ``32647.0``

**Date type**: ``vector``

**Scale / Resolution**: ``subdistrict``

**Notes**: ``English names not provided; these have been derived using manual linkage with data from HDX subdistricts and population data provided by BMA, with verification from Kornsupha Nitvimol of BMA.``

**Data location relative to project folder**: ``./data/Bangkok_subdistricts_BMA_HLC_derived_20190805_cleaned_final.gpkg:subdistricts``

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


data
||||

Population statistics targetting Bangkok in 2018 were received from the Bangkok Metropolitan Administration, indexed by subdistrict. Fields included total population, sex strata, household, number of communities, and population in communities.  

**Data source**: ``BMA``

**URL**: ``http://www.bangkok.go.th``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190805``

**Licence**: ``none specified``

**Scale / Resolution**: ``subdistrict``

**Notes**: ``Derived population layer based on data received from Korn Nitviminol (BMA) via e-mail on 5 August 2019``

**Data location relative to project folder**: ``./data/Bangkok_subdistrict_population_BMA_HLC_derived_20190808.csv``

Population data were linked with boundaries using corresponding subdistrict ID numbers.  Density measures were calculated using population statistics relative to analysis area size. 


Population per km²
------------------





.. only:: html

    .. raw:: html

        <figure>
        <img alt="Population per km², by district" src="./../png/<class 'map'>.png">
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
        <img alt="Population per km², by subdistrict" src="./../png/<class 'map'>.png">
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
        <img alt="Households per km², by district" src="./../png/<class 'map'>.png">
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
        <img alt="Households per km², by subdistrict" src="./../png/<class 'map'>.png">
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
        <img alt="Communities per km², by district" src="./../png/<class 'map'>.png">
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
        <img alt="Communities per km², by subdistrict" src="./../png/<class 'map'>.png">
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
        <img alt="Population in communities per km², by district" src="./../png/<class 'map'>.png">
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
        <img alt="Population in communities per km², by subdistrict" src="./../png/<class 'map'>.png">
        <figcaption>Population in communities per km², by subdistrict.         <a href="./../html/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.html" target="_blank">Click to open interactive map in new tab.</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_02_population_subdistrict_population_in_communities_per_sqkm.png
       :width: 70%
       :align: center

       Population in communities per km², by subdistrict




City problems impacting health and wellbeing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Water quality/pollution
|||||||||||||||||||||||

คุณภาพน้ำ/มลพิษทางน้ำ

Water quality refers to the physical, chemical, biological and sensory properties (for example, taste) of water. Water pollution means the presence of toxic chemicals in groundwater and biological substances in excess of what is found in natural water and which may pose a threat to human health and / or the environment.


Dataset: Canal water quality
----------------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  The data comprised sample point records of canal water quality for 130 canals where Dissolved Oxygen (DO) less than 2 amount 130 canals (224 storage points).  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of Drainage and Sewerage, BMA``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190617``

**Licence**: ``none specified``

**Date type**: ``float``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190617/canal water quality 2018_final.xlsx``


Canal water storage DO (mg/L; 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average milligrams of dissolved oxygen per litre (DO mg/L) recorded at sample points within each analysis area was recorded.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage DO (mg/L; 2018), by district" src="./../png/bangkok_ind_district_water_quality_do.png">
        <figcaption>Canal water storage DO (mg/L; 2018), by district.         <a href="./../html/bangkok_ind_district_water_quality_do.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_do.png
       :width: 70%
       :align: center

       Canal water storage DO (mg/L; 2018), by district




Canal water storage BOD (mg/L; 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average milligrams of biochemical oxygen demand  per litre (BOD mg/L) recorded at sample points within each analysis area was recorded.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage BOD (mg/L; 2018), by district" src="./../png/bangkok_ind_district_water_quality_bod.png">
        <figcaption>Canal water storage BOD (mg/L; 2018), by district.         <a href="./../html/bangkok_ind_district_water_quality_bod.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_bod.png
       :width: 70%
       :align: center

       Canal water storage BOD (mg/L; 2018), by district




Canal water storage sample locations, 2018
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage sample locations, 2018, by district" src="./../png/bangkok_ind_district_water_quality_canals_poor.png">
        <figcaption>Canal water storage sample locations, 2018, by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor.png
       :width: 70%
       :align: center

       Canal water storage sample locations, 2018, by district




Canal water storage sample locations, 2018 per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage sample locations, 2018 per km², by district" src="./../png/bangkok_ind_district_water_quality_canals_poor_rate_area.png">
        <figcaption>Canal water storage sample locations, 2018 per km², by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor_rate_area.png
       :width: 70%
       :align: center

       Canal water storage sample locations, 2018 per km², by district




Canal water storage sample locations, 2018 per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage sample locations, 2018 per 10,000 population, by district" src="./../png/bangkok_ind_district_water_quality_canals_poor_rate_population.png">
        <figcaption>Canal water storage sample locations, 2018 per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor_rate_population.png
       :width: 70%
       :align: center

       Canal water storage sample locations, 2018 per 10,000 population, by district




Canal water storage sample locations, 2018 per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of sample points with poor water quality (< 2 DO mg/L) was recorded for each analysis area.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage sample locations, 2018 per 10,000 household, by district" src="./../png/bangkok_ind_district_water_quality_canals_poor_rate_household.png">
        <figcaption>Canal water storage sample locations, 2018 per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_water_quality_canals_poor_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_canals_poor_rate_household.png
       :width: 70%
       :align: center

       Canal water storage sample locations, 2018 per 10,000 household, by district




Canal water storage BOD < 6 mg/L (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The percentage of sample locations with  biochemical oxygen demand  less than 6  mg/L recorded within each analysis area was recorded.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Canal water storage BOD < 6 mg/L (2018), by district" src="./../png/bangkok_ind_district_water_quality_bod_less_than_6mg_l.png">
        <figcaption>Canal water storage BOD < 6 mg/L (2018), by district.         <a href="./../html/bangkok_ind_district_water_quality_bod_less_than_6mg_l.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_water_quality_bod_less_than_6mg_l.png
       :width: 70%
       :align: center

       Canal water storage BOD < 6 mg/L (2018), by district




Reduced/no car congestion
|||||||||||||||||||||||||

รถติดลดลง/ไม่มีรถติด

Traffic congestion is a condition that slows down transportation speed, resulting in longer travel times and increased occurances of stationary vehicles on long roads 


Dataset: Traffic jam
--------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``BMA, sourced from  https://www.grandprix.co.th/10 , opened 25 September 2019``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190930``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190930/transfer_1730651_files_296a713c/9 main Roads of Traffic Jam in Bangkok year 2018 by district and road _kn20190925.xlsx``


Number of main road of traffic jams (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road traffic jams associated with each analysis area was recorded.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of main road of traffic jams (2018), by district" src="./../png/bangkok_ind_district_main_road_traffic_jam.png">
        <figcaption>Number of main road of traffic jams (2018), by district.         <a href="./../html/bangkok_ind_district_main_road_traffic_jam.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_traffic_jam.png
       :width: 70%
       :align: center

       Number of main road of traffic jams (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Number of main road of traffic jam by district  by population src="./../svg/plots/district_main_road_traffic_jam_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Number of main road of traffic jam by district  by population per sqkm src="./../svg/plots/district_main_road_traffic_jam_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Number of main road of traffic jam by district , ranked in ascending order src="./../svg/plots/district_main_road_traffic_jam.svg">
            </div>
       <figcaption>Figures for Number Of Main Road Of Traffic Jams (2018) with regard to Number of main road of traffic jam by district  by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_traffic_jam_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of main road of traffic jam by district  by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_traffic_jam_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of main road of traffic jam by district  by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_traffic_jam.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by number of main road of traffic jam by district  with regard to number of main road of traffic jams (2018).




Zero waste
||||||||||

ไม่มีขยะ/ขยะเป็นศูนย์

Garbage (waste) means unwanted or unusable materials or any substances that are discarded after first use or unable to be reused and may be considered to be a co-product that has little economic value.  Waste is divided into 5 categories which are liquid waste, solid waste, organic waste, recyclable waste and hazardous waste.


Dataset: Solid waste
--------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of Environment, BMA``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190911``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190911/transfer_1710171_files_127133c5/solid waste in Bangkok -kn08242019.xlsx``


Annual solid waste (tonnes, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The amount of solid waste (tonnes) taken to waste transfer stations during 2018 was recorded for each district.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Annual solid waste (tonnes, 2018), by district" src="./../png/bangkok_ind_district_annual_solid_waste_tonnes.png">
        <figcaption>Annual solid waste (tonnes, 2018), by district.         <a href="./../html/bangkok_ind_district_annual_solid_waste_tonnes.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_annual_solid_waste_tonnes.png
       :width: 70%
       :align: center

       Annual solid waste (tonnes, 2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=annual solid waste (tonnes) by population src="./../svg/plots/district_annual_solid_waste_tonnes_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=annual solid waste (tonnes) by population per sqkm src="./../svg/plots/district_annual_solid_waste_tonnes_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=annual solid waste (tonnes), ranked in ascending order src="./../svg/plots/district_annual_solid_waste_tonnes.svg">
            </div>
       <figcaption>Figures for Annual Solid Waste (Tonnes, 2018) with regard to annual solid waste (tonnes) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_solid_waste_tonnes_population.pdf
      :width: 48%
      :align: center

      Scatterplot of annual solid waste (tonnes) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_solid_waste_tonnes_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of annual solid waste (tonnes) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_solid_waste_tonnes.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by annual solid waste (tonnes) with regard to annual solid waste (tonnes, 2018).




Annual recyclable waste (tonnes, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The amount of recyclable waste (waste that is managed by recycling; tonnes) taken to waste transfer stations during 2018 was recorded for each district.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Annual recyclable waste (tonnes, 2018), by district" src="./../png/bangkok_ind_district_annual_recyclable_waste_tonnes.png">
        <figcaption>Annual recyclable waste (tonnes, 2018), by district.         <a href="./../html/bangkok_ind_district_annual_recyclable_waste_tonnes.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_annual_recyclable_waste_tonnes.png
       :width: 70%
       :align: center

       Annual recyclable waste (tonnes, 2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=annual recyclable waste (tonnes) by population src="./../svg/plots/district_annual_recyclable_waste_tonnes_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=annual recyclable waste (tonnes) by population per sqkm src="./../svg/plots/district_annual_recyclable_waste_tonnes_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=annual recyclable waste (tonnes), ranked in ascending order src="./../svg/plots/district_annual_recyclable_waste_tonnes.svg">
            </div>
       <figcaption>Figures for Annual Recyclable Waste (Tonnes, 2018) with regard to annual recyclable waste (tonnes) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_recyclable_waste_tonnes_population.pdf
      :width: 48%
      :align: center

      Scatterplot of annual recyclable waste (tonnes) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_recyclable_waste_tonnes_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of annual recyclable waste (tonnes) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_recyclable_waste_tonnes.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by annual recyclable waste (tonnes) with regard to annual recyclable waste (tonnes, 2018).




Percentage recyclable waste (tonnes, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The percentage of total waste (solid and recyclable) taken to waste transfer stations during 2018  that was recyclable was recorded for each district.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage recyclable waste (tonnes, 2018), by district" src="./../png/bangkok_ind_district_percentage_recyclable_waste.png">
        <figcaption>Percentage recyclable waste (tonnes, 2018), by district.         <a href="./../html/bangkok_ind_district_percentage_recyclable_waste.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_percentage_recyclable_waste.png
       :width: 70%
       :align: center

       Percentage recyclable waste (tonnes, 2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=annual recyclable waste (tonnes) by population src="./../svg/plots/district_percentage_recyclable_waste_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=annual recyclable waste (tonnes) by population per sqkm src="./../svg/plots/district_percentage_recyclable_waste_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=annual recyclable waste (tonnes), ranked in ascending order src="./../svg/plots/district_percentage_recyclable_waste.svg">
            </div>
       <figcaption>Figures for Percentage Recyclable Waste (Tonnes, 2018) with regard to annual recyclable waste (tonnes) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percentage_recyclable_waste_population.pdf
      :width: 48%
      :align: center

      Scatterplot of annual recyclable waste (tonnes) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percentage_recyclable_waste_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of annual recyclable waste (tonnes) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percentage_recyclable_waste.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by annual recyclable waste (tonnes) with regard to percentage recyclable waste (tonnes, 2018).




Dataset: Hazardous waste
------------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of Environment, BMA``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190911``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20200507/Hazardous waste segregation 2018-kn81519pter.xlsx``


Annual hazardous waste (kg, 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The amount of hazardous waste segregation (kg) at waste transfer stations during 2018 was recorded for each district.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Annual hazardous waste (kg, 2018), by district" src="./../png/bangkok_ind_district_annual_hazardous_waste_kg.png">
        <figcaption>Annual hazardous waste (kg, 2018), by district.         <a href="./../html/bangkok_ind_district_annual_hazardous_waste_kg.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_annual_hazardous_waste_kg.png
       :width: 70%
       :align: center

       Annual hazardous waste (kg, 2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Hazardous waste segregation (kg)  by population src="./../svg/plots/district_annual_hazardous_waste_kg_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Hazardous waste segregation (kg)  by population per sqkm src="./../svg/plots/district_annual_hazardous_waste_kg_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Hazardous waste segregation (kg) , ranked in ascending order src="./../svg/plots/district_annual_hazardous_waste_kg.svg">
            </div>
       <figcaption>Figures for Annual Hazardous Waste (Kg, 2018) with regard to Hazardous waste segregation (kg)  by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_hazardous_waste_kg_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Hazardous waste segregation (kg)  by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_hazardous_waste_kg_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Hazardous waste segregation (kg)  by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_annual_hazardous_waste_kg.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by hazardous waste segregation (kg)  with regard to annual hazardous waste (kg, 2018).




Percentage hazardous waste (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The percentage of total waste (solid and hazardous) taken to waste transfer stations during 2018  that was hazardous was recorded for each district.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage hazardous waste (2018), by district" src="./../png/bangkok_ind_district_percentage_hazardous_waste.png">
        <figcaption>Percentage hazardous waste (2018), by district.         <a href="./../html/bangkok_ind_district_percentage_hazardous_waste.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_percentage_hazardous_waste.png
       :width: 70%
       :align: center

       Percentage hazardous waste (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Hazardous waste segregation (tonnes)  by population src="./../svg/plots/district_percentage_hazardous_waste_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Hazardous waste segregation (tonnes)  by population per sqkm src="./../svg/plots/district_percentage_hazardous_waste_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Hazardous waste segregation (tonnes) , ranked in ascending order src="./../svg/plots/district_percentage_hazardous_waste.svg">
            </div>
       <figcaption>Figures for Percentage Hazardous Waste (2018) with regard to Hazardous waste segregation (tonnes)  by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percentage_hazardous_waste_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Hazardous waste segregation (tonnes)  by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percentage_hazardous_waste_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Hazardous waste segregation (tonnes)  by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percentage_hazardous_waste.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by hazardous waste segregation (tonnes)  with regard to percentage hazardous waste (2018).




No flooding
|||||||||||

ไม่มีน้ำท่วม

Floods means large amounts of water overflowing into normal land.


Dataset: Flood risk
-------------------

Data at subdistrict level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of Drainage and Sewerage , BMA``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190809``

**Licence**: ``none specified``

**Date type**: ``float``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190809/transfer_1673010_files_4a5fe795/BKK indicator_flood_kn 63019.xlsx``


Main road flood area location count (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations.png">
        <figcaption>Main road flood area location count (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations.png
       :width: 70%
       :align: center

       Main road flood area location count (2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018), by district" src="./../png/bangkok_ind_district_main_road_flood_locations.png">
        <figcaption>Main road flood area location count (2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations.png
       :width: 70%
       :align: center

       Main road flood area location count (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=main road flood locations by population src="./../svg/plots/district_main_road_flood_locations_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=main road flood locations by population per sqkm src="./../svg/plots/district_main_road_flood_locations_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=main road flood locations, ranked in ascending order src="./../svg/plots/district_main_road_flood_locations.svg">
            </div>
       <figcaption>Figures for Main Road Flood Area Location Count (2018) with regard to main road flood locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_population.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by main road flood locations with regard to main road flood area location count (2018).




Main road flood area location count (2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations_rate_area.png">
        <figcaption>Main road flood area location count (2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations_rate_area.png
       :width: 70%
       :align: center

       Main road flood area location count (2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018) per km², by district" src="./../png/bangkok_ind_district_main_road_flood_locations_rate_area.png">
        <figcaption>Main road flood area location count (2018) per km², by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations_rate_area.png
       :width: 70%
       :align: center

       Main road flood area location count (2018) per km², by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=main road flood locations by population src="./../svg/plots/district_main_road_flood_locations_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=main road flood locations by population per sqkm src="./../svg/plots/district_main_road_flood_locations_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=main road flood locations, ranked in ascending order src="./../svg/plots/district_main_road_flood_locations_rate_area.svg">
            </div>
       <figcaption>Figures for Main Road Flood Area Location Count (2018) Per Km² with regard to main road flood locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by main road flood locations with regard to main road flood area location count (2018) per km².




Main road flood area location count (2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations_rate_population.png">
        <figcaption>Main road flood area location count (2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations_rate_population.png
       :width: 70%
       :align: center

       Main road flood area location count (2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_main_road_flood_locations_rate_population.png">
        <figcaption>Main road flood area location count (2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations_rate_population.png
       :width: 70%
       :align: center

       Main road flood area location count (2018) per 10,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=main road flood locations by population src="./../svg/plots/district_main_road_flood_locations_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=main road flood locations by population per sqkm src="./../svg/plots/district_main_road_flood_locations_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=main road flood locations, ranked in ascending order src="./../svg/plots/district_main_road_flood_locations_rate_population.svg">
            </div>
       <figcaption>Figures for Main Road Flood Area Location Count (2018) Per 10,000 Population with regard to main road flood locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by main road flood locations with regard to main road flood area location count (2018) per 10,000 population.




Main road flood area location count (2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of main road flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_locations_rate_household.png">
        <figcaption>Main road flood area location count (2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_locations_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_locations_rate_household.png
       :width: 70%
       :align: center

       Main road flood area location count (2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Main road flood area location count (2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_main_road_flood_locations_rate_household.png">
        <figcaption>Main road flood area location count (2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_main_road_flood_locations_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_locations_rate_household.png
       :width: 70%
       :align: center

       Main road flood area location count (2018) per 10,000 household, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=main road flood locations by population src="./../svg/plots/district_main_road_flood_locations_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=main road flood locations by population per sqkm src="./../svg/plots/district_main_road_flood_locations_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=main road flood locations, ranked in ascending order src="./../svg/plots/district_main_road_flood_locations_rate_household.svg">
            </div>
       <figcaption>Figures for Main Road Flood Area Location Count (2018) Per 10,000 Household with regard to main road flood locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of main road flood locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_locations_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by main road flood locations with regard to main road flood area location count (2018) per 10,000 household.




Average days of rain (main road flood areas;  2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average number of days of rain recorded for 14 main road flood areas was taken for each analysis area.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of rain (main road flood areas;  2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_days_rain.png">
        <figcaption>Average days of rain (main road flood areas;  2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_days_rain.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_days_rain.png
       :width: 70%
       :align: center

       Average days of rain (main road flood areas;  2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of rain (main road flood areas;  2018), by district" src="./../png/bangkok_ind_district_main_road_flood_days_rain.png">
        <figcaption>Average days of rain (main road flood areas;  2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_days_rain.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_days_rain.png
       :width: 70%
       :align: center

       Average days of rain (main road flood areas;  2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=days of rain by population src="./../svg/plots/district_main_road_flood_days_rain_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=days of rain by population per sqkm src="./../svg/plots/district_main_road_flood_days_rain_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=days of rain, ranked in ascending order src="./../svg/plots/district_main_road_flood_days_rain.svg">
            </div>
       <figcaption>Figures for Average Days Of Rain (Main Road Flood Areas;  2018) with regard to days of rain by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_days_rain_population.pdf
      :width: 48%
      :align: center

      Scatterplot of days of rain by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_days_rain_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of days of rain by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_days_rain.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by days of rain with regard to average days of rain (main road flood areas;  2018).




Average maximum intensity (main road flood areas;  2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average maximum intensity recorded for 14 main road flood areas was taken for each analysis area.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average maximum intensity (main road flood areas;  2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_intensity.png">
        <figcaption>Average maximum intensity (main road flood areas;  2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_intensity.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_intensity.png
       :width: 70%
       :align: center

       Average maximum intensity (main road flood areas;  2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average maximum intensity (main road flood areas;  2018), by district" src="./../png/bangkok_ind_district_main_road_flood_intensity.png">
        <figcaption>Average maximum intensity (main road flood areas;  2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_intensity.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_intensity.png
       :width: 70%
       :align: center

       Average maximum intensity (main road flood areas;  2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=maximum intensity by population src="./../svg/plots/district_main_road_flood_intensity_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=maximum intensity by population per sqkm src="./../svg/plots/district_main_road_flood_intensity_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=maximum intensity, ranked in ascending order src="./../svg/plots/district_main_road_flood_intensity.svg">
            </div>
       <figcaption>Figures for Average Maximum Intensity (Main Road Flood Areas;  2018) with regard to maximum intensity by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_intensity_population.pdf
      :width: 48%
      :align: center

      Scatterplot of maximum intensity by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_intensity_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of maximum intensity by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_intensity.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by maximum intensity with regard to average maximum intensity (main road flood areas;  2018).




Average days of flooding  (main road flood areas;  2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average number of days of flooding recorded for 14 main road flood areas was taken for each analysis area.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of flooding  (main road flood areas;  2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_main_road_flood_days_flood.png">
        <figcaption>Average days of flooding  (main road flood areas;  2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_main_road_flood_days_flood.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_main_road_flood_days_flood.png
       :width: 70%
       :align: center

       Average days of flooding  (main road flood areas;  2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average days of flooding  (main road flood areas;  2018), by district" src="./../png/bangkok_ind_district_main_road_flood_days_flood.png">
        <figcaption>Average days of flooding  (main road flood areas;  2018), by district.         <a href="./../html/bangkok_ind_district_main_road_flood_days_flood.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_main_road_flood_days_flood.png
       :width: 70%
       :align: center

       Average days of flooding  (main road flood areas;  2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=days of flooding by population src="./../svg/plots/district_main_road_flood_days_flood_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=days of flooding by population per sqkm src="./../svg/plots/district_main_road_flood_days_flood_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=days of flooding, ranked in ascending order src="./../svg/plots/district_main_road_flood_days_flood.svg">
            </div>
       <figcaption>Figures for Average Days Of Flooding  (Main Road Flood Areas;  2018) with regard to days of flooding by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_days_flood_population.pdf
      :width: 48%
      :align: center

      Scatterplot of days of flooding by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_days_flood_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of days of flooding by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_main_road_flood_days_flood.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by days of flooding with regard to average days of flooding  (main road flood areas;  2018).




Vulnerable flood area count (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas.png">
        <figcaption>Vulnerable flood area count (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018), by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas.png">
        <figcaption>Vulnerable flood area count (2018), by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=flood risk locations by population src="./../svg/plots/district_vulnerable_flood_areas_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=flood risk locations by population per sqkm src="./../svg/plots/district_vulnerable_flood_areas_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=flood risk locations, ranked in ascending order src="./../svg/plots/district_vulnerable_flood_areas.svg">
            </div>
       <figcaption>Figures for Vulnerable Flood Area Count (2018) with regard to flood risk locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_population.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by flood risk locations with regard to vulnerable flood area count (2018).




Vulnerable flood area count (2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_area.png">
        <figcaption>Vulnerable flood area count (2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_area.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018) per km², by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas_rate_area.png">
        <figcaption>Vulnerable flood area count (2018) per km², by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas_rate_area.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018) per km², by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=flood risk locations by population src="./../svg/plots/district_vulnerable_flood_areas_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=flood risk locations by population per sqkm src="./../svg/plots/district_vulnerable_flood_areas_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=flood risk locations, ranked in ascending order src="./../svg/plots/district_vulnerable_flood_areas_rate_area.svg">
            </div>
       <figcaption>Figures for Vulnerable Flood Area Count (2018) Per Km² with regard to flood risk locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by flood risk locations with regard to vulnerable flood area count (2018) per km².




Vulnerable flood area count (2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_population.png">
        <figcaption>Vulnerable flood area count (2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_population.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas_rate_population.png">
        <figcaption>Vulnerable flood area count (2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas_rate_population.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018) per 10,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=flood risk locations by population src="./../svg/plots/district_vulnerable_flood_areas_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=flood risk locations by population per sqkm src="./../svg/plots/district_vulnerable_flood_areas_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=flood risk locations, ranked in ascending order src="./../svg/plots/district_vulnerable_flood_areas_rate_population.svg">
            </div>
       <figcaption>Figures for Vulnerable Flood Area Count (2018) Per 10,000 Population with regard to flood risk locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by flood risk locations with regard to vulnerable flood area count (2018) per 10,000 population.




Vulnerable flood area count (2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of vulnerable flood areas associated with each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_household.png">
        <figcaption>Vulnerable flood area count (2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vulnerable_flood_areas_rate_household.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vulnerable flood area count (2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_vulnerable_flood_areas_rate_household.png">
        <figcaption>Vulnerable flood area count (2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_vulnerable_flood_areas_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vulnerable_flood_areas_rate_household.png
       :width: 70%
       :align: center

       Vulnerable flood area count (2018) per 10,000 household, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=flood risk locations by population src="./../svg/plots/district_vulnerable_flood_areas_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=flood risk locations by population per sqkm src="./../svg/plots/district_vulnerable_flood_areas_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=flood risk locations, ranked in ascending order src="./../svg/plots/district_vulnerable_flood_areas_rate_household.svg">
            </div>
       <figcaption>Figures for Vulnerable Flood Area Count (2018) Per 10,000 Household with regard to flood risk locations by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of flood risk locations by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vulnerable_flood_areas_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by flood risk locations with regard to vulnerable flood area count (2018) per 10,000 household.




High quality air
||||||||||||||||

อากาศคุณภาพสูง

Air quality refers to the weather conditions within the area around us. High air quality is at a level that is clean, clear and free from pollution such as smoke, dust, gas etc.  Human health, plants, animals and natural resources are threatened when air pollution reaches a high concentration.  Poor air quality affects or is harmful to human health and / or the environment.


Dataset: Air quality: PM2.5
---------------------------

Data from monitoring stations were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with IDs for districts containing the monitoring stations.  Point locations for monitoring stations were acquired from monitoring station geojson data retrieved from http://air4thai.pcd.go.th and aligned with the supplied data.

**Data source**: ``From article (Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019) citing data sourced from Thai Pollution Control Department websites http://air4thai.pcd.go.th and http://aqmthai.com/public_report.php``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190809``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Citation**: ``Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019``

**Notes**: ``From article (Thara Bua Kham Si. 2019.  How many days does Bangkok people live in polluted air, toxic PM2.5 dust? Greenpeace.  January 2019. https://www.greenpeace.org/thailand/story/2122/people-living-with-air-pollution/ accessed 6 July 2019) citing data sourced from Thai Pollution Control Department websites http://air4thai.pcd.go.th and http://aqmthai.com/public_report.php``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190809/transfer_1673010_files_4a5fe795/air quality in Bangkok 2019 kn 7719.xlsx``


Air quality monitoring stations (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Air quality monitoring stations (2019), by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations.png">
        <figcaption>Air quality monitoring stations (2019), by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations.png
       :width: 70%
       :align: center

       Air quality monitoring stations (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=stationID by population src="./../svg/plots/district_pcd_monitoring_stations_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=stationID by population per sqkm src="./../svg/plots/district_pcd_monitoring_stations_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=stationID, ranked in ascending order src="./../svg/plots/district_pcd_monitoring_stations.svg">
            </div>
       <figcaption>Figures for Air Quality Monitoring Stations (2019) with regard to stationID by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_population.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by stationid with regard to air quality monitoring stations (2019).




Air quality monitoring stations (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Air quality monitoring stations (2019) per km², by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations_rate_area.png">
        <figcaption>Air quality monitoring stations (2019) per km², by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations_rate_area.png
       :width: 70%
       :align: center

       Air quality monitoring stations (2019) per km², by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=stationID by population src="./../svg/plots/district_pcd_monitoring_stations_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=stationID by population per sqkm src="./../svg/plots/district_pcd_monitoring_stations_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=stationID, ranked in ascending order src="./../svg/plots/district_pcd_monitoring_stations_rate_area.svg">
            </div>
       <figcaption>Figures for Air Quality Monitoring Stations (2019) Per Km² with regard to stationID by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by stationid with regard to air quality monitoring stations (2019) per km².




Air quality monitoring stations (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Air quality monitoring stations (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations_rate_population.png">
        <figcaption>Air quality monitoring stations (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations_rate_population.png
       :width: 70%
       :align: center

       Air quality monitoring stations (2019) per 10,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=stationID by population src="./../svg/plots/district_pcd_monitoring_stations_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=stationID by population per sqkm src="./../svg/plots/district_pcd_monitoring_stations_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=stationID, ranked in ascending order src="./../svg/plots/district_pcd_monitoring_stations_rate_population.svg">
            </div>
       <figcaption>Figures for Air Quality Monitoring Stations (2019) Per 10,000 Population with regard to stationID by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by stationid with regard to air quality monitoring stations (2019) per 10,000 population.




Air quality monitoring stations (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of monitoring stations in each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 7, 11, 2, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Air quality monitoring stations (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_pcd_monitoring_stations_rate_household.png">
        <figcaption>Air quality monitoring stations (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_pcd_monitoring_stations_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_pcd_monitoring_stations_rate_household.png
       :width: 70%
       :align: center

       Air quality monitoring stations (2019) per 10,000 household, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=stationID by population src="./../svg/plots/district_pcd_monitoring_stations_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=stationID by population per sqkm src="./../svg/plots/district_pcd_monitoring_stations_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=stationID, ranked in ascending order src="./../svg/plots/district_pcd_monitoring_stations_rate_household.svg">
            </div>
       <figcaption>Figures for Air Quality Monitoring Stations (2019) Per 10,000 Household with regard to stationID by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of stationID by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pcd_monitoring_stations_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by stationid with regard to air quality monitoring stations (2019) per 10,000 household.




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=days exceeding Thai standard (50 µg/m³; January 2019, PCD) by population src="./../svg/plots/district_pm2p5_days_exceeding_thai_standard_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=days exceeding Thai standard (50 µg/m³; January 2019, PCD) by population per sqkm src="./../svg/plots/district_pm2p5_days_exceeding_thai_standard_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=days exceeding Thai standard (50 µg/m³; January 2019, PCD), ranked in ascending order src="./../svg/plots/district_pm2p5_days_exceeding_thai_standard.svg">
            </div>
       <figcaption>Figures for Number Of Days Pm 2.5 Exceeds Thai Standard (50 Μg/M³; January 2019, Pcd) with regard to days exceeding Thai standard (50 µg/m³; January 2019, PCD) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pm2p5_days_exceeding_thai_standard_population.pdf
      :width: 48%
      :align: center

      Scatterplot of days exceeding Thai standard (50 µg/m³; January 2019, PCD) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pm2p5_days_exceeding_thai_standard_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of days exceeding Thai standard (50 µg/m³; January 2019, PCD) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pm2p5_days_exceeding_thai_standard.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by days exceeding thai standard (50 µg/m³; january 2019, pcd) with regard to number of days pm 2.5 exceeds thai standard (50 μg/m³; january 2019, pcd).




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=days exceeding WHO standard (25 µg/m³; January 2019, PCD) by population src="./../svg/plots/district_pm2p5_days_exceeding_who_standard_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=days exceeding WHO standard (25 µg/m³; January 2019, PCD) by population per sqkm src="./../svg/plots/district_pm2p5_days_exceeding_who_standard_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=days exceeding WHO standard (25 µg/m³; January 2019, PCD), ranked in ascending order src="./../svg/plots/district_pm2p5_days_exceeding_who_standard.svg">
            </div>
       <figcaption>Figures for Number Of Days Pm 2.5 Exceeds Who Standard (25 Μg/M³; January 2019, Pcd) with regard to days exceeding WHO standard (25 µg/m³; January 2019, PCD) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pm2p5_days_exceeding_who_standard_population.pdf
      :width: 48%
      :align: center

      Scatterplot of days exceeding WHO standard (25 µg/m³; January 2019, PCD) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pm2p5_days_exceeding_who_standard_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of days exceeding WHO standard (25 µg/m³; January 2019, PCD) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_pm2p5_days_exceeding_who_standard.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by days exceeding who standard (25 µg/m³; january 2019, pcd) with regard to number of days pm 2.5 exceeds who standard (25 μg/m³; january 2019, pcd).




Dataset: Sentinel-5P NRTI NO2: Near Real-Time Nitrogen Dioxide
--------------------------------------------------------------

Google Earth Engine was used to process Sentinel 5p data from the Copernicus satellite detailing total vertical column of NO2 (ratio of the slant column density of NO2 and the total air mass factor), taking the annual average from 13 October 2017 (commencement of the S5P monitoring mission) to 12 October 2018.  

**Data source**: ``Copernicus Sentinel Data processed using Google Earth Engine``

**URL**: ``https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S5P_NRTI_L3_NO2``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20191009``

**Licence**: ``Free, full and open access for lawful usage, with attribution``

**Licence URL**: ``https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice``

**Spatial reference (EPSG code)**: ``4326.0``

**Date type**: ``raster:float64``

**Scale / Resolution**: ``10``

**Notes**: ``Free access, but must acknowledge Copernicus Sentinel, year of data and if it has been modified.  Requires processing, as data is in half hourly updates.``

**Data location relative to project folder**: ``./data/International/Google EarthEngine/copernicus_s5p_nrti_l3_no2-mean_col_num_density_20171013_20181012.tif``


Annual average NO2 (1-e6 mmol/m²; 2017-18)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total vertical column of NO2 is a measure of air pollution, however it is based on tropospheric and stratospheric presence of NO2 and measured in mmol per square metre; in contrast, health guidelines for exposure are usually based on ground monitoring of NO2, recorded in parts per billion.  As a spatially continuous measure, annual average NO2 is useful for indicating areas of relatively intense pollution and may be compared with ground based measures (ie. from monitoring stations) as well as longitudinally to monitor change over time.  For mapping purposes, NO2 was scaled as 1-e6 mmol per square metre (ie. divided by 0.000001).






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Annual average NO2 (1-e6 mmol/m²; 2017-18), by subdistrict" src="./../png/bangkok_ind_subdistrict_no2_2017_18_mean.png">
        <figcaption>Annual average NO2 (1-e6 mmol/m²; 2017-18), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_no2_2017_18_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_no2_2017_18_mean.png
       :width: 70%
       :align: center

       Annual average NO2 (1-e6 mmol/m²; 2017-18), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Annual average NO2 (1-e6 mmol/m²; 2017-18), by district" src="./../png/bangkok_ind_district_no2_2017_18_mean.png">
        <figcaption>Annual average NO2 (1-e6 mmol/m²; 2017-18), by district.         <a href="./../html/bangkok_ind_district_no2_2017_18_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_no2_2017_18_mean.png
       :width: 70%
       :align: center

       Annual average NO2 (1-e6 mmol/m²; 2017-18), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Annual average NO2 (1-e6 mmol/m²; 2017-18) by population src="./../svg/plots/district_no2_2017_18_mean_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Annual average NO2 (1-e6 mmol/m²; 2017-18) by population per sqkm src="./../svg/plots/district_no2_2017_18_mean_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Annual average NO2 (1-e6 mmol/m²; 2017-18), ranked in ascending order src="./../svg/plots/district_no2_2017_18_mean.svg">
            </div>
       <figcaption>Figures for Annual Average No2 (1-E6 Mmol/M²; 2017-18) with regard to Annual average NO2 (1-e6 mmol/m²; 2017-18) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_no2_2017_18_mean_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Annual average NO2 (1-e6 mmol/m²; 2017-18) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_no2_2017_18_mean_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Annual average NO2 (1-e6 mmol/m²; 2017-18) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_no2_2017_18_mean.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by annual average no2 (1-e6 mmol/m²; 2017-18) with regard to annual average no2 (1-e6 mmol/m²; 2017-18).




A safe environment
||||||||||||||||||

สิ่งแวดล้อมปลอดภัย

Environmental safety in an urban context refers to minimisation of risk of fire, crime and road accidents. 


Dataset: Fire incidence
-----------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with IDs. 

**Data source**: ``Fire and Rescue Department, BMA``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190809``

**Licence**: ``none specified``

**Date type**: ``table``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190809/transfer_1673010_files_4a5fe795/Fire Incidence in Bangkok 2018_kn8919.xlsx``


Fire incidence (2018)
>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (2018), by district" src="./../png/bangkok_ind_district_fire_incidence.png">
        <figcaption>Fire incidence (2018), by district.         <a href="./../html/bangkok_ind_district_fire_incidence.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence.png
       :width: 70%
       :align: center

       Fire incidence (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=fire incidence by population src="./../svg/plots/district_fire_incidence_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=fire incidence by population per sqkm src="./../svg/plots/district_fire_incidence_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=fire incidence, ranked in ascending order src="./../svg/plots/district_fire_incidence.svg">
            </div>
       <figcaption>Figures for Fire Incidence (2018) with regard to fire incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_population.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by fire incidence with regard to fire incidence (2018).




Fire incidence (2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (2018) per km², by district" src="./../png/bangkok_ind_district_fire_incidence_rate_area.png">
        <figcaption>Fire incidence (2018) per km², by district.         <a href="./../html/bangkok_ind_district_fire_incidence_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence_rate_area.png
       :width: 70%
       :align: center

       Fire incidence (2018) per km², by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=fire incidence by population src="./../svg/plots/district_fire_incidence_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=fire incidence by population per sqkm src="./../svg/plots/district_fire_incidence_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=fire incidence, ranked in ascending order src="./../svg/plots/district_fire_incidence_rate_area.svg">
            </div>
       <figcaption>Figures for Fire Incidence (2018) Per Km² with regard to fire incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by fire incidence with regard to fire incidence (2018) per km².




Fire incidence (2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_fire_incidence_rate_population.png">
        <figcaption>Fire incidence (2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_fire_incidence_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence_rate_population.png
       :width: 70%
       :align: center

       Fire incidence (2018) per 10,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=fire incidence by population src="./../svg/plots/district_fire_incidence_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=fire incidence by population per sqkm src="./../svg/plots/district_fire_incidence_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=fire incidence, ranked in ascending order src="./../svg/plots/district_fire_incidence_rate_population.svg">
            </div>
       <figcaption>Figures for Fire Incidence (2018) Per 10,000 Population with regard to fire incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by fire incidence with regard to fire incidence (2018) per 10,000 population.




Fire incidence (2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of fire occurences recorded for each analysis area within 2018 was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Fire incidence (2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_fire_incidence_rate_household.png">
        <figcaption>Fire incidence (2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_fire_incidence_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_fire_incidence_rate_household.png
       :width: 70%
       :align: center

       Fire incidence (2018) per 10,000 household, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=fire incidence by population src="./../svg/plots/district_fire_incidence_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=fire incidence by population per sqkm src="./../svg/plots/district_fire_incidence_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=fire incidence, ranked in ascending order src="./../svg/plots/district_fire_incidence_rate_household.svg">
            </div>
       <figcaption>Figures for Fire Incidence (2018) Per 10,000 Household with regard to fire incidence by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of fire incidence by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_fire_incidence_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by fire incidence with regard to fire incidence (2018) per 10,000 household.




Dataset: Risk areas
-------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of City Law Enforcement, BMA``

**Publication year**: ``2019``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20200511``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Notes**: ``Only one district has 30 locations; most have below 20.  Perhaps 15 would be a more meaningful target to aspire to?  Alternately, number of reported incidents could be a more meaningful metric.``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20200511/Risk Areas _crime_ in Bangkok _improved_kn20200510.xlsx``


Number of locations with reported crime (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of crime locations reported within each district was recorded, and subsequently evaluated against a target threshold.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of locations with reported crime (2019), by district" src="./../png/bangkok_ind_district_crime_locations.png">
        <figcaption>Number of locations with reported crime (2019), by district.         <a href="./../html/bangkok_ind_district_crime_locations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_crime_locations.png
       :width: 70%
       :align: center

       Number of locations with reported crime (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Locations with reported crime by population src="./../svg/plots/district_crime_locations_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Locations with reported crime by population per sqkm src="./../svg/plots/district_crime_locations_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Locations with reported crime, ranked in ascending order src="./../svg/plots/district_crime_locations.svg">
            </div>
       <figcaption>Figures for Number Of Locations With Reported Crime (2019) with regard to Locations with reported crime by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_crime_locations_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Locations with reported crime by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_crime_locations_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Locations with reported crime by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_crime_locations.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by locations with reported crime with regard to number of locations with reported crime (2019).




Number of locations with reported road accidents (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of road accidents locations reported within each district was recorded, and subsequently evaluated against a target threshold.

Aligns with Sustainable Development Goals: 11, 13.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of locations with reported road accidents (2019), by district" src="./../png/bangkok_ind_district_road_accident_locations.png">
        <figcaption>Number of locations with reported road accidents (2019), by district.         <a href="./../html/bangkok_ind_district_road_accident_locations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_road_accident_locations.png
       :width: 70%
       :align: center

       Number of locations with reported road accidents (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Locations with reported road accidents by population src="./../svg/plots/district_road_accident_locations_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Locations with reported road accidents by population per sqkm src="./../svg/plots/district_road_accident_locations_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Locations with reported road accidents, ranked in ascending order src="./../svg/plots/district_road_accident_locations.svg">
            </div>
       <figcaption>Figures for Number Of Locations With Reported Road Accidents (2019) with regard to Locations with reported road accidents by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_road_accident_locations_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Locations with reported road accidents by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_road_accident_locations_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Locations with reported road accidents by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_road_accident_locations.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by locations with reported road accidents with regard to number of locations with reported road accidents (2019).




Health-promoting environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Green space, pocket parks
|||||||||||||||||||||||||

พื้นที่สีเขียว/สวนหย่อม

Public Parks and open spaces refer to official and unofficial land reserved for sports and recreation, preserving the natural environment and providing green space for urban flood management.  The development of green areas, gardens and open spaces can increase the value of land, for example by adding amenities to create happiness or enjoyment for the public, or promoting activities to strengthen family relationships within an area. Examples of such sites include botanical parks, sports fields, children's playgrounds, marshes with water sports / fishing / community swimming pools, camps, picnic activities for families, dog parks. 


Dataset: Green areas
--------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``BMA``

**Publication year**: ``2019``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20190930``

**Licence**: ``none specified``

**Licence URL**: ``Website 203.155.220.220/parks``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Notes**: ``Only two districts have 12 locations; perhaps <= 10 would be a more aspirational target.``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190930/transfer_1730651_files_296a713c/Green area in BKK by district 2019_kn20190923.xlsx``


Total public green area percent (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total area of green space reported within each district was recorded, and subsequently evaluated against target thresholds with regard to total area, and per capita.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Total public green area percent (2019), by district" src="./../png/bangkok_ind_district_green_space_public_percent.png">
        <figcaption>Total public green area percent (2019), by district.         <a href="./../html/bangkok_ind_district_green_space_public_percent.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_green_space_public_percent.png
       :width: 70%
       :align: center

       Total public green area percent (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Total public green space percent by population src="./../svg/plots/district_green_space_public_percent_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Total public green space percent by population per sqkm src="./../svg/plots/district_green_space_public_percent_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Total public green space percent, ranked in ascending order src="./../svg/plots/district_green_space_public_percent.svg">
            </div>
       <figcaption>Figures for Total Public Green Area Percent (2019) with regard to Total public green space percent by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_public_percent_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Total public green space percent by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_public_percent_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Total public green space percent by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_public_percent.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by total public green space percent with regard to total public green area percent (2019).







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Green space per capita (sqm) by population src="./../svg/plots/district_green_space_public_per_capita_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Green space per capita (sqm) by population per sqkm src="./../svg/plots/district_green_space_public_per_capita_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Green space per capita (sqm), ranked in ascending order src="./../svg/plots/district_green_space_public_per_capita.svg">
            </div>
       <figcaption>Figures for Total Public Green Area Per Capita (M²; 2019) with regard to Green space per capita (sqm) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_public_per_capita_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Green space per capita (sqm) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_public_per_capita_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Green space per capita (sqm) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_public_per_capita.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by green space per capita (sqm) with regard to total public green area per capita (m²; 2019).




Number of green areas (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of green areas within each district was recorded.  Classification was based on a typology of 9 kinds of green space: outdoor stadium, golf course, water source, lowland, open space, big tree areas, agricultural areas, aquaculture areas and other areas.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of green areas (2019), by district" src="./../png/bangkok_ind_district_green_space_count.png">
        <figcaption>Number of green areas (2019), by district.         <a href="./../html/bangkok_ind_district_green_space_count.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_green_space_count.png
       :width: 70%
       :align: center

       Number of green areas (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Total number of green areas (places) by population src="./../svg/plots/district_green_space_count_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Total number of green areas (places) by population per sqkm src="./../svg/plots/district_green_space_count_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Total number of green areas (places), ranked in ascending order src="./../svg/plots/district_green_space_count.svg">
            </div>
       <figcaption>Figures for Number Of Green Areas (2019) with regard to Total number of green areas (places) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_count_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Total number of green areas (places) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_count_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Total number of green areas (places) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_green_space_count.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by total number of green areas (places) with regard to number of green areas (2019).




Greater tree coverage to provide shade
||||||||||||||||||||||||||||||||||||||

ต้นไม้ที่ให้ร่มเงาในวงกว้าง

Greater tree coverage refers to canopy trees, being large trees with thick canopies or foliage coverings.


Dataset: Normalised Difference Vegetation Index
-----------------------------------------------

Landsat 8 Collection 1 Tier 1 Annual NDVI Composite data (LANDSAT/LC08/C01/T1_ANNUAL_NDVI) was retrieved using Google Earth Engine for Bangkok for 2019, using the bounding box WGS84 coordinates [100.327866596872, 13.4851864441217, 100.938637619401, 13.9551828398924].  Normalized Difference Vegetation Index (NDVI) was generated from the Near-IR and Red bands of each scene as (NIR - Red) / (NIR + Red), and ranges in value from -1.0 to 1.0. 

**Data source**: ``Landsat-8 data courtesy of the U.S. Geological Survey, processed using Google Earth Engine``

**URL**: ``https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_ANNUAL_NDVI``

**Publication year**: ``2020``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20200722``

**Licence**: ``none specified``

**Spatial reference (EPSG code)**: ``4326.0``

**Date type**: ``raster:float64``

**Scale / Resolution**: ``30``

**Notes**: ``Public domain; give credit to USGS and Google Earth Engine.``

**Data location relative to project folder**: ``./data/International/Google EarthEngine/LANDSAT_LC08_C01_T1_ANNUAL_NDVI_20190101_20191231.tif``


Normalised Difference Vegetation Index (NDVI, annual mean; 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The mean Normalized Difference Vegetation Index (NDVI) for each district and subdistrict was recorded

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Normalised Difference Vegetation Index (NDVI, annual mean; 2019), by subdistrict" src="./../png/bangkok_ind_subdistrict_vegetation_ndvi_mean.png">
        <figcaption>Normalised Difference Vegetation Index (NDVI, annual mean; 2019), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vegetation_ndvi_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_ndvi_mean.png
       :width: 70%
       :align: center

       Normalised Difference Vegetation Index (NDVI, annual mean; 2019), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Normalised Difference Vegetation Index (NDVI, annual mean; 2019), by district" src="./../png/bangkok_ind_district_vegetation_ndvi_mean.png">
        <figcaption>Normalised Difference Vegetation Index (NDVI, annual mean; 2019), by district.         <a href="./../html/bangkok_ind_district_vegetation_ndvi_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_ndvi_mean.png
       :width: 70%
       :align: center

       Normalised Difference Vegetation Index (NDVI, annual mean; 2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=mean Normalised Difference Vegetation Index (NDVI) by population src="./../svg/plots/district_vegetation_ndvi_mean_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=mean Normalised Difference Vegetation Index (NDVI) by population per sqkm src="./../svg/plots/district_vegetation_ndvi_mean_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=mean Normalised Difference Vegetation Index (NDVI), ranked in ascending order src="./../svg/plots/district_vegetation_ndvi_mean.svg">
            </div>
       <figcaption>Figures for Normalised Difference Vegetation Index (Ndvi, Annual Mean; 2019) with regard to mean Normalised Difference Vegetation Index (NDVI) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_ndvi_mean_population.pdf
      :width: 48%
      :align: center

      Scatterplot of mean Normalised Difference Vegetation Index (NDVI) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_ndvi_mean_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of mean Normalised Difference Vegetation Index (NDVI) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_ndvi_mean.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by mean normalised difference vegetation index (ndvi) with regard to normalised difference vegetation index (ndvi, annual mean; 2019).




Dataset: Enhanced vegetation index
----------------------------------

Landsat 8 Collection 1 Tier 1 Annual EVI Composite data (LANDSAT/LC08/C01/T1_ANNUAL_EVI) was retrieved using Google Earth Engine for Bangkok for 2019, using the bounding box WGS84 coordinates [100.327866596872, 13.4851864441217, 100.938637619401, 13.9551828398924].  The Enhanced Vegetation Index (EVI) is generated from the Near-IR, Red and Blue bands of each scene, and ranges in value from -1.0 to 1.0. See Huete et al. (2002) for details.

**Data source**: ``Landsat-8 data courtesy of the U.S. Geological Survey, processed using Google Earth Engine``

**URL**: ``https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_ANNUAL_EVI``

**Publication year**: ``2020``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20200722``

**Licence**: ``none specified``

**Spatial reference (EPSG code)**: ``4326.0``

**Date type**: ``raster:float64``

**Scale / Resolution**: ``30``

**Notes**: ``Public domain; give credit to USGS and Google Earth Engine.``

**Data location relative to project folder**: ``./data/International/Google EarthEngine/LANDSAT_LC08_C01_T1_ANNUAL_EVI_20190101_20191231.tif``


Enhanced Vegetation Index (EVI, annual mean; 2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The mean Enhanced Vegetation Index (EVI) for each district and subdistrict was recorded

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Enhanced Vegetation Index (EVI, annual mean; 2019), by subdistrict" src="./../png/bangkok_ind_subdistrict_vegetation_index_mean.png">
        <figcaption>Enhanced Vegetation Index (EVI, annual mean; 2019), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vegetation_index_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_index_mean.png
       :width: 70%
       :align: center

       Enhanced Vegetation Index (EVI, annual mean; 2019), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Enhanced Vegetation Index (EVI, annual mean; 2019), by district" src="./../png/bangkok_ind_district_vegetation_index_mean.png">
        <figcaption>Enhanced Vegetation Index (EVI, annual mean; 2019), by district.         <a href="./../html/bangkok_ind_district_vegetation_index_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_index_mean.png
       :width: 70%
       :align: center

       Enhanced Vegetation Index (EVI, annual mean; 2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=mean Enhanced Vegetation Index (EVI) by population src="./../svg/plots/district_vegetation_index_mean_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=mean Enhanced Vegetation Index (EVI) by population per sqkm src="./../svg/plots/district_vegetation_index_mean_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=mean Enhanced Vegetation Index (EVI), ranked in ascending order src="./../svg/plots/district_vegetation_index_mean.svg">
            </div>
       <figcaption>Figures for Enhanced Vegetation Index (Evi, Annual Mean; 2019) with regard to mean Enhanced Vegetation Index (EVI) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_index_mean_population.pdf
      :width: 48%
      :align: center

      Scatterplot of mean Enhanced Vegetation Index (EVI) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_index_mean_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of mean Enhanced Vegetation Index (EVI) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_index_mean.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by mean enhanced vegetation index (evi) with regard to enhanced vegetation index (evi, annual mean; 2019).




Dataset: Fraction of Vegetation Cover
-------------------------------------

A modelled fraction of vegetation cover (FCOVER, V2) 1km grid data product based on Copernicus satellite imagery targetting 20 December 2018 was downloaded in NetCDF (.nc) format.  Using the ESA SNAP software, a GeoTiff (.tif) excerpt was taken for the Bangkok region.  Band 1 of this satellite data product represents the fraction of vegetation cover.  Data values ranging from 0 to 250 are to be transformed to a 0 to 1 range to represent the fraction of vegetation cover within each grid portion.  Cell values of 255 represent no data, and were excluded.

**Data source**: ``Copernicus Service Information``

**URL**: ``https://land.copernicus.eu/global/products/fcover``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190913``

**Licence**: ``Free, full and open access for lawful usage, with attribution``

**Licence URL**: ``https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice``

**Spatial reference (EPSG code)**: ``4326.0``

**Date type**: ``raster:float64``

**Scale / Resolution**: ``1000``

**Data location relative to project folder**: ``./data/International/EC-JRC/Copernicus/subset_0_of_c_gls_FCOVER-RT6_201812200000_GLOBE_PROBAV_V2.tif``


Vegetation Percent (mean; December 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The estimated percentage of vegetation cover within each analysis area was calculated by first scaling the raster grid cell values by 100/250 ( a scale factor of 0.4) and then taking the mean (average) of all intersecting grid cells.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (mean; December 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_vegetation_pct_mean.png">
        <figcaption>Vegetation Percent (mean; December 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vegetation_pct_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_pct_mean.png
       :width: 70%
       :align: center

       Vegetation Percent (mean; December 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (mean; December 2018), by district" src="./../png/bangkok_ind_district_vegetation_pct_mean.png">
        <figcaption>Vegetation Percent (mean; December 2018), by district.         <a href="./../html/bangkok_ind_district_vegetation_pct_mean.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_pct_mean.png
       :width: 70%
       :align: center

       Vegetation Percent (mean; December 2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=mean vegetation cover percent  (Copernicus, December 2018) by population src="./../svg/plots/district_vegetation_pct_mean_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=mean vegetation cover percent  (Copernicus, December 2018) by population per sqkm src="./../svg/plots/district_vegetation_pct_mean_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=mean vegetation cover percent  (Copernicus, December 2018), ranked in ascending order src="./../svg/plots/district_vegetation_pct_mean.svg">
            </div>
       <figcaption>Figures for Vegetation Percent (Mean; December 2018) with regard to mean vegetation cover percent  (Copernicus, December 2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_pct_mean_population.pdf
      :width: 48%
      :align: center

      Scatterplot of mean vegetation cover percent  (Copernicus, December 2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_pct_mean_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of mean vegetation cover percent  (Copernicus, December 2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_vegetation_pct_mean.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by mean vegetation cover percent  (copernicus, december 2018) with regard to vegetation percent (mean; december 2018).




Vegetation Percent (standard deviation; December 2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The estimated standard deviation of percentage of vegetation cover within each analysis area was calculated by first scaling the raster grid cell values by 100/250 ( a scale factor of 0.4) and then taking the standard deviation of all intersecting grid cells.  This is a measure of the degree to wich estimates vary across a particular area, and is a useful contextual measure to accompany the average vegetation percent for the area.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (standard deviation; December 2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_vegetation_pct_sd.png">
        <figcaption>Vegetation Percent (standard deviation; December 2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_vegetation_pct_sd.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_vegetation_pct_sd.png
       :width: 70%
       :align: center

       Vegetation Percent (standard deviation; December 2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Vegetation Percent (standard deviation; December 2018), by district" src="./../png/bangkok_ind_district_vegetation_pct_sd.png">
        <figcaption>Vegetation Percent (standard deviation; December 2018), by district.         <a href="./../html/bangkok_ind_district_vegetation_pct_sd.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_vegetation_pct_sd.png
       :width: 70%
       :align: center

       Vegetation Percent (standard deviation; December 2018), by district




Areas for passive recreation and physical activity
||||||||||||||||||||||||||||||||||||||||||||||||||

พื้นที่สำหรับพักผ่อนและออกกำลังกาย

Passive recreation means recreational activities that do not require facilities such as a stadium or pavilion (walking, picnic, camping, swimming, biking, hiking, observing and photographing nature ).  Physical activity means an individual or team activity that has a structure that requires facilities, courses, courts, or special equipment (football, golf, tennis, et cetera).


Dataset: Public Open Space
--------------------------

A dataset of Areas of Public Open Space was derived from OpenStreetMap using a series of key-value pair tag queries in conjunction with morphological and heuristic criteria.  [description to be updated]

**Data source**: ``OpenStreetMap``

**Publication year**: ``2019``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20191007``

**Licence**: ``ODbL``

**Licence URL**: ``https://wiki.osmfoundation.org/wiki/Licence``

**Scale / Resolution**: ``400``

**Notes**: ``User contributed data; Please note licence implications involving usage of OSM data when combined with other data sets``

**Data location relative to project folder**: ``./data/International/OSM/thailand-latest.20191007.osm.pbf``


Percentage of residents living within 400 metres of public open space  (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Accessibility within 400m was evaluated using the Python network analysis package Pandana for a series of sample points generated every 50 metres along the Bangkok OSM pedestrian network.   Population weighted averages for the proportion of sample points having access in each subdistrict were used to estimate the measure.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living within 400 metres of public open space  (2019), by subdistrict" src="./../png/bangkok_ind_subdistrict_access_pos_entry_any_400m_pop_pct.png">
        <figcaption>Percentage of residents living within 400 metres of public open space  (2019), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_access_pos_entry_any_400m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_access_pos_entry_any_400m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living within 400 metres of public open space  (2019), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living within 400 metres of public open space  (2019), by district" src="./../png/bangkok_ind_district_access_pos_entry_any_400m_pop_pct.png">
        <figcaption>Percentage of residents living within 400 metres of public open space  (2019), by district.         <a href="./../html/bangkok_ind_district_access_pos_entry_any_400m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_access_pos_entry_any_400m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living within 400 metres of public open space  (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=% living within 400 metres of public open space  (OSM, 2019) by population src="./../svg/plots/district_access_pos_entry_any_400m_pop_pct_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=% living within 400 metres of public open space  (OSM, 2019) by population per sqkm src="./../svg/plots/district_access_pos_entry_any_400m_pop_pct_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=% living within 400 metres of public open space  (OSM, 2019), ranked in ascending order src="./../svg/plots/district_access_pos_entry_any_400m_pop_pct.svg">
            </div>
       <figcaption>Figures for Percentage Of Residents Living Within 400 Metres Of Public Open Space  (2019) with regard to % living within 400 metres of public open space  (OSM, 2019) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pos_entry_any_400m_pop_pct_population.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 400 metres of public open space  (OSM, 2019) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pos_entry_any_400m_pop_pct_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 400 metres of public open space  (OSM, 2019) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pos_entry_any_400m_pop_pct.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by % living within 400 metres of public open space  (osm, 2019) with regard to percentage of residents living within 400 metres of public open space  (2019).







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=% living within 400 metres of large public open space  (OSM, 2019) by population src="./../svg/plots/district_access_pos_entry_large_400m_pop_pct_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=% living within 400 metres of large public open space  (OSM, 2019) by population per sqkm src="./../svg/plots/district_access_pos_entry_large_400m_pop_pct_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=% living within 400 metres of large public open space  (OSM, 2019), ranked in ascending order src="./../svg/plots/district_access_pos_entry_large_400m_pop_pct.svg">
            </div>
       <figcaption>Figures for Percentage Of Residents Living Within 400 Metres Of Large Public Open Space  (1.5 Hectares Or Larger; 2019) with regard to % living within 400 metres of large public open space  (OSM, 2019) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pos_entry_large_400m_pop_pct_population.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 400 metres of large public open space  (OSM, 2019) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pos_entry_large_400m_pop_pct_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 400 metres of large public open space  (OSM, 2019) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pos_entry_large_400m_pop_pct.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by % living within 400 metres of large public open space  (osm, 2019) with regard to percentage of residents living within 400 metres of large public open space  (1.5 hectares or larger; 2019).




Mass transit availability; connected public transport networks; increased provision of transit-oriented developments
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

ขนส่งมวลชนที่มีให้บริการ (เครือข่ายเชื่อมต่อ พัฒนาเพิ่มทางเลือก

Mass transportation systems refer to public transport in the metropolitan area, usually consisting of buses subway and elevated trains.   Convenient public transportation access means refers to public transport stops accessible within a walkable distance (e.g. 500 metres) of a reference point, such as homes, schools, workplaces, markets, etc. Additional characteristics includ:  A) Public transportation can reach people with special needs, including people with physical disabilities and / or hearing impairments, including people with temporary disabilities. The elderly, children and others in vulnerable situations;  B. Frequent public transport services during peak travel times;  C. Stations or stops showing a safe and convenient environment


Dataset: Public Transport
-------------------------

Combined BMA railway stations (BTS, MRT, airtportlink, and other train stations; BMA, 2014) were analysed for Accessibility using an OSM pedestrian network, derived using OSMnx.

**Data source**: ``BangkokGIS (BMA)``

**Publication year**: ``2014``

**Target year**: ``2014``

**Acquisition date (yyyymmdd)**: ``20181210``

**Licence**: ``none specified``

**Spatial reference (EPSG code)**: ``32647.0``

**Date type**: ``vector``

**Scale / Resolution**: ``800``


Percentage of residents living within 800 metres of a train station (2014)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Accessibility within 800m was evaluated using the Python network analysis package Pandana for a series of sample points generated every 50 metres along the Bangkok OSM pedestrian network.   Population weighted averages for the proportion of sample points having access in each subdistrict were used to estimate the measure.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living within 800 metres of a train station (2014), by subdistrict" src="./../png/bangkok_ind_subdistrict_access_train_800m_pop_pct.png">
        <figcaption>Percentage of residents living within 800 metres of a train station (2014), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_access_train_800m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_access_train_800m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living within 800 metres of a train station (2014), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living within 800 metres of a train station (2014), by district" src="./../png/bangkok_ind_district_access_train_800m_pop_pct.png">
        <figcaption>Percentage of residents living within 800 metres of a train station (2014), by district.         <a href="./../html/bangkok_ind_district_access_train_800m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_access_train_800m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living within 800 metres of a train station (2014), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=% living within 800 metres by population src="./../svg/plots/district_access_train_800m_pop_pct_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=% living within 800 metres by population per sqkm src="./../svg/plots/district_access_train_800m_pop_pct_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=% living within 800 metres, ranked in ascending order src="./../svg/plots/district_access_train_800m_pop_pct.svg">
            </div>
       <figcaption>Figures for Percentage Of Residents Living Within 800 Metres Of A Train Station (2014) with regard to % living within 800 metres by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_train_800m_pop_pct_population.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 800 metres by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_train_800m_pop_pct_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 800 metres by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_train_800m_pop_pct.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by % living within 800 metres with regard to percentage of residents living within 800 metres of a train station (2014).




Healthy population
||||||||||||||||||

ประชากรมีสุขภาพดี ทั้งทางกายและจิตใจ

Healthy population refers to the health status and health outcomes within the population.


Dataset: Public Transport
-------------------------

Ferry terminals / quays along the Chao Praya river and Canal Sansabai (BMA, 2014) were combined and analysed for Accessibility using an OSM pedestrian network, derived using OSMnx.

**Data source**: ``BangkokGIS (BMA)``

**Publication year**: ``2014``

**Target year**: ``2014``

**Acquisition date (yyyymmdd)**: ``20181210``

**Licence**: ``none specified``

**Spatial reference (EPSG code)**: ``32647.0``

**Date type**: ``vector``

**Scale / Resolution**: ``800``


Percentage of residents living within 800 metres of a ferry terminal or pier (2014)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Accessibility within 800m was evaluated using the Python network analysis package Pandana for a series of sample points generated every 50 metres along the Bangkok OSM pedestrian network.   Population weighted averages for the proportion of sample points having access in each subdistrict were used to estimate the measure.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living within 800 metres of a ferry terminal or pier (2014), by subdistrict" src="./../png/bangkok_ind_subdistrict_access_ferry_800m_pop_pct.png">
        <figcaption>Percentage of residents living within 800 metres of a ferry terminal or pier (2014), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_access_ferry_800m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_access_ferry_800m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living within 800 metres of a ferry terminal or pier (2014), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living within 800 metres of a ferry terminal or pier (2014), by district" src="./../png/bangkok_ind_district_access_ferry_800m_pop_pct.png">
        <figcaption>Percentage of residents living within 800 metres of a ferry terminal or pier (2014), by district.         <a href="./../html/bangkok_ind_district_access_ferry_800m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_access_ferry_800m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living within 800 metres of a ferry terminal or pier (2014), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=% living within 800 metres by population src="./../svg/plots/district_access_ferry_800m_pop_pct_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=% living within 800 metres by population per sqkm src="./../svg/plots/district_access_ferry_800m_pop_pct_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=% living within 800 metres, ranked in ascending order src="./../svg/plots/district_access_ferry_800m_pop_pct.svg">
            </div>
       <figcaption>Figures for Percentage Of Residents Living Within 800 Metres Of A Ferry Terminal Or Pier (2014) with regard to % living within 800 metres by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_ferry_800m_pop_pct_population.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 800 metres by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_ferry_800m_pop_pct_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 800 metres by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_ferry_800m_pop_pct.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by % living within 800 metres with regard to percentage of residents living within 800 metres of a ferry terminal or pier (2014).







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=% living within 800 metres by population src="./../svg/plots/district_access_pt_any_800m_pop_pct_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=% living within 800 metres by population per sqkm src="./../svg/plots/district_access_pt_any_800m_pop_pct_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=% living within 800 metres, ranked in ascending order src="./../svg/plots/district_access_pt_any_800m_pop_pct.svg">
            </div>
       <figcaption>Figures for Percentage Of Residents Living 800 Metres Distance Of Any Public Transport (2019) with regard to % living within 800 metres by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pt_any_800m_pop_pct_population.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 800 metres by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pt_any_800m_pop_pct_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of % living within 800 metres by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_pt_any_800m_pop_pct.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by % living within 800 metres with regard to percentage of residents living 800 metres distance of any public transport (2019).




Enhancing quality of life
~~~~~~~~~~~~~~~~~~~~~~~~~


Job security
||||||||||||

ความมั่นคงในการทำงาน

Security at work or employment means the confidence of people that they will not lose their current job without sufficient or acceptable reason.


Dataset: Welfare card holders
-----------------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``BMA``

**Publication year**: ``2017``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20191204``

**Licence**: ``none specified``

**Licence URL**: ``Ministry of Finance; Department of Social Development (BMA)``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Notes**: ``Only two districts have 12 locations; perhaps <= 10 would be a more aspirational target.``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20191204/transfer_1815197_files_51cc5a2c/1_Holders of a state welfare card in Bangkok by district_kn20191111.xlsx``


Holders of a state welfare card in Bangkok (2017)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of persons issued a state welfare card in Bangkok Year 2017 was recorded for each district.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Holders of a state welfare card in Bangkok (2017), by district" src="./../png/bangkok_ind_district_welfare_card_holders.png">
        <figcaption>Holders of a state welfare card in Bangkok (2017), by district.         <a href="./../html/bangkok_ind_district_welfare_card_holders.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_welfare_card_holders.png
       :width: 70%
       :align: center

       Holders of a state welfare card in Bangkok (2017), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=State welfare card holders by population src="./../svg/plots/district_welfare_card_holders_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=State welfare card holders by population per sqkm src="./../svg/plots/district_welfare_card_holders_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=State welfare card holders, ranked in ascending order src="./../svg/plots/district_welfare_card_holders.svg">
            </div>
       <figcaption>Figures for Holders Of A State Welfare Card In Bangkok (2017) with regard to State welfare card holders by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_welfare_card_holders_population.pdf
      :width: 48%
      :align: center

      Scatterplot of State welfare card holders by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_welfare_card_holders_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of State welfare card holders by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_welfare_card_holders.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by state welfare card holders with regard to holders of a state welfare card in bangkok (2017).




Dataset: Drought impact
-----------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``BMA``

**Publication year**: ``2015``

**Target year**: ``2016``

**Acquisition date (yyyymmdd)**: ``20191204``

**Licence**: ``none specified``

**Licence URL**: ``Ministry of Finance; Department of Social Development (BMA)``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Notes**: ``Only two districts have 12 locations; perhaps <= 10 would be a more aspirational target.``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20191204/transfer_1815197_files_51cc5a2c/2_BKK agriculture _drought_2016 _ district _kn20191124.xlsx``


Number of registered farmer househoulds expected to be impacted by drought (2016)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Number of farmers (households) who expected to be impacted drought in 2016 was recorded for each district.

Aligns with Sustainable Development Goals: 3, 11, 13, 15.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of registered farmer househoulds expected to be impacted by drought (2016), by district" src="./../png/bangkok_ind_district_drought_impacted_farmers.png">
        <figcaption>Number of registered farmer househoulds expected to be impacted by drought (2016), by district.         <a href="./../html/bangkok_ind_district_drought_impacted_farmers.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_drought_impacted_farmers.png
       :width: 70%
       :align: center

       Number of registered farmer househoulds expected to be impacted by drought (2016), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Number of households in the area expected to get impacts drought (registered farmers) by population src="./../svg/plots/district_drought_impacted_farmers_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Number of households in the area expected to get impacts drought (registered farmers) by population per sqkm src="./../svg/plots/district_drought_impacted_farmers_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Number of households in the area expected to get impacts drought (registered farmers), ranked in ascending order src="./../svg/plots/district_drought_impacted_farmers.svg">
            </div>
       <figcaption>Figures for Number Of Registered Farmer Househoulds Expected To Be Impacted By Drought (2016) with regard to Number of households in the area expected to get impacts drought (registered farmers) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_drought_impacted_farmers_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of households in the area expected to get impacts drought (registered farmers) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_drought_impacted_farmers_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of households in the area expected to get impacts drought (registered farmers) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_drought_impacted_farmers.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by number of households in the area expected to get impacts drought (registered farmers) with regard to number of registered farmer househoulds expected to be impacted by drought (2016).




Healthy population
||||||||||||||||||

ประชากรมีสุขภาพดี ทั้งทางกายและจิตใจ

Healthy population refers to the health status and health outcomes within the population.


Dataset: Population by age groups
---------------------------------

Bangkok population counts classified by years of age (December 2018) were cleaned for processing,  aligned with standard area identification codes, and used to derive average and standard deviation for age for each district and subdistrict.

**Data source**: ``Department of Provincial Administration, Ministry of Interior (BMA)``

**Publication year**: ``2018``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190930``

**Licence**: ``none specified``

**Date type**: ``numeric``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190930/transfer_1730651_files_296a713c/Bangkok Population by age groups2018_kn08242019.xlsx``


Average age (2018)
>>>>>>>>>>>>>>>>>>

The average age of residents for each district and subdistrict was estimated and recorded. 

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average age (2018), by district" src="./../png/bangkok_ind_district_age_mean_district.png">
        <figcaption>Average age (2018), by district.         <a href="./../html/bangkok_ind_district_age_mean_district.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_age_mean_district.png
       :width: 70%
       :align: center

       Average age (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=average age by population src="./../svg/plots/district_age_mean_district_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=average age by population per sqkm src="./../svg/plots/district_age_mean_district_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=average age, ranked in ascending order src="./../svg/plots/district_age_mean_district.svg">
            </div>
       <figcaption>Figures for Average Age (2018) with regard to average age by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_age_mean_district_population.pdf
      :width: 48%
      :align: center

      Scatterplot of average age by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_age_mean_district_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of average age by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_age_mean_district.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by average age with regard to average age (2018).







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average age (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_age_mean_subdistrict.png">
        <figcaption>Average age (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_age_mean_subdistrict.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_age_mean_subdistrict.png
       :width: 70%
       :align: center

       Average age (2018), by subdistrict




Dataset: Vital diseases
-----------------------

Data at subdistrict level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of Health, BMA``

**Publication year**: ``2018``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190617``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190617/vital diseases HC BMA 2018.xlsx``


Health centers (2018)
>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres.png">
        <figcaption>Health centers (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres.png
       :width: 70%
       :align: center

       Health centers (2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018), by district" src="./../png/bangkok_ind_district_health_centres.png">
        <figcaption>Health centers (2018), by district.         <a href="./../html/bangkok_ind_district_health_centres.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres.png
       :width: 70%
       :align: center

       Health centers (2018), by district




Health centers (2018) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018) per km², by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres_rate_area.png">
        <figcaption>Health centers (2018) per km², by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres_rate_area.png
       :width: 70%
       :align: center

       Health centers (2018) per km², by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018) per km², by district" src="./../png/bangkok_ind_district_health_centres_rate_area.png">
        <figcaption>Health centers (2018) per km², by district.         <a href="./../html/bangkok_ind_district_health_centres_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres_rate_area.png
       :width: 70%
       :align: center

       Health centers (2018) per km², by district




Health centers (2018) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018) per 10,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres_rate_population.png">
        <figcaption>Health centers (2018) per 10,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres_rate_population.png
       :width: 70%
       :align: center

       Health centers (2018) per 10,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018) per 10,000 population, by district" src="./../png/bangkok_ind_district_health_centres_rate_population.png">
        <figcaption>Health centers (2018) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_health_centres_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres_rate_population.png
       :width: 70%
       :align: center

       Health centers (2018) per 10,000 population, by district




Health centers (2018) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of health centers within each analysis area was calculated, based on the supplied data.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018) per 10,000 household, by subdistrict" src="./../png/bangkok_ind_subdistrict_health_centres_rate_household.png">
        <figcaption>Health centers (2018) per 10,000 household, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_health_centres_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_health_centres_rate_household.png
       :width: 70%
       :align: center

       Health centers (2018) per 10,000 household, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Health centers (2018) per 10,000 household, by district" src="./../png/bangkok_ind_district_health_centres_rate_household.png">
        <figcaption>Health centers (2018) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_health_centres_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_health_centres_rate_household.png
       :width: 70%
       :align: center

       Health centers (2018) per 10,000 household, by district




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population src="./../svg/plots/district_outpatients_mental_health_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population per sqkm src="./../svg/plots/district_outpatients_mental_health_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=mental and behavioural disorders (2018), ranked in ascending order src="./../svg/plots/district_outpatients_mental_health.svg">
            </div>
       <figcaption>Figures for Mental And Behavioural Disorder Outpatients (2018) with regard to mental and behavioural disorders (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_population.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by mental and behavioural disorders (2018) with regard to mental and behavioural disorder outpatients (2018).




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population src="./../svg/plots/district_outpatients_mental_health_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population per sqkm src="./../svg/plots/district_outpatients_mental_health_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=mental and behavioural disorders (2018), ranked in ascending order src="./../svg/plots/district_outpatients_mental_health_rate_area.svg">
            </div>
       <figcaption>Figures for Mental And Behavioural Disorder Outpatients (2018) Per Km² with regard to mental and behavioural disorders (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by mental and behavioural disorders (2018) with regard to mental and behavioural disorder outpatients (2018) per km².




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population src="./../svg/plots/district_outpatients_mental_health_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population per sqkm src="./../svg/plots/district_outpatients_mental_health_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=mental and behavioural disorders (2018), ranked in ascending order src="./../svg/plots/district_outpatients_mental_health_rate_population.svg">
            </div>
       <figcaption>Figures for Mental And Behavioural Disorder Outpatients (2018) Per 10,000 Population with regard to mental and behavioural disorders (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by mental and behavioural disorders (2018) with regard to mental and behavioural disorder outpatients (2018) per 10,000 population.




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population src="./../svg/plots/district_outpatients_mental_health_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=mental and behavioural disorders (2018) by population per sqkm src="./../svg/plots/district_outpatients_mental_health_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=mental and behavioural disorders (2018), ranked in ascending order src="./../svg/plots/district_outpatients_mental_health_rate_household.svg">
            </div>
       <figcaption>Figures for Mental And Behavioural Disorder Outpatients (2018) Per 10,000 Household with regard to mental and behavioural disorders (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of mental and behavioural disorders (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_mental_health_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by mental and behavioural disorders (2018) with regard to mental and behavioural disorder outpatients (2018) per 10,000 household.




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=hypertension (2018) by population src="./../svg/plots/district_outpatients_hypertension_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=hypertension (2018) by population per sqkm src="./../svg/plots/district_outpatients_hypertension_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=hypertension (2018), ranked in ascending order src="./../svg/plots/district_outpatients_hypertension.svg">
            </div>
       <figcaption>Figures for Hypertension Outpatients (2018) with regard to hypertension (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_population.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by hypertension (2018) with regard to hypertension outpatients (2018).




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=hypertension (2018) by population src="./../svg/plots/district_outpatients_hypertension_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=hypertension (2018) by population per sqkm src="./../svg/plots/district_outpatients_hypertension_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=hypertension (2018), ranked in ascending order src="./../svg/plots/district_outpatients_hypertension_rate_area.svg">
            </div>
       <figcaption>Figures for Hypertension Outpatients (2018) Per Km² with regard to hypertension (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by hypertension (2018) with regard to hypertension outpatients (2018) per km².




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=hypertension (2018) by population src="./../svg/plots/district_outpatients_hypertension_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=hypertension (2018) by population per sqkm src="./../svg/plots/district_outpatients_hypertension_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=hypertension (2018), ranked in ascending order src="./../svg/plots/district_outpatients_hypertension_rate_population.svg">
            </div>
       <figcaption>Figures for Hypertension Outpatients (2018) Per 10,000 Population with regard to hypertension (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by hypertension (2018) with regard to hypertension outpatients (2018) per 10,000 population.




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=hypertension (2018) by population src="./../svg/plots/district_outpatients_hypertension_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=hypertension (2018) by population per sqkm src="./../svg/plots/district_outpatients_hypertension_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=hypertension (2018), ranked in ascending order src="./../svg/plots/district_outpatients_hypertension_rate_household.svg">
            </div>
       <figcaption>Figures for Hypertension Outpatients (2018) Per 10,000 Household with regard to hypertension (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of hypertension (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_hypertension_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by hypertension (2018) with regard to hypertension outpatients (2018) per 10,000 household.




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=diabetes (2018) by population src="./../svg/plots/district_outpatients_diabetes_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=diabetes (2018) by population per sqkm src="./../svg/plots/district_outpatients_diabetes_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=diabetes (2018), ranked in ascending order src="./../svg/plots/district_outpatients_diabetes.svg">
            </div>
       <figcaption>Figures for Diabetes Outpatients (2018) with regard to diabetes (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_population.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by diabetes (2018) with regard to diabetes outpatients (2018).




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=diabetes (2018) by population src="./../svg/plots/district_outpatients_diabetes_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=diabetes (2018) by population per sqkm src="./../svg/plots/district_outpatients_diabetes_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=diabetes (2018), ranked in ascending order src="./../svg/plots/district_outpatients_diabetes_rate_area.svg">
            </div>
       <figcaption>Figures for Diabetes Outpatients (2018) Per Km² with regard to diabetes (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by diabetes (2018) with regard to diabetes outpatients (2018) per km².




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=diabetes (2018) by population src="./../svg/plots/district_outpatients_diabetes_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=diabetes (2018) by population per sqkm src="./../svg/plots/district_outpatients_diabetes_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=diabetes (2018), ranked in ascending order src="./../svg/plots/district_outpatients_diabetes_rate_population.svg">
            </div>
       <figcaption>Figures for Diabetes Outpatients (2018) Per 10,000 Population with regard to diabetes (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by diabetes (2018) with regard to diabetes outpatients (2018) per 10,000 population.




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=diabetes (2018) by population src="./../svg/plots/district_outpatients_diabetes_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=diabetes (2018) by population per sqkm src="./../svg/plots/district_outpatients_diabetes_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=diabetes (2018), ranked in ascending order src="./../svg/plots/district_outpatients_diabetes_rate_household.svg">
            </div>
       <figcaption>Figures for Diabetes Outpatients (2018) Per 10,000 Household with regard to diabetes (2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of diabetes (2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_diabetes_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by diabetes (2018) with regard to diabetes outpatients (2018) per 10,000 household.




Quality food
||||||||||||

อาหารมีคุณภาพ

Food safety refers to the practice and conditions of maintaining food quality to prevent contamination and foodborne illnesses during preparation, management and storage.   Food quality refers to properties and characteristics of food products that are acceptable to consumers and meet expectations of safety and value for money.


Dataset: Vital diseases
-----------------------

Data at subdistrict level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of Health, BMA``

**Publication year**: ``2018``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190617``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190617/vital diseases HC BMA 2018.xlsx``


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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population src="./../svg/plots/district_outpatients_combined_diseases_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population per sqkm src="./../svg/plots/district_outpatients_combined_diseases_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=vital diseases (combined; 2018), ranked in ascending order src="./../svg/plots/district_outpatients_combined_diseases.svg">
            </div>
       <figcaption>Figures for Vital Diseases (Combined, 2018) with regard to vital diseases (combined; 2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_population.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by vital diseases (combined; 2018) with regard to vital diseases (combined, 2018).




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population src="./../svg/plots/district_outpatients_combined_diseases_rate_area_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population per sqkm src="./../svg/plots/district_outpatients_combined_diseases_rate_area_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=vital diseases (combined; 2018), ranked in ascending order src="./../svg/plots/district_outpatients_combined_diseases_rate_area.svg">
            </div>
       <figcaption>Figures for Vital Diseases (Combined, 2018) Per Km² with regard to vital diseases (combined; 2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_area_population.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_area_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_area.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by vital diseases (combined; 2018) with regard to vital diseases (combined, 2018) per km².




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population src="./../svg/plots/district_outpatients_combined_diseases_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population per sqkm src="./../svg/plots/district_outpatients_combined_diseases_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=vital diseases (combined; 2018), ranked in ascending order src="./../svg/plots/district_outpatients_combined_diseases_rate_population.svg">
            </div>
       <figcaption>Figures for Vital Diseases (Combined, 2018) Per 10,000 Population with regard to vital diseases (combined; 2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by vital diseases (combined; 2018) with regard to vital diseases (combined, 2018) per 10,000 population.




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







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population src="./../svg/plots/district_outpatients_combined_diseases_rate_household_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=vital diseases (combined; 2018) by population per sqkm src="./../svg/plots/district_outpatients_combined_diseases_rate_household_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=vital diseases (combined; 2018), ranked in ascending order src="./../svg/plots/district_outpatients_combined_diseases_rate_household.svg">
            </div>
       <figcaption>Figures for Vital Diseases (Combined, 2018) Per 10,000 Household with regard to vital diseases (combined; 2018) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_household_population.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_household_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of vital diseases (combined; 2018) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_outpatients_combined_diseases_rate_household.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by vital diseases (combined; 2018) with regard to vital diseases (combined, 2018) per 10,000 household.




Dataset: Supermarket acccess
----------------------------

Supermarket locations identified through key-value pair tags according to OSM guidelines or common usage patterns identified from OSM Taginfo were analysed for accessibility using a pedestrian network derived from OSM data using OSMnx.

**Data source**: ``OpenStreetMap``

**Publication year**: ``2019``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20191007``

**Licence**: ``ODbL``

**Licence URL**: ``https://wiki.osmfoundation.org/wiki/Licence``

**Scale / Resolution**: ``800``


Percentage of residents living 800 metres distance of a supermarket (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Accessibility within 800m was evaluated using the Python network analysis package Pandana for a series of sample points generated every 50 metres along the Bangkok OSM pedestrian network.   Population weighted averages for the proportion of sample points having access in each subdistrict were used to estimate the measure.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living 800 metres distance of a supermarket (2019), by subdistrict" src="./../png/bangkok_ind_subdistrict_access_supermarket_800m_pop_pct.png">
        <figcaption>Percentage of residents living 800 metres distance of a supermarket (2019), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_access_supermarket_800m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_access_supermarket_800m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living 800 metres distance of a supermarket (2019), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of residents living 800 metres distance of a supermarket (2019), by district" src="./../png/bangkok_ind_district_access_supermarket_800m_pop_pct.png">
        <figcaption>Percentage of residents living 800 metres distance of a supermarket (2019), by district.         <a href="./../html/bangkok_ind_district_access_supermarket_800m_pop_pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_access_supermarket_800m_pop_pct.png
       :width: 70%
       :align: center

       Percentage of residents living 800 metres distance of a supermarket (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Percentage of residents living 800 metres distance of a supermarket (OSM, 2019) by population src="./../svg/plots/district_access_supermarket_800m_pop_pct_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Percentage of residents living 800 metres distance of a supermarket (OSM, 2019) by population per sqkm src="./../svg/plots/district_access_supermarket_800m_pop_pct_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Percentage of residents living 800 metres distance of a supermarket (OSM, 2019), ranked in ascending order src="./../svg/plots/district_access_supermarket_800m_pop_pct.svg">
            </div>
       <figcaption>Figures for Percentage Of Residents Living 800 Metres Distance Of A Supermarket (2019) with regard to Percentage of residents living 800 metres distance of a supermarket (OSM, 2019) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_supermarket_800m_pop_pct_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Percentage of residents living 800 metres distance of a supermarket (OSM, 2019) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_supermarket_800m_pop_pct_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Percentage of residents living 800 metres distance of a supermarket (OSM, 2019) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_access_supermarket_800m_pop_pct.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by percentage of residents living 800 metres distance of a supermarket (osm, 2019) with regard to percentage of residents living 800 metres distance of a supermarket (2019).




Dataset: Food entrepreneurs
---------------------------

Data comprising counts of restaurants, supermarkets, minimarts, stalls and markets for each district were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of Environment and Sanitation, BMA``

**Publication year**: ``2019``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190820``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190820/transfer_1682928_files_504fdeaf/Num of food entrepreneur in Bangkok 2019 -kn15819.xlsx``


Number of restaurants (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (2019), by district" src="./../png/bangkok_ind_district_restaurants.png">
        <figcaption>Number of restaurants (2019), by district.         <a href="./../html/bangkok_ind_district_restaurants.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants.png
       :width: 70%
       :align: center

       Number of restaurants (2019), by district




Number of restaurants (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (2019) per km², by district" src="./../png/bangkok_ind_district_restaurants_rate_area.png">
        <figcaption>Number of restaurants (2019) per km², by district.         <a href="./../html/bangkok_ind_district_restaurants_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_rate_area.png
       :width: 70%
       :align: center

       Number of restaurants (2019) per km², by district




Number of restaurants (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_restaurants_rate_population.png">
        <figcaption>Number of restaurants (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_restaurants_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_rate_population.png
       :width: 70%
       :align: center

       Number of restaurants (2019) per 10,000 population, by district




Number of restaurants (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of restaurants within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of restaurants (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_restaurants_rate_household.png">
        <figcaption>Number of restaurants (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_restaurants_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_restaurants_rate_household.png
       :width: 70%
       :align: center

       Number of restaurants (2019) per 10,000 household, by district




Number of supermarkets (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (2019), by district" src="./../png/bangkok_ind_district_supermarkets.png">
        <figcaption>Number of supermarkets (2019), by district.         <a href="./../html/bangkok_ind_district_supermarkets.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets.png
       :width: 70%
       :align: center

       Number of supermarkets (2019), by district




Number of supermarkets (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (2019) per km², by district" src="./../png/bangkok_ind_district_supermarkets_rate_area.png">
        <figcaption>Number of supermarkets (2019) per km², by district.         <a href="./../html/bangkok_ind_district_supermarkets_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_rate_area.png
       :width: 70%
       :align: center

       Number of supermarkets (2019) per km², by district




Number of supermarkets (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_supermarkets_rate_population.png">
        <figcaption>Number of supermarkets (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_supermarkets_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_rate_population.png
       :width: 70%
       :align: center

       Number of supermarkets (2019) per 10,000 population, by district




Number of supermarkets (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of supermarkets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of supermarkets (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_supermarkets_rate_household.png">
        <figcaption>Number of supermarkets (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_supermarkets_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_supermarkets_rate_household.png
       :width: 70%
       :align: center

       Number of supermarkets (2019) per 10,000 household, by district




Number of minimarts (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (2019), by district" src="./../png/bangkok_ind_district_minimarts.png">
        <figcaption>Number of minimarts (2019), by district.         <a href="./../html/bangkok_ind_district_minimarts.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts.png
       :width: 70%
       :align: center

       Number of minimarts (2019), by district




Number of minimarts (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (2019) per km², by district" src="./../png/bangkok_ind_district_minimarts_rate_area.png">
        <figcaption>Number of minimarts (2019) per km², by district.         <a href="./../html/bangkok_ind_district_minimarts_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_rate_area.png
       :width: 70%
       :align: center

       Number of minimarts (2019) per km², by district




Number of minimarts (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_minimarts_rate_population.png">
        <figcaption>Number of minimarts (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_minimarts_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_rate_population.png
       :width: 70%
       :align: center

       Number of minimarts (2019) per 10,000 population, by district




Number of minimarts (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of minimarts within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of minimarts (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_minimarts_rate_household.png">
        <figcaption>Number of minimarts (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_minimarts_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_minimarts_rate_household.png
       :width: 70%
       :align: center

       Number of minimarts (2019) per 10,000 household, by district




Number of stalls (2019)
>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (2019), by district" src="./../png/bangkok_ind_district_stalls.png">
        <figcaption>Number of stalls (2019), by district.         <a href="./../html/bangkok_ind_district_stalls.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls.png
       :width: 70%
       :align: center

       Number of stalls (2019), by district




Number of stalls (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (2019) per km², by district" src="./../png/bangkok_ind_district_stalls_rate_area.png">
        <figcaption>Number of stalls (2019) per km², by district.         <a href="./../html/bangkok_ind_district_stalls_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_rate_area.png
       :width: 70%
       :align: center

       Number of stalls (2019) per km², by district




Number of stalls (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_stalls_rate_population.png">
        <figcaption>Number of stalls (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_stalls_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_rate_population.png
       :width: 70%
       :align: center

       Number of stalls (2019) per 10,000 population, by district




Number of stalls (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of stalls within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of stalls (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_stalls_rate_household.png">
        <figcaption>Number of stalls (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_stalls_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_stalls_rate_household.png
       :width: 70%
       :align: center

       Number of stalls (2019) per 10,000 household, by district




Number of markets (2019)
>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (2019), by district" src="./../png/bangkok_ind_district_markets.png">
        <figcaption>Number of markets (2019), by district.         <a href="./../html/bangkok_ind_district_markets.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets.png
       :width: 70%
       :align: center

       Number of markets (2019), by district




Number of markets (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (2019) per km², by district" src="./../png/bangkok_ind_district_markets_rate_area.png">
        <figcaption>Number of markets (2019) per km², by district.         <a href="./../html/bangkok_ind_district_markets_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_rate_area.png
       :width: 70%
       :align: center

       Number of markets (2019) per km², by district




Number of markets (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_markets_rate_population.png">
        <figcaption>Number of markets (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_markets_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_rate_population.png
       :width: 70%
       :align: center

       Number of markets (2019) per 10,000 population, by district




Number of markets (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of markets within each analysis area was recorded.  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of markets (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_markets_rate_household.png">
        <figcaption>Number of markets (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_markets_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_markets_rate_household.png
       :width: 70%
       :align: center

       Number of markets (2019) per 10,000 household, by district




Dataset: Sidewalk hawkers
-------------------------

Data comprising counts of permitted sidewalk locations for hawkers/stalls, and the number of hawkers and stalls for each district were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Department of City Law Enforcement, BMA``

**Publication year**: ``2019``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20191204``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20191204/transfer_1815197_files_51cc5a2c/3_BKK_sidewalk_hawkers - stalls _2019 _kn20190923.xlsx``


Permitted sidewalk hawker/stall locations (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of permitted sidewalk points for hawker/stall locations was recorded

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Permitted sidewalk hawker/stall locations (2019), by district" src="./../png/bangkok_ind_district_hawker_permitted_locations.png">
        <figcaption>Permitted sidewalk hawker/stall locations (2019), by district.         <a href="./../html/bangkok_ind_district_hawker_permitted_locations.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_hawker_permitted_locations.png
       :width: 70%
       :align: center

       Permitted sidewalk hawker/stall locations (2019), by district




Permitted sidewalk hawker/stall locations (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of permitted sidewalk points for hawker/stall locations was recorded  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Permitted sidewalk hawker/stall locations (2019) per km², by district" src="./../png/bangkok_ind_district_hawker_permitted_locations_rate_area.png">
        <figcaption>Permitted sidewalk hawker/stall locations (2019) per km², by district.         <a href="./../html/bangkok_ind_district_hawker_permitted_locations_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_hawker_permitted_locations_rate_area.png
       :width: 70%
       :align: center

       Permitted sidewalk hawker/stall locations (2019) per km², by district




Permitted sidewalk hawker/stall locations (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of permitted sidewalk points for hawker/stall locations was recorded  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Permitted sidewalk hawker/stall locations (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_hawker_permitted_locations_rate_population.png">
        <figcaption>Permitted sidewalk hawker/stall locations (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_hawker_permitted_locations_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_hawker_permitted_locations_rate_population.png
       :width: 70%
       :align: center

       Permitted sidewalk hawker/stall locations (2019) per 10,000 population, by district




Permitted sidewalk hawker/stall locations (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of permitted sidewalk points for hawker/stall locations was recorded  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Permitted sidewalk hawker/stall locations (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_hawker_permitted_locations_rate_household.png">
        <figcaption>Permitted sidewalk hawker/stall locations (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_hawker_permitted_locations_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_hawker_permitted_locations_rate_household.png
       :width: 70%
       :align: center

       Permitted sidewalk hawker/stall locations (2019) per 10,000 household, by district




Dataset: Food quality tests
---------------------------

Data on food quality testing across 50 Bangkok districts between October 2018 to July 2019  were acquired from the BMA Health Department.  The data was comprised of spreadsheets detailing the number of food establishments, and for each of 9 key quality stanards, the number of tests conducted and the number of tests which did not pass: การตรวจด้านกายภาพ Physical examination; ฟอร์มาลิน formalin; สารฟอกขาว Bleach; สารกันรา Mold; ยาฆ่าแมลง Insecticide; สีสังเคราะห์ Synthetic color; สารโพลาร์ Polar substance; กรดแร่อิสระ Free mineral acid; and ไอโอเดท Iodate.

**Data source**: ``Health Department BMA``

**Publication year**: ``2019``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20191204``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20191204/transfer_1815206_files_409fa2da/BKK_ Food quality testing_2018_19_kn20191114.xlsx``


Food quality tests (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>

The total number of tests conducted across all 9 health and hygeine standards in each district were summed.  Not all tests were conducted in all districts, and some had low sampling; for example,  Wang Thonglang (481 establishments) had zero samples taken for two tests (synthetic color, and free mineral acid), and Khan Na Yao (281 establishments) had only 1 sample recorded for insecticide.  On the other hand, some other districts had a high ratio of tests to establishments.  This data context is important to remember when interpreting the data (for example, out of 1/1592 samples in Chatuchak did not pass insecticide quality standard testing, and so for this standard the target of 100% was not achieved; the comparison with Khan Na Yao where 1/1 tests passed does not in itself provide a fair comparison for food quality in the two districts).

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Food quality tests (2019), by district" src="./../png/bangkok_ind_district_food_qual_test_count.png">
        <figcaption>Food quality tests (2019), by district.         <a href="./../html/bangkok_ind_district_food_qual_test_count.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_food_qual_test_count.png
       :width: 70%
       :align: center

       Food quality tests (2019), by district




Food quality tests (2019) per km²
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total number of tests conducted across all 9 health and hygeine standards in each district were summed.  Not all tests were conducted in all districts, and some had low sampling; for example,  Wang Thonglang (481 establishments) had zero samples taken for two tests (synthetic color, and free mineral acid), and Khan Na Yao (281 establishments) had only 1 sample recorded for insecticide.  On the other hand, some other districts had a high ratio of tests to establishments.  This data context is important to remember when interpreting the data (for example, out of 1/1592 samples in Chatuchak did not pass insecticide quality standard testing, and so for this standard the target of 100% was not achieved; the comparison with Khan Na Yao where 1/1 tests passed does not in itself provide a fair comparison for food quality in the two districts).  The indicator was rated as the rate per km².

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Food quality tests (2019) per km², by district" src="./../png/bangkok_ind_district_food_qual_test_count_rate_area.png">
        <figcaption>Food quality tests (2019) per km², by district.         <a href="./../html/bangkok_ind_district_food_qual_test_count_rate_area.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_food_qual_test_count_rate_area.png
       :width: 70%
       :align: center

       Food quality tests (2019) per km², by district




Food quality tests (2019) per 10,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total number of tests conducted across all 9 health and hygeine standards in each district were summed.  Not all tests were conducted in all districts, and some had low sampling; for example,  Wang Thonglang (481 establishments) had zero samples taken for two tests (synthetic color, and free mineral acid), and Khan Na Yao (281 establishments) had only 1 sample recorded for insecticide.  On the other hand, some other districts had a high ratio of tests to establishments.  This data context is important to remember when interpreting the data (for example, out of 1/1592 samples in Chatuchak did not pass insecticide quality standard testing, and so for this standard the target of 100% was not achieved; the comparison with Khan Na Yao where 1/1 tests passed does not in itself provide a fair comparison for food quality in the two districts).  The indicator was rated as the rate per 10,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Food quality tests (2019) per 10,000 population, by district" src="./../png/bangkok_ind_district_food_qual_test_count_rate_population.png">
        <figcaption>Food quality tests (2019) per 10,000 population, by district.         <a href="./../html/bangkok_ind_district_food_qual_test_count_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_food_qual_test_count_rate_population.png
       :width: 70%
       :align: center

       Food quality tests (2019) per 10,000 population, by district




Food quality tests (2019) per 10,000 household
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total number of tests conducted across all 9 health and hygeine standards in each district were summed.  Not all tests were conducted in all districts, and some had low sampling; for example,  Wang Thonglang (481 establishments) had zero samples taken for two tests (synthetic color, and free mineral acid), and Khan Na Yao (281 establishments) had only 1 sample recorded for insecticide.  On the other hand, some other districts had a high ratio of tests to establishments.  This data context is important to remember when interpreting the data (for example, out of 1/1592 samples in Chatuchak did not pass insecticide quality standard testing, and so for this standard the target of 100% was not achieved; the comparison with Khan Na Yao where 1/1 tests passed does not in itself provide a fair comparison for food quality in the two districts).  The indicator was rated as the rate per 10,000 household.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Food quality tests (2019) per 10,000 household, by district" src="./../png/bangkok_ind_district_food_qual_test_count_rate_household.png">
        <figcaption>Food quality tests (2019) per 10,000 household, by district.         <a href="./../html/bangkok_ind_district_food_qual_test_count_rate_household.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_food_qual_test_count_rate_household.png
       :width: 70%
       :align: center

       Food quality tests (2019) per 10,000 household, by district




Percentage of food standards (/9) with 100% test pass rate (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Percentage of food health and hygiene standards  (/9) with 100% of samples passing quality testing was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Percentage of food standards (/9) with 100% test pass rate (2019), by district" src="./../png/bangkok_ind_district_food_qual_pct_standards_100pct.png">
        <figcaption>Percentage of food standards (/9) with 100% test pass rate (2019), by district.         <a href="./../html/bangkok_ind_district_food_qual_pct_standards_100pct.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_food_qual_pct_standards_100pct.png
       :width: 70%
       :align: center

       Percentage of food standards (/9) with 100% test pass rate (2019), by district




High quality education and schools
||||||||||||||||||||||||||||||||||

โรงเรียนและการศึกษาที่มีคุณภาพสูง

Good quality education means that all learners learn the value of humanity, have the knowledge needed to make an impact in improving the quality of life and well-being of each individual, as well as participating in sustainable social and economic development.   Important basic education encompasses an acceptable level of literacy and numeracy, basic scientific knowledge as well as life skills, including awareness and disease prevention.  Note: the secondary schools are not under the BMA’s responsibility.


Dataset: BMA School locations
-----------------------------

Data on locations of BMA primary schools (2016) was cleaned, such that it represented counts by subdistrict, and associated with district and subdistrict area linkage identifiers

**Data source**: ``Education Department, BMA``

**Publication year**: ``2019``

**Target year**: ``2016``

**Acquisition date (yyyymmdd)**: ``20191204``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20191204/transfer_1815206_files_409fa2da/V3_BMA schools _location_subdistrict_kn 20191203.xlsx``


Number of primary schools (2016)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total count of BMA primary schools was calculated for each district and subdistrict.  District estimates were derived by summing the subdistrict counts.  Primary school counts were considered relative to area population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of primary schools (2016), by subdistrict" src="./../png/bangkok_ind_subdistrict_schools_primary_count.png">
        <figcaption>Number of primary schools (2016), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_schools_primary_count.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_schools_primary_count.png
       :width: 70%
       :align: center

       Number of primary schools (2016), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of primary schools (2016), by district" src="./../png/bangkok_ind_district_schools_primary_count.png">
        <figcaption>Number of primary schools (2016), by district.         <a href="./../html/bangkok_ind_district_schools_primary_count.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_schools_primary_count.png
       :width: 70%
       :align: center

       Number of primary schools (2016), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=primary schools by population src="./../svg/plots/district_schools_primary_count_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=primary schools by population per sqkm src="./../svg/plots/district_schools_primary_count_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=primary schools, ranked in ascending order src="./../svg/plots/district_schools_primary_count.svg">
            </div>
       <figcaption>Figures for Number Of Primary Schools (2016) with regard to primary schools by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_count_population.pdf
      :width: 48%
      :align: center

      Scatterplot of primary schools by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_count_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of primary schools by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_count.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by primary schools with regard to number of primary schools (2016).




Number of primary schools (2016) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The total count of BMA primary schools was calculated for each district and subdistrict.  District estimates were derived by summing the subdistrict counts.  Primary school counts were considered relative to area population.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of primary schools (2016) per 1,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_schools_primary_count_rate_population.png">
        <figcaption>Number of primary schools (2016) per 1,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_schools_primary_count_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_schools_primary_count_rate_population.png
       :width: 70%
       :align: center

       Number of primary schools (2016) per 1,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of primary schools (2016) per 1,000 population, by district" src="./../png/bangkok_ind_district_schools_primary_count_rate_population.png">
        <figcaption>Number of primary schools (2016) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_schools_primary_count_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_schools_primary_count_rate_population.png
       :width: 70%
       :align: center

       Number of primary schools (2016) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=primary schools by population src="./../svg/plots/district_schools_primary_count_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=primary schools by population per sqkm src="./../svg/plots/district_schools_primary_count_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=primary schools, ranked in ascending order src="./../svg/plots/district_schools_primary_count_rate_population.svg">
            </div>
       <figcaption>Figures for Number Of Primary Schools (2016) Per 1,000 Population with regard to primary schools by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_count_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of primary schools by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_count_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of primary schools by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_count_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by primary schools with regard to number of primary schools (2016) per 1,000 population.




Dataset: O-Net in BMA schools
-----------------------------

Data on the district average score of the test results of the National General Education (O-NET) for level 6 primary school students across four core subjects (Thai, mathematics, science and English) was cleaned and associated with area linkage codes.

**Data source**: ``Education Department, BMA``

**Publication year**: ``2019``

**Target year**: ``2016``

**Acquisition date (yyyymmdd)**: ``20200511``

**Licence**: ``none specified``

**Date type**: ``numeric``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20200511/O-NET in BMA schools Academic year 2018 __  only primalt level 6 _kn20200508.xlsx``


Average National General Education (O-NET) score for BMA primary schools for each of four core subjects (Thai, mathematics, science and English; 2016)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average across all four core subject scores for each district was taken, for evaluation against a target (for individual subjects) of > 50.  There were no districts achieving an average score of greater than 50 in each subject, so the average of the four subjects in each district was taken as an alternative continuous indicator.  Only Chatuchak (6 schools) achieved an overall average of greater than 50.  However, it should be noted that district averages do not necessarily reflect individual school performance (some districts have more than 20 schools), and within schools it is expected that there may be considerable heterogeneity.  Furthermore, estimates of the average score may be influenced by poor performing outlying students, and alternate measures such as the median may be more appropriate as a summary of central tendency.   As such, it is recommended that these results be interpreted cautiously, with consideration to reviewing the distribution of student results as clustered within schools and districts in more depth.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average National General Education (O-NET) score for BMA primary schools for each of four core subjects (Thai, mathematics, science and English; 2016), by district" src="./../png/bangkok_ind_district_schools_primary_o_net_avg.png">
        <figcaption>Average National General Education (O-NET) score for BMA primary schools for each of four core subjects (Thai, mathematics, science and English; 2016), by district.         <a href="./../html/bangkok_ind_district_schools_primary_o_net_avg.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_schools_primary_o_net_avg.png
       :width: 70%
       :align: center

       Average National General Education (O-NET) score for BMA primary schools for each of four core subjects (Thai, mathematics, science and English; 2016), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=average O-NET by population src="./../svg/plots/district_schools_primary_o_net_avg_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=average O-NET by population per sqkm src="./../svg/plots/district_schools_primary_o_net_avg_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=average O-NET, ranked in ascending order src="./../svg/plots/district_schools_primary_o_net_avg.svg">
            </div>
       <figcaption>Figures for Average National General Education (O-Net) Score For Bma Primary Schools For Each Of Four Core Subjects (Thai, Mathematics, Science And English; 2016) with regard to average O-NET by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_o_net_avg_population.pdf
      :width: 48%
      :align: center

      Scatterplot of average O-NET by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_o_net_avg_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of average O-NET by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_schools_primary_o_net_avg.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by average o-net with regard to average national general education (o-net) score for bma primary schools for each of four core subjects (thai, mathematics, science and english; 2016).




Access to temples, museums, music and other cultural events that provide opportunities for people to come together; Multi-purpose local community centres
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

การเข้าถึงวัด พิพิธภัณฑ์ การจัดงานด้านวัฒนธรรมและดนตรีที่เปิดโอกาสให้ประชาชนมารวมกัน ศูนย์ชุมชนที่ดำเนินการด้วยวัตถุประสงค์หลากหลาย

Access to cultural facilities means that people have access to various locations for increasing their happiness and promoting good actions. Such places or facilities include religious sites, museums, theaters, arts and craft centers, theatre, as well as cultural and music events in communities or neighborhoods.


Dataset: BMA Places of Worship
------------------------------

Data on counts of places of worship (Temples; Mosques; Christian, Hindu and Sikh churches; and Shrines ) were cleaned and associated with area linkage codes.

**Data source**: ``Buddhism Division, National Buddhism Office; BMA district offices``

**Publication year**: ``2019``

**Target year**: ``2014``

**Acquisition date (yyyymmdd)**: ``20190930``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190930/transfer_1730651_files_296a713c/number of worship places 2014 by district _kn20190929.xlsx``


Number of temples (2014)
>>>>>>>>>>>>>>>>>>>>>>>>

The count of temples recorded in each district was recorded, and evaluated with regard to population for each district.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of temples (2014), by district" src="./../png/bangkok_ind_district_temples.png">
        <figcaption>Number of temples (2014), by district.         <a href="./../html/bangkok_ind_district_temples.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_temples.png
       :width: 70%
       :align: center

       Number of temples (2014), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Temples by population src="./../svg/plots/district_temples_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Temples by population per sqkm src="./../svg/plots/district_temples_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Temples, ranked in ascending order src="./../svg/plots/district_temples.svg">
            </div>
       <figcaption>Figures for Number Of Temples (2014) with regard to Temples by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_temples_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Temples by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_temples_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Temples by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_temples.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by temples with regard to number of temples (2014).




Number of temples (2014) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of temples recorded in each district was recorded, and evaluated with regard to population for each district.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of temples (2014) per 1,000 population, by district" src="./../png/bangkok_ind_district_temples_rate_population.png">
        <figcaption>Number of temples (2014) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_temples_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_temples_rate_population.png
       :width: 70%
       :align: center

       Number of temples (2014) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Temples by population src="./../svg/plots/district_temples_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Temples by population per sqkm src="./../svg/plots/district_temples_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Temples, ranked in ascending order src="./../svg/plots/district_temples_rate_population.svg">
            </div>
       <figcaption>Figures for Number Of Temples (2014) Per 1,000 Population with regard to Temples by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_temples_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Temples by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_temples_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Temples by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_temples_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by temples with regard to number of temples (2014) per 1,000 population.




Dataset: BMA Libraries and Museums
----------------------------------

Data on counts of libraries and museums by district and subdistrict were cleaned and associated with area linkage codes.

**Data source**: ``Culture, Sports and Tourism Department BMA``

**Publication year**: ``2018``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190911``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190911/transfer_1710171_files_127133c5/Library and Museum BKK 2018_kn082419.xlsx``


Number of museums (2018)
>>>>>>>>>>>>>>>>>>>>>>>>

The count of temples recorded in each subdistrict were tallied for districts and subdistricts, and evaluated with regard to population for each district.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of museums (2018), by subdistrict" src="./../png/bangkok_ind_subdistrict_museums.png">
        <figcaption>Number of museums (2018), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_museums.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_museums.png
       :width: 70%
       :align: center

       Number of museums (2018), by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of museums (2018), by district" src="./../png/bangkok_ind_district_museums.png">
        <figcaption>Number of museums (2018), by district.         <a href="./../html/bangkok_ind_district_museums.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_museums.png
       :width: 70%
       :align: center

       Number of museums (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Number of Museums by population src="./../svg/plots/district_museums_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Number of Museums by population per sqkm src="./../svg/plots/district_museums_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Number of Museums, ranked in ascending order src="./../svg/plots/district_museums.svg">
            </div>
       <figcaption>Figures for Number Of Museums (2018) with regard to Number of Museums by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_museums_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of Museums by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_museums_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of Museums by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_museums.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by number of museums with regard to number of museums (2018).




Number of museums (2018) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The count of temples recorded in each subdistrict were tallied for districts and subdistricts, and evaluated with regard to population for each district.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of museums (2018) per 1,000 population, by subdistrict" src="./../png/bangkok_ind_subdistrict_museums_rate_population.png">
        <figcaption>Number of museums (2018) per 1,000 population, by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_museums_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_museums_rate_population.png
       :width: 70%
       :align: center

       Number of museums (2018) per 1,000 population, by subdistrict







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of museums (2018) per 1,000 population, by district" src="./../png/bangkok_ind_district_museums_rate_population.png">
        <figcaption>Number of museums (2018) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_museums_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_museums_rate_population.png
       :width: 70%
       :align: center

       Number of museums (2018) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Number of Museums by population src="./../svg/plots/district_museums_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Number of Museums by population per sqkm src="./../svg/plots/district_museums_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Number of Museums, ranked in ascending order src="./../svg/plots/district_museums_rate_population.svg">
            </div>
       <figcaption>Figures for Number Of Museums (2018) Per 1,000 Population with regard to Number of Museums by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_museums_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of Museums by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_museums_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Number of Museums by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_museums_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by number of museums with regard to number of museums (2018) per 1,000 population.




Dataset: BMA Youth centers
--------------------------

Data on counts of youth centers, sports centers and sport yards and their usage counts within Bangkok districts (2018) were cleaned and associated with area linkage codes.

**Data source**: ``Culture, Sports and Tourism Department BMA``

**Publication year**: ``2018``

**Target year**: ``2018``

**Acquisition date (yyyymmdd)**: ``20190911``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20190911/transfer_1710171_files_127133c5/Youth centers in Bangkok 2018_kn 20190909.xlsx``


Number of youth centers (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of youth centers was recorded for each district.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of youth centers (2018), by district" src="./../png/bangkok_ind_district_youth_center_count.png">
        <figcaption>Number of youth centers (2018), by district.         <a href="./../html/bangkok_ind_district_youth_center_count.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_youth_center_count.png
       :width: 70%
       :align: center

       Number of youth centers (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Youth centers by population src="./../svg/plots/district_youth_center_count_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Youth centers by population per sqkm src="./../svg/plots/district_youth_center_count_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Youth centers, ranked in ascending order src="./../svg/plots/district_youth_center_count.svg">
            </div>
       <figcaption>Figures for Number Of Youth Centers (2018) with regard to Youth centers by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_count_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth centers by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_count_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth centers by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_count.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by youth centers with regard to number of youth centers (2018).




Number of youth centers (2018) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of youth centers was recorded for each district.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of youth centers (2018) per 1,000 population, by district" src="./../png/bangkok_ind_district_youth_center_count_rate_population.png">
        <figcaption>Number of youth centers (2018) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_youth_center_count_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_youth_center_count_rate_population.png
       :width: 70%
       :align: center

       Number of youth centers (2018) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Youth centers by population src="./../svg/plots/district_youth_center_count_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Youth centers by population per sqkm src="./../svg/plots/district_youth_center_count_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Youth centers, ranked in ascending order src="./../svg/plots/district_youth_center_count_rate_population.svg">
            </div>
       <figcaption>Figures for Number Of Youth Centers (2018) Per 1,000 Population with regard to Youth centers by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_count_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth centers by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_count_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth centers by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_count_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by youth centers with regard to number of youth centers (2018) per 1,000 population.




Visits to youth centers (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of visits to youth centers within each district was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Visits to youth centers (2018), by district" src="./../png/bangkok_ind_district_youth_center_usage.png">
        <figcaption>Visits to youth centers (2018), by district.         <a href="./../html/bangkok_ind_district_youth_center_usage.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_youth_center_usage.png
       :width: 70%
       :align: center

       Visits to youth centers (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Youth center visits by population src="./../svg/plots/district_youth_center_usage_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Youth center visits by population per sqkm src="./../svg/plots/district_youth_center_usage_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Youth center visits, ranked in ascending order src="./../svg/plots/district_youth_center_usage.svg">
            </div>
       <figcaption>Figures for Visits To Youth Centers (2018) with regard to Youth center visits by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_usage_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth center visits by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_usage_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth center visits by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_usage.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by youth center visits with regard to visits to youth centers (2018).




Visits to youth centers (2018) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of visits to youth centers within each district was recorded.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Visits to youth centers (2018) per 1,000 population, by district" src="./../png/bangkok_ind_district_youth_center_usage_rate_population.png">
        <figcaption>Visits to youth centers (2018) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_youth_center_usage_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_youth_center_usage_rate_population.png
       :width: 70%
       :align: center

       Visits to youth centers (2018) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Youth center visits by population src="./../svg/plots/district_youth_center_usage_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Youth center visits by population per sqkm src="./../svg/plots/district_youth_center_usage_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Youth center visits, ranked in ascending order src="./../svg/plots/district_youth_center_usage_rate_population.svg">
            </div>
       <figcaption>Figures for Visits To Youth Centers (2018) Per 1,000 Population with regard to Youth center visits by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_usage_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth center visits by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_usage_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Youth center visits by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_youth_center_usage_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by youth center visits with regard to visits to youth centers (2018) per 1,000 population.




Number of sport centers (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of sport centers was recorded for each district.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of sport centers (2018), by district" src="./../png/bangkok_ind_district_sport_center_count.png">
        <figcaption>Number of sport centers (2018), by district.         <a href="./../html/bangkok_ind_district_sport_center_count.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_center_count.png
       :width: 70%
       :align: center

       Number of sport centers (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport centers by population src="./../svg/plots/district_sport_center_count_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport centers by population per sqkm src="./../svg/plots/district_sport_center_count_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport centers, ranked in ascending order src="./../svg/plots/district_sport_center_count.svg">
            </div>
       <figcaption>Figures for Number Of Sport Centers (2018) with regard to Sport centers by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_count_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport centers by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_count_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport centers by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_count.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport centers with regard to number of sport centers (2018).




Number of sport centers (2018) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of sport centers was recorded for each district.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of sport centers (2018) per 1,000 population, by district" src="./../png/bangkok_ind_district_sport_center_count_rate_population.png">
        <figcaption>Number of sport centers (2018) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_sport_center_count_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_center_count_rate_population.png
       :width: 70%
       :align: center

       Number of sport centers (2018) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport centers by population src="./../svg/plots/district_sport_center_count_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport centers by population per sqkm src="./../svg/plots/district_sport_center_count_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport centers, ranked in ascending order src="./../svg/plots/district_sport_center_count_rate_population.svg">
            </div>
       <figcaption>Figures for Number Of Sport Centers (2018) Per 1,000 Population with regard to Sport centers by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_count_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport centers by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_count_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport centers by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_count_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport centers with regard to number of sport centers (2018) per 1,000 population.




Visits to sport centers (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of visits to sport centers within each district was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Visits to sport centers (2018), by district" src="./../png/bangkok_ind_district_sport_center_usage.png">
        <figcaption>Visits to sport centers (2018), by district.         <a href="./../html/bangkok_ind_district_sport_center_usage.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_center_usage.png
       :width: 70%
       :align: center

       Visits to sport centers (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport center visits by population src="./../svg/plots/district_sport_center_usage_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport center visits by population per sqkm src="./../svg/plots/district_sport_center_usage_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport center visits, ranked in ascending order src="./../svg/plots/district_sport_center_usage.svg">
            </div>
       <figcaption>Figures for Visits To Sport Centers (2018) with regard to Sport center visits by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_usage_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport center visits by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_usage_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport center visits by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_usage.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport center visits with regard to visits to sport centers (2018).




Visits to sport centers (2018) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of visits to sport centers within each district was recorded.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Visits to sport centers (2018) per 1,000 population, by district" src="./../png/bangkok_ind_district_sport_center_usage_rate_population.png">
        <figcaption>Visits to sport centers (2018) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_sport_center_usage_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_center_usage_rate_population.png
       :width: 70%
       :align: center

       Visits to sport centers (2018) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport center visits by population src="./../svg/plots/district_sport_center_usage_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport center visits by population per sqkm src="./../svg/plots/district_sport_center_usage_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport center visits, ranked in ascending order src="./../svg/plots/district_sport_center_usage_rate_population.svg">
            </div>
       <figcaption>Figures for Visits To Sport Centers (2018) Per 1,000 Population with regard to Sport center visits by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_usage_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport center visits by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_usage_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport center visits by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_center_usage_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport center visits with regard to visits to sport centers (2018) per 1,000 population.




Number of sport yards (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of sport yards was recorded for each district.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of sport yards (2018), by district" src="./../png/bangkok_ind_district_sport_yard_count.png">
        <figcaption>Number of sport yards (2018), by district.         <a href="./../html/bangkok_ind_district_sport_yard_count.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_yard_count.png
       :width: 70%
       :align: center

       Number of sport yards (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport yards by population src="./../svg/plots/district_sport_yard_count_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport yards by population per sqkm src="./../svg/plots/district_sport_yard_count_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport yards, ranked in ascending order src="./../svg/plots/district_sport_yard_count.svg">
            </div>
       <figcaption>Figures for Number Of Sport Yards (2018) with regard to Sport yards by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_count_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yards by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_count_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yards by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_count.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport yards with regard to number of sport yards (2018).




Number of sport yards (2018) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of sport yards was recorded for each district.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Number of sport yards (2018) per 1,000 population, by district" src="./../png/bangkok_ind_district_sport_yard_count_rate_population.png">
        <figcaption>Number of sport yards (2018) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_sport_yard_count_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_yard_count_rate_population.png
       :width: 70%
       :align: center

       Number of sport yards (2018) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport yards by population src="./../svg/plots/district_sport_yard_count_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport yards by population per sqkm src="./../svg/plots/district_sport_yard_count_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport yards, ranked in ascending order src="./../svg/plots/district_sport_yard_count_rate_population.svg">
            </div>
       <figcaption>Figures for Number Of Sport Yards (2018) Per 1,000 Population with regard to Sport yards by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_count_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yards by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_count_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yards by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_count_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport yards with regard to number of sport yards (2018) per 1,000 population.




Visits to sport yards (2018)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of visits to sport yards within each district was recorded.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Visits to sport yards (2018), by district" src="./../png/bangkok_ind_district_sport_yard_usage.png">
        <figcaption>Visits to sport yards (2018), by district.         <a href="./../html/bangkok_ind_district_sport_yard_usage.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_yard_usage.png
       :width: 70%
       :align: center

       Visits to sport yards (2018), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport yard visits by population src="./../svg/plots/district_sport_yard_usage_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport yard visits by population per sqkm src="./../svg/plots/district_sport_yard_usage_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport yard visits, ranked in ascending order src="./../svg/plots/district_sport_yard_usage.svg">
            </div>
       <figcaption>Figures for Visits To Sport Yards (2018) with regard to Sport yard visits by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_usage_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yard visits by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_usage_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yard visits by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_usage.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport yard visits with regard to visits to sport yards (2018).




Visits to sport yards (2018) per 1,000 population
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The number of visits to sport yards within each district was recorded.  The indicator was rated as the rate per 1,000 population.

Aligns with Sustainable Development Goals: 2.1, 3, 11.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Visits to sport yards (2018) per 1,000 population, by district" src="./../png/bangkok_ind_district_sport_yard_usage_rate_population.png">
        <figcaption>Visits to sport yards (2018) per 1,000 population, by district.         <a href="./../html/bangkok_ind_district_sport_yard_usage_rate_population.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_sport_yard_usage_rate_population.png
       :width: 70%
       :align: center

       Visits to sport yards (2018) per 1,000 population, by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Sport yard visits by population src="./../svg/plots/district_sport_yard_usage_rate_population_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Sport yard visits by population per sqkm src="./../svg/plots/district_sport_yard_usage_rate_population_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Sport yard visits, ranked in ascending order src="./../svg/plots/district_sport_yard_usage_rate_population.svg">
            </div>
       <figcaption>Figures for Visits To Sport Yards (2018) Per 1,000 Population with regard to Sport yard visits by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_usage_rate_population_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yard visits by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_usage_rate_population_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Sport yard visits by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_sport_yard_usage_rate_population.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by sport yard visits with regard to visits to sport yards (2018) per 1,000 population.




Opportunity to earn a fair wage
|||||||||||||||||||||||||||||||

โอกาสในการมีรายได้จากการทำงานอย่างยุติธรรม

Wage means the money agreed upon by an employer and employees to be paid in compensation for normal working hours according to the employment contract.  The wage may be paid on a periodic basis, or according to the work done by the employee during normal working hours of the working day.  The wage includes the money that an employer pays to an employee on holidays and days off for which the employee does not work.  Fair wage means the wage rate for an employee under the national wage laws, such as the minimum wage, overtime pay, holiday pay, social security payment, etc.  Cost of living means the cost of a person or goods used to purchase goods and services according to the type and quantity needed for living, such as home expenses.  


Dataset: Poverty Indicators 2017
--------------------------------

The data table "Poverty Indicators 2017: Cost Dimensions with records for Bangkok overall, districts, and subdistricts" was retrieved from the Thai National Statistical Office (NSO).  Data were cleaned for processing and aligned with area IDs.  

**Data source**: ``National Statistical Office``

**URL**: ``http://www.nso.go.th/sites/2014/DocLib8/2560/central/urban/10_bangkok.xls``

**Publication year**: ``2018``

**Target year**: ``2017``

**Acquisition date (yyyymmdd)**: ``20180121``

**Licence**: ``none specified``

**Date type**: ``numeric``

**Scale / Resolution**: ``area summary``

**Notes**: ``The source data table also includes standard error as a measure of precision for each area estimate``

**Data location relative to project folder**: ``./data/Thai/National Statistical Office/2017 poverty index/NSO_Bangkok_2017_poverty_index_en_cleaned.xlsx``


Average monthly cost of living per person (Baht; 2017)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The average monthly cost of living per person within each analysis area was recorded.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average monthly cost of living per person (Baht; 2017), by district" src="./../png/bangkok_ind_district_cost_of_living_district.png">
        <figcaption>Average monthly cost of living per person (Baht; 2017), by district.         <a href="./../html/bangkok_ind_district_cost_of_living_district.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_cost_of_living_district.png
       :width: 70%
       :align: center

       Average monthly cost of living per person (Baht; 2017), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Average monthly cost of living per person (Baht; NSO, 2017) by population src="./../svg/plots/district_cost_of_living_district_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Average monthly cost of living per person (Baht; NSO, 2017) by population per sqkm src="./../svg/plots/district_cost_of_living_district_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Average monthly cost of living per person (Baht; NSO, 2017), ranked in ascending order src="./../svg/plots/district_cost_of_living_district.svg">
            </div>
       <figcaption>Figures for Average Monthly Cost Of Living Per Person (Baht; 2017) with regard to Average monthly cost of living per person (Baht; NSO, 2017) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_cost_of_living_district_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Average monthly cost of living per person (Baht; NSO, 2017) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_cost_of_living_district_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Average monthly cost of living per person (Baht; NSO, 2017) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_cost_of_living_district.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by average monthly cost of living per person (baht; nso, 2017) with regard to average monthly cost of living per person (baht; 2017).







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Average monthly cost of living per person (Baht; 2017), by subdistrict" src="./../png/bangkok_ind_subdistrict_cost_of_living_subdistrict.png">
        <figcaption>Average monthly cost of living per person (Baht; 2017), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_cost_of_living_subdistrict.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_cost_of_living_subdistrict.png
       :width: 70%
       :align: center

       Average monthly cost of living per person (Baht; 2017), by subdistrict




Social development
~~~~~~~~~~~~~~~~~~


Opportunity to earn a fair wage
|||||||||||||||||||||||||||||||

โอกาสในการมีรายได้จากการทำงานอย่างยุติธรรม

Wage means the money agreed upon by an employer and employees to be paid in compensation for normal working hours according to the employment contract.  The wage may be paid on a periodic basis, or according to the work done by the employee during normal working hours of the working day.  The wage includes the money that an employer pays to an employee on holidays and days off for which the employee does not work.  Fair wage means the wage rate for an employee under the national wage laws, such as the minimum wage, overtime pay, holiday pay, social security payment, etc.  Cost of living means the cost of a person or goods used to purchase goods and services according to the type and quantity needed for living, such as home expenses.  


Dataset: Poverty Indicators 2017
--------------------------------

The data table "Poverty Indicators 2017: Cost Dimensions with records for Bangkok overall, districts, and subdistricts" was retrieved from the Thai National Statistical Office (NSO).  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``National Statistical Office``

**URL**: ``http://www.nso.go.th/sites/2014/DocLib8/2560/central/urban/10_bangkok.xls``

**Publication year**: ``2018``

**Target year**: ``2017``

**Acquisition date (yyyymmdd)**: ``20180121``

**Licence**: ``none specified``

**Date type**: ``integer``

**Scale / Resolution**: ``area summary``

**Notes**: ``The source data table also includes standard error as a measure of precision for each area estimate``

**Data location relative to project folder**: ``./data/Thai/National Statistical Office/2017 poverty index/NSO_Bangkok_2017_poverty_index_en_cleaned.xlsx``


Coefficient of inequality (2017)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The coefficient of inequality within each analysis area was recorded.  Also known as the Gini coefficient, this is defined as a ratio between 0 and 1 and is here expressed as a percentage. A low Gini coefficient is suggestive of equality in income distribution. Higher values are indicative of an increasingly disparate income distribution.  Expressed as a percentage,  0 means absolute equality (Everyone has the same income) and 100 means complete inequality.   The Gini coefficient calculation is based on the assumption that no one has a lower income than zero.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="Coefficient of inequality (2017), by district" src="./../png/bangkok_ind_district_inequality_district.png">
        <figcaption>Coefficient of inequality (2017), by district.         <a href="./../html/bangkok_ind_district_inequality_district.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_inequality_district.png
       :width: 70%
       :align: center

       Coefficient of inequality (2017), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Coefficient of inequality (NSO, 2017) by population src="./../svg/plots/district_inequality_district_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Coefficient of inequality (NSO, 2017) by population per sqkm src="./../svg/plots/district_inequality_district_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Coefficient of inequality (NSO, 2017), ranked in ascending order src="./../svg/plots/district_inequality_district.svg">
            </div>
       <figcaption>Figures for Coefficient Of Inequality (2017) with regard to Coefficient of inequality (NSO, 2017) by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_inequality_district_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Coefficient of inequality (NSO, 2017) by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_inequality_district_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Coefficient of inequality (NSO, 2017) by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_inequality_district.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by coefficient of inequality (nso, 2017) with regard to coefficient of inequality (2017).







.. only:: html

    .. raw:: html

        <figure>
        <img alt="Coefficient of inequality (2017), by subdistrict" src="./../png/bangkok_ind_subdistrict_inequality_subdistrict.png">
        <figcaption>Coefficient of inequality (2017), by subdistrict.         <a href="./../html/bangkok_ind_subdistrict_inequality_subdistrict.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_subdistrict_inequality_subdistrict.png
       :width: 70%
       :align: center

       Coefficient of inequality (2017), by subdistrict




Local employment opportunities
||||||||||||||||||||||||||||||

โอกาสในการทำงานในท้องถิ่น

Local job opportunities mean that the people living in an area can expect or assess whether there will be work in that area where they live.


Dataset: Taxes collected
------------------------

Data at district level were prepared by the Bangkok Metropolitan Administration and supplied as an Excel workbook.  The data comprised sample point records of actual revenue by taxes collected by BMA district offices for the fiscale year of 2019, source dfrom the BMA Finance Department in October 2019.  Data were cleaned for processing and aligned with area IDs. 

**Data source**: ``Finance Department, BMA``

**Publication year**: ``2019``

**Target year**: ``2019``

**Acquisition date (yyyymmdd)**: ``20190617``

**Licence**: ``none specified``

**Date type**: ``float``

**Scale / Resolution**: ``area summary``

**Data location relative to project folder**: ``./data/Thai/_from BMA/20191204/transfer_1815206_files_409fa2da/BKK_taxes_district_19 _kn20191201.xlsx``


The percentage contribution of local taxes to overall BMA tax revenue (2019)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

The percentage contribution of local taxes to BMA's overall tax revenue for 2019 was calculated by dividing the total revenue for each district (sum of house and building taxes, local development taxes, and signboard taxes) by the contribution from local deveopment taxes and multiplying this by 100.

Aligns with Sustainable Development Goals: 3, 6, 9, 11, 12, 14.






.. only:: html

    .. raw:: html

        <figure>
        <img alt="The percentage contribution of local taxes to overall BMA tax revenue (2019), by district" src="./../png/bangkok_ind_district_percent_bma_income_from_local_taxes.png">
        <figcaption>The percentage contribution of local taxes to overall BMA tax revenue (2019), by district.         <a href="./../html/bangkok_ind_district_percent_bma_income_from_local_taxes.html" target="_blank">Open interactive map in new tab</a><br></figcaption>
        </figure><br>

.. only:: latex

    .. figure:: ../maps/bangkok_thailand_2018/png/bangkok_ind_district_percent_bma_income_from_local_taxes.png
       :width: 70%
       :align: center

       The percentage contribution of local taxes to overall BMA tax revenue (2019), by district







.. only:: html

    .. raw:: html

        <div id="plot-div">
            <div id="div1" class="plot-box">
        	     <img alt=Local Development Taxes by population src="./../svg/plots/district_percent_bma_income_from_local_taxes_population.svg" class="plot-img">
            </div>
            <div id="div2" class="plot-box">
        	     <img alt=Local Development Taxes by population per sqkm src="./../svg/plots/district_percent_bma_income_from_local_taxes_population_per_sqkm.svg" class="plot-img">
            </div><br>
       </div><br>
       <div>
            <div id="div3" class="plot-box-large">
        	     <img alt=Local Development Taxes, ranked in ascending order src="./../svg/plots/district_percent_bma_income_from_local_taxes.svg">
            </div>
       <figcaption>Figures for The Percentage Contribution Of Local Taxes To Overall Bma Tax Revenue (2019) with regard to Local Development Taxes by district, clockwise from top: by population; by population per sqkm; districts ranked in ascending order..</figcaption>

       </div><br>

.. only:: latex

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percent_bma_income_from_local_taxes_population.pdf
      :width: 48%
      :align: center

      Scatterplot of Local Development Taxes by population for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percent_bma_income_from_local_taxes_population_per_sqkm.pdf
      :width: 48%
      :align: center

      Scatterplot of Local Development Taxes by population density for districts.

   .. figure:: ../maps/bangkok_thailand_2018/pdf/plots/district_percent_bma_income_from_local_taxes.pdf
      :width: 100%
      :align: center

      Districts ranked in ascending order by local development taxes with regard to the percentage contribution of local taxes to overall bma tax revenue (2019).



