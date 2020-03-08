--zestawienie stacji pod kątem popularności (starty i oddania)

with starty as (    

select count(start_station_id ) lpoczatek , start_station_id
from trip
group by start_station_id
order by count(start_station_id ) desc),
zakonczenia as ( 
select count(end_station_id ) lkoniec, end_station_id 
from trip t 
group by end_station_id
order by count(start_station_id ) desc )

select * from starty
join zakonczenia on zakonczenia.end_station_id = starty.start_station_id