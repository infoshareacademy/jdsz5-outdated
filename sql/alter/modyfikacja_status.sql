select to_timestamp("time", 'YYYY/MM/DD HH24:MI:SS'), time
from status

update status
set "time" = to_timestamp("time", 'YYYY/MM/DD HH24:MI:SS')


