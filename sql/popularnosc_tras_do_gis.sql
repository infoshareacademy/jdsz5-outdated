

select *from trip
select * from station

select
distinct start_station_name,
s.lat,
s.long,
count(t.id) over(partition by start_station_name) as popularnosc_trasy_start
from trip t 
join station s on s.name= t.start_station_name
order by popularnosc_trasy_start


select 
distinct end_station_name,
s.lat,
s.long,
count(t.id) over(partition by end_station_name) as popularnosc_trasy_end
from trip t 
join station s on s.name= t.end_station_name
order by popularnosc_trasy_end 