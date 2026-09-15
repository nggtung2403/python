
from datetime import datetime
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(day,month,year,hour,minute,second)

new_year = datetime(2026,9,9,4,5,6)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day,month,year,hour,minute,second)
print(f"{day}/{month}/{year} {hour}:{minute}")

now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time: ",t)

time_one = now.strftime("%m/%d/%Y,%H:%M:%S")
print("time one:",time_one)

time_two = now.strftime("%d/%m/%Y,%I:%M:%S")
print("time two: ",time_two)

date_string = "5 ,Dec, 2019"
print("date_string=",date_string)
date_object = datetime.strptime(date_string,"%d ,%b, %Y")
print(date_object)

from datetime import date
a = date.today()
print(a)
d = date(2026,8,9)
print(d)
print("current date",d.today())

today = date.today()
print("Current year:",today.year)
print("Current month:",today.month)
print("Current day:",today.day)

from datetime import time
a = time()
print(a)
b = time(10,2,26)
print(b)
c = time(hour=23,minute=59,second=59)
print(c)
d = time(10,30,50,200545)
print(d)

from datetime import timedelta
t1 = timedelta(weeks=12,days=10,hours=4,seconds=20)
t2 = timedelta(days=7,hours=5,minutes=3,seconds=30)
t3 = t1 - t2
print(t3)