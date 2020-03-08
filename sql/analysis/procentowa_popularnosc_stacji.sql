--procentowa popularnosc trasy

with krok1 as
(
select 
count(id) liczba,
start_station_name stacja
from trip 
group by start_station_name),
krok2 as
(
select *, liczba/sum(liczba) over()::numeric procent
from krok1)

select* from krok2