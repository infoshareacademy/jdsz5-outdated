
--- Stworzenie dodatkowej tabeli do analizy ilosci rowerow na stacjach

create table bikes_median as (
with t1 as (
select 
station_id,
bikes_available,
docks_available,
date_trunc('hour', time::timestamp) as date_hour 
from status s )
select
station_id,
date_hour,
percentile_disc(0.5) within group(order by bikes_available) as bikes_available,
percentile_disc(0.5) within group(order by docks_available) as docks_available 
from t1
group by station_id, date_hour )
