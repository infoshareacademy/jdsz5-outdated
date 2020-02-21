select * 
from weather w2 
limit 50


-- konwersja kolumn na formaty europejskie:

select 
(max_temperature_f - 32) * 5/9 as max_temperature_c,
(mean_temperature_f - 32) * 5/9 as mean_temperature_c,
(min_temperature_f - 32) * 5/9 as min_temperature_c,
(max_dew_point_f - 32) * 5/9 as max_dew_point_c,
(mean_dew_point_f -32) * 5/9 as mean_dew_point_c,
(min_dew_point_f  -32) *5/9 as min_dew_point_c,
max_sea_level_pressure_inches *2.54 as max_sea_level_pressure_cm,
mean_sea_level_pressure_inches *2.54 as mean_sea_level_pressure_cm,
min_sea_level_pressure_inches *2.54 as min_sea_level_pressure_cm,
max_visibility_miles * 1.609 as max_visibility_km,
mean_visibility_miles *1.609 as mean_visibility_km,
min_visibility_miles  *1.609 as min_visibility_km,
max_wind_speed_mph  * 1.609 as max_wind_speed_km,
mean_wind_speed_mph *1.609 as mean_wind_speed_km,
max_gust_speed_mph *1.609 as max_gust_speed_km,
precipitation_inches *2.54 as precipitation_cm
from weather w 
