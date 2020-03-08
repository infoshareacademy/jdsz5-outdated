select *
from station 

/* 
id INTEGER
"name" VARCHAR
lat NUMERIC
long NUMERIC
dock_count INTEGER
city VARCHAR
installation_date VARCHAR 
*/

--installation_date date format usa to eu
 
update station 
set installation_date = to_date(installation_date, 'MM/DD/YYYY')


--tabela zawiera informacje o stacjach rowerowych wraz z położeniem na mapie i liczbie miejsc na rowery
