
Select month, account_id, no_of_patients
from (
  Select *,
  rank() over (partition by month order by no_patients desc, account_id) rnk
  from (
      select month, account_id, count(1) as no_of_patients
    from (
        select distinct to_char(date, 'month') as month, account_id, patient_id
        from patient_logs) pl
    group by month, account_id) x
    ) temp
where temp.rnk in (1, 2);
