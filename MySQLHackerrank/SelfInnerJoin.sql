
"""Compare one row with all the other rows in the same table"""

Select d1.*
from doctors d1
join doctors d2 on d1.id <> d2.id and d1.hospital = d2.hospital
and d1.specialty <> d2.specialty;
