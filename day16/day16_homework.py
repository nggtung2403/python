from datetime import datetime
now = datetime.now()
print(now)
time = now.strftime("%m/%d/%Y,%H:%M:%S")
print(time)
today = datetime(2019,12,5)
print(today)

from datetime import timedelta
now = datetime.now()
next_year = now.year + 1
new_year_day = datetime(next_year,1,1)
time_left = new_year_day - now
t2 = next_year - now.year
print(time_left)
print(t2)

t = datetime(1970,1,1)
t3 = now - t
print(t3)