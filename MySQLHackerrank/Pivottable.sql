Select min(=Doctor), min(Professor), min(Singer), min(Actor)
from(
Select
row_number() over (partition by occupation order by name) rn,
case when occupation='Doctor' then name else null end as Doctor,
case when occupation='Professor' then name else null end as Professor,
case when occupation='Singer' then name else null end as Singer,
case when occupation='Actor' then name else null end as Actor
from Occupations order by name) x
group by rn
order by rn