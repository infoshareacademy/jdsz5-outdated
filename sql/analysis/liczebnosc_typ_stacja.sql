--rozkład liczebności per stacja per typ użytkownika
with krok1 as
(
select
s."name",
count (case when subscription_type ilike 'subscriber' then 1 end) subskrybenci,
count (case when subscription_type not ilike 'subscriber' then 1 end) klienci
from trip t
join station s on t.start_station_id = s.id 
group by s."name"),

krok2 as
(
select 
*,
subskrybenci/sum(subskrybenci) over()::numeric dsubs,
klienci/sum(klienci) over()::numeric dcusts
from krok1)

select * from krok2