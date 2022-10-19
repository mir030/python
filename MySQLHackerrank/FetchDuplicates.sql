
Select user_id, user_name, email
from(
  Select *,
  row_number() over (partition by user_name order by user_id) as rn
  from users
  order by user_id) x
where x.rn > 1 ;
