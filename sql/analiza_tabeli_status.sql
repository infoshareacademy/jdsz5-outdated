-- Sprawdzanie dostepnosci rowerow w dni powszednie oraz weekendy

with base as (
select
station_id,
to_char(date_hour, 'day') as day,
date_part('hour', date_hour) as hour,
bikes_available,
docks_available
from bikes_median ),
week_days as (
select
station_id,
hour,
mode() within group(order by bikes_available) as bikes_available,
mode() within group(order by docks_available) as docks_available
from base 
where day in ('monday', 'tuesday', 'wednesday', 'friday', 'thursday')
group by 1, 2 ),
weekend as (
select
station_id,
hour,
mode() within group(order by bikes_available) as bikes_available,
mode() within group(order by docks_available) as docks_available
from base 
where day not in ('monday', 'tuesday', 'wednesday', 'friday', 'thursday')
group by 1, 2
)
select station_id, s.name from weekend w
left join station s on s.id = w.station_id
where bikes_available < 4
group by station_id, name

--select * from week_days
--where bikes_available < 4
--order by station_id asc, hour asc
