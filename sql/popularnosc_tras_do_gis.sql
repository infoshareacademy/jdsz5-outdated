

select *from trip


select 
distinct start_station_name,
count(id) over(partition by start_station_name  ) as popularna_trasa_start
from trip t 
order by popularna_trasa_start

select 
distinct end_station_name,
count(id) over(partition by end_station_name) as popularna_trasa_end
from trip t 
order by popularna_trasa_end 