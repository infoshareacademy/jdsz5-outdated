  
  
select *from trip



    -- id INTEGER PRIMARY KEY,
    -- duration INTEGER,
    -- start_date varchar,
    -- start_station_name varchar,
    -- start_station_id INTEGER,
    -- end_date varchar,
    -- end_station_name varchar,
    -- end_station_id INTEGER,
    -- bike_id INTEGER,
    -- zip_code INTEGER);
    
-- zmienić typ i format dat: start_date, end_date (m)m/(d)d/rrrr hh:mm => dd/mm/rrrr hh:mm
   
select start_date, to_timestamp(start_date, 'MM/DD/YYYY HH24:MI:SS')
from trip


update trip 
set start_date = to_timestamp(start_date, 'MM/DD/YYYY HH24:MI:SS')



-- czy zmieniać zapis zip_code 00,000 => 00-000

select zip_code, replace(zip_code, "," , "-")
from trip
 
set zip_code = replace (zip_code , "," , "-")

