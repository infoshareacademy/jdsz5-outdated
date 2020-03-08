--popularnosc tras (ilosciowa)+średni czas trwania
select 
concat (start_station_id,'-', end_station_id) as trasy, 
concat (start_station_name, '-', end_station_name) as nazwy_tras, 
count  (concat (start_station_id,'-', end_station_id)) as ilosc_wypozyczen, 
avg(duration) as sredni_czas_wypozyczenia
from trip
group by 1,2
order by 3 desc


