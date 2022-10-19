
"""lead(user_name) is used to compare the user_name with the next user_name"""
select distinct user_name
from(
  select *,
  case when user_name = lead(user_name) over(order by login_id)
          and user_name = lead(user_name, 2) over (order by login_id)
          then user_name
        else null
  end as repeated_user
  from login_details) x
where x.repeated_user is not null;