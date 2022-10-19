
Select *
from(
  select *,
  case when temperature < 0
        and lead(temperature) over (order by id) < 0
        and lead(temperature, 2) over (order by id) < 0
      then 'Yes'

      when temperature < 0
        and lag(temperature) over (order by id) < 0
        and lead(temperature) over (order by id) < 0
      then 'Yes'

      when temperature < 0
        and lag(temperature) over (order by id) < 0
        and lag(temperature, 2) over (order by id) < 0
      then 'Yes'

      else null
  end as flag
  from weather) x
where x.flag = yes;