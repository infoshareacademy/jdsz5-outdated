
--- Stworzenie dodatkowej tabeli do analizy ilosci rowerow na stacjach godzinami

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
select 
station_id,
bikes_available,
docks_available
from week_days
where hour = 5

