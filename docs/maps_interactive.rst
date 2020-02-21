Interactive maps
================

.. only:: html

    .. raw:: html

        <form name="change">
        <SELECT NAME="options" ONCHANGE="document.getElementById('maps_interactive').src = './../html/'+this.options[this.selectedIndex].value+'.html'">
        <option value="bangkok_02_population_subdistrict_population_per_sqkm">Please select a map to explore...</option>
        <option value="bangkok_ind_district_fire_incidence">สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018): fire incidence</option>
        <option value="bangkok_ind_district_fire_incidence_rate_area">สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per km²: fire incidence</option>
        <option value="bangkok_ind_district_fire_incidence_rate_population">สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 population: fire incidence</option>
        <option value="bangkok_ind_district_fire_incidence_rate_household">สถิติอัคคีภัยจำแนกตามพื้นที่เขตในกรุงเทพมหานคร ปี 2561 (Fire Incidence in Bangkok 2018) per 10,000 household: fire incidence</option>
        <option value="bangkok_ind_subdistrict_health_centres">Health centers (n = 68): health centers</option>
        <option value="bangkok_ind_subdistrict_health_centres_rate_area">Health centers (n = 68) per km²: health centers</option>
        <option value="bangkok_ind_subdistrict_health_centres_rate_population">Health centers (n = 68) per 10,000 population: health centers</option>
        <option value="bangkok_ind_subdistrict_health_centres_rate_household">Health centers (n = 68) per 10,000 household: health centers</option>
        <option value="bangkok_ind_district_health_centres">Health centers (n = 68): health centers</option>
        <option value="bangkok_ind_district_health_centres_rate_area">Health centers (n = 68) per km²: health centers</option>
        <option value="bangkok_ind_district_health_centres_rate_population">Health centers (n = 68) per 10,000 population: health centers</option>
        <option value="bangkok_ind_district_health_centres_rate_household">Health centers (n = 68) per 10,000 household: health centers</option>
        <option value="bangkok_ind_subdistrict_main_road_flood_days_flood">14 flood areas of main roads in Bangkok Year 2018: days of flooding</option>
        <option value="bangkok_ind_district_main_road_flood_days_flood">14 flood areas of main roads in Bangkok Year 2018: days of flooding</option>
        <option value="bangkok_ind_subdistrict_main_road_flood_days_rain">14 flood areas of main roads in Bangkok Year 2018: days of rain</option>
        <option value="bangkok_ind_district_main_road_flood_days_rain">14 flood areas of main roads in Bangkok Year 2018: days of rain</option>
        <option value="bangkok_ind_subdistrict_main_road_flood_intensity">14 flood areas of main roads in Bangkok Year 2018: maximum intensity</option>
        <option value="bangkok_ind_district_main_road_flood_intensity">14 flood areas of main roads in Bangkok Year 2018: maximum intensity</option>
        <option value="bangkok_ind_subdistrict_main_road_flood_locations">14 flood areas of main roads in Bangkok Year 2018: main road flood locations</option>
        <option value="bangkok_ind_subdistrict_main_road_flood_locations_rate_area">14 flood areas of main roads in Bangkok Year 2018 per km²: main road flood locations</option>
        <option value="bangkok_ind_subdistrict_main_road_flood_locations_rate_population">14 flood areas of main roads in Bangkok Year 2018 per 10,000 population: main road flood locations</option>
        <option value="bangkok_ind_subdistrict_main_road_flood_locations_rate_household">14 flood areas of main roads in Bangkok Year 2018 per 10,000 household: main road flood locations</option>
        <option value="bangkok_ind_district_main_road_flood_locations">14 flood areas of main roads in Bangkok Year 2018: main road flood locations</option>
        <option value="bangkok_ind_district_main_road_flood_locations_rate_area">14 flood areas of main roads in Bangkok Year 2018 per km²: main road flood locations</option>
        <option value="bangkok_ind_district_main_road_flood_locations_rate_population">14 flood areas of main roads in Bangkok Year 2018 per 10,000 population: main road flood locations</option>
        <option value="bangkok_ind_district_main_road_flood_locations_rate_household">14 flood areas of main roads in Bangkok Year 2018 per 10,000 household: main road flood locations</option>
        <option value="bangkok_ind_district_markets">Number of food entrepreneurs: ตลาด/Market</option>
        <option value="bangkok_ind_district_markets_rate_area">Number of food entrepreneurs per km²: ตลาด/Market</option>
        <option value="bangkok_ind_district_markets_rate_population">Number of food entrepreneurs per 10,000 population: ตลาด/Market</option>
        <option value="bangkok_ind_district_markets_rate_household">Number of food entrepreneurs per 10,000 household: ตลาด/Market</option>
        <option value="bangkok_ind_district_minimarts">Number of food entrepreneurs: มินิมาร์ท/Mini-mart</option>
        <option value="bangkok_ind_district_minimarts_rate_area">Number of food entrepreneurs per km²: มินิมาร์ท/Mini-mart</option>
        <option value="bangkok_ind_district_minimarts_rate_population">Number of food entrepreneurs per 10,000 population: มินิมาร์ท/Mini-mart</option>
        <option value="bangkok_ind_district_minimarts_rate_household">Number of food entrepreneurs per 10,000 household: มินิมาร์ท/Mini-mart</option>
        <option value="bangkok_ind_subdistrict_no2_2017_18_mean">Air quality: Annual average NO₂ (1-e6 mmol/m²; 2017-18)</option>
        <option value="bangkok_ind_district_no2_2017_18_mean">Air quality: Annual average NO₂ (1-e6 mmol/m²; 2017-18)</option>
        <option value="bangkok_ind_subdistrict_outpatients_combined_diseases">Health center outpatients: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_combined_diseases_rate_area">Health center outpatients per km²: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_combined_diseases_rate_population">Health center outpatients per 10,000 population: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_combined_diseases_rate_household">Health center outpatients per 10,000 household: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_district_outpatients_combined_diseases">Health center outpatients: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_district_outpatients_combined_diseases_rate_area">Health center outpatients per km²: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_district_outpatients_combined_diseases_rate_population">Health center outpatients per 10,000 population: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_district_outpatients_combined_diseases_rate_household">Health center outpatients per 10,000 household: vital diseases (combined; 2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_diabetes">Health center outpatients: diabetes (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_diabetes_rate_area">Health center outpatients per km²: diabetes (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_diabetes_rate_population">Health center outpatients per 10,000 population: diabetes (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_diabetes_rate_household">Health center outpatients per 10,000 household: diabetes (2018)</option>
        <option value="bangkok_ind_district_outpatients_diabetes">Health center outpatients: diabetes (2018)</option>
        <option value="bangkok_ind_district_outpatients_diabetes_rate_area">Health center outpatients per km²: diabetes (2018)</option>
        <option value="bangkok_ind_district_outpatients_diabetes_rate_population">Health center outpatients per 10,000 population: diabetes (2018)</option>
        <option value="bangkok_ind_district_outpatients_diabetes_rate_household">Health center outpatients per 10,000 household: diabetes (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_hypertension">Health center outpatients: hypertension (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_hypertension_rate_area">Health center outpatients per km²: hypertension (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_hypertension_rate_population">Health center outpatients per 10,000 population: hypertension (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_hypertension_rate_household">Health center outpatients per 10,000 household: hypertension (2018)</option>
        <option value="bangkok_ind_district_outpatients_hypertension">Health center outpatients: hypertension (2018)</option>
        <option value="bangkok_ind_district_outpatients_hypertension_rate_area">Health center outpatients per km²: hypertension (2018)</option>
        <option value="bangkok_ind_district_outpatients_hypertension_rate_population">Health center outpatients per 10,000 population: hypertension (2018)</option>
        <option value="bangkok_ind_district_outpatients_hypertension_rate_household">Health center outpatients per 10,000 household: hypertension (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_mental_health">Health center outpatients: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_mental_health_rate_area">Health center outpatients per km²: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_mental_health_rate_population">Health center outpatients per 10,000 population: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_subdistrict_outpatients_mental_health_rate_household">Health center outpatients per 10,000 household: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_district_outpatients_mental_health">Health center outpatients: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_district_outpatients_mental_health_rate_area">Health center outpatients per km²: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_district_outpatients_mental_health_rate_population">Health center outpatients per 10,000 population: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_district_outpatients_mental_health_rate_household">Health center outpatients per 10,000 household: mental and behavioural disorders (2018)</option>
        <option value="bangkok_ind_district_pcd_monitoring_stations">Air quality: PM2.5: monitoring stations</option>
        <option value="bangkok_ind_district_pcd_monitoring_stations_rate_area">Air quality: PM2.5 per km²: monitoring stations</option>
        <option value="bangkok_ind_district_pcd_monitoring_stations_rate_population">Air quality: PM2.5 per 10,000 population: monitoring stations</option>
        <option value="bangkok_ind_district_pcd_monitoring_stations_rate_household">Air quality: PM2.5 per 10,000 household: monitoring stations</option>
        <option value="bangkok_ind_district_pm2p5_days_exceeding_thai_standard">Air quality: PM2.5: days exceeding Thai standard (50 µg/m³; January 2019, PCD)</option>
        <option value="bangkok_ind_district_pm2p5_days_exceeding_who_standard">Air quality: PM2.5: days exceeding WHO standard (25 µg/m³; January 2019, PCD)</option>
        <option value="bangkok_ind_district_restaurants">Number of food entrepreneurs: ร้านอาหาร/Restaurant</option>
        <option value="bangkok_ind_district_restaurants_rate_area">Number of food entrepreneurs per km²: ร้านอาหาร/Restaurant</option>
        <option value="bangkok_ind_district_restaurants_rate_population">Number of food entrepreneurs per 10,000 population: ร้านอาหาร/Restaurant</option>
        <option value="bangkok_ind_district_restaurants_rate_household">Number of food entrepreneurs per 10,000 household: ร้านอาหาร/Restaurant</option>
        <option value="bangkok_ind_district_stalls">Number of food entrepreneurs: แผงลอย/Stall</option>
        <option value="bangkok_ind_district_stalls_rate_area">Number of food entrepreneurs per km²: แผงลอย/Stall</option>
        <option value="bangkok_ind_district_stalls_rate_population">Number of food entrepreneurs per 10,000 population: แผงลอย/Stall</option>
        <option value="bangkok_ind_district_stalls_rate_household">Number of food entrepreneurs per 10,000 household: แผงลอย/Stall</option>
        <option value="bangkok_ind_district_supermarkets">Number of food entrepreneurs: ซูเปอร์มาร์เกต/Supermarket</option>
        <option value="bangkok_ind_district_supermarkets_rate_area">Number of food entrepreneurs per km²: ซูเปอร์มาร์เกต/Supermarket</option>
        <option value="bangkok_ind_district_supermarkets_rate_population">Number of food entrepreneurs per 10,000 population: ซูเปอร์มาร์เกต/Supermarket</option>
        <option value="bangkok_ind_district_supermarkets_rate_household">Number of food entrepreneurs per 10,000 household: ซูเปอร์มาร์เกต/Supermarket</option>
        <option value="bangkok_ind_subdistrict_vegetation_pct_mean">Green space: mean vegetation cover percent  (Copernicus, December 2018)</option>
        <option value="bangkok_ind_district_vegetation_pct_mean">Green space: mean vegetation cover percent  (Copernicus, December 2018)</option>
        <option value="bangkok_ind_subdistrict_vegetation_pct_sd">Green space: standard deviation vegetation cover percent  (Copernicus, December 2018)</option>
        <option value="bangkok_ind_district_vegetation_pct_sd">Green space: standard deviation vegetation cover percent  (Copernicus, December 2018)</option>
        <option value="bangkok_ind_subdistrict_vulnerable_flood_areas">56 vulnerable flood areas in Bangkok year 2018: flood risk locations</option>
        <option value="bangkok_ind_subdistrict_vulnerable_flood_areas_rate_area">56 vulnerable flood areas in Bangkok year 2018 per km²: flood risk locations</option>
        <option value="bangkok_ind_subdistrict_vulnerable_flood_areas_rate_population">56 vulnerable flood areas in Bangkok year 2018 per 10,000 population: flood risk locations</option>
        <option value="bangkok_ind_subdistrict_vulnerable_flood_areas_rate_household">56 vulnerable flood areas in Bangkok year 2018 per 10,000 household: flood risk locations</option>
        <option value="bangkok_ind_district_vulnerable_flood_areas">56 vulnerable flood areas in Bangkok year 2018: flood risk locations</option>
        <option value="bangkok_ind_district_vulnerable_flood_areas_rate_area">56 vulnerable flood areas in Bangkok year 2018 per km²: flood risk locations</option>
        <option value="bangkok_ind_district_vulnerable_flood_areas_rate_population">56 vulnerable flood areas in Bangkok year 2018 per 10,000 population: flood risk locations</option>
        <option value="bangkok_ind_district_vulnerable_flood_areas_rate_household">56 vulnerable flood areas in Bangkok year 2018 per 10,000 household: flood risk locations</option>
        <option value="bangkok_ind_district_water_quality_bod">Water quality in canals with < 2  mg/L dissolved oxygen (DO), 2018: BOD (mg/l)</option>
        <option value="bangkok_ind_district_water_quality_canals_poor">Water quality in canals with < 2  mg/L dissolved oxygen (DO), 2018: canal water storage with < 2 mg/L DO</option>
        <option value="bangkok_ind_district_water_quality_canals_poor_rate_area">Water quality in canals with < 2  mg/L dissolved oxygen (DO), 2018 per km²: canal water storage with < 2 mg/L DO</option>
        <option value="bangkok_ind_district_water_quality_canals_poor_rate_population">Water quality in canals with < 2  mg/L dissolved oxygen (DO), 2018 per 10,000 population: canal water storage with < 2 mg/L DO</option>
        <option value="bangkok_ind_district_water_quality_canals_poor_rate_household">Water quality in canals with < 2  mg/L dissolved oxygen (DO), 2018 per 10,000 household: canal water storage with < 2 mg/L DO</option>
        <option value="bangkok_ind_district_water_quality_do">Water quality in canals with < 2  mg/L dissolved oxygen (DO), 2018: DO (mg/l)</option>
        </SELECT>
        
        <iframe name="iframe" id="maps_interactive" src="./../html/bangkok_02_population_subdistrict_population_per_sqkm.html" height="500px" width="100%"></iframe>
        
.. only:: latex

    Interactive maps for indicators were created and are browsable using the html documentation.
        

