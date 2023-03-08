from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time

# import datetime

# print(dir(datetime))

simdi = datetime.now()   # == datetime.today()

# print(simdi)
# print(simdi.year)
# print(simdi.day)
# print(simdi.month)
# print(simdi.hour)
# print(simdi.minute)
# print(simdi.second)

# print(datetime.ctime(simdi))

# print(datetime.strftime(simdi,'%Y'))    # year
# print(datetime.strftime(simdi,'%X'))    # time
# print(datetime.strftime(simdi,'%d'))    # day
# print(datetime.strftime(simdi,'%A'))    # day name
# print(datetime.strftime(simdi,'%B'))    # month name
# print(datetime.strftime(simdi,'%Y %B %A'))

# google => datetime python

# t = "29 Temmuz 2020"
# gun,ay,yil = t.split()
# print(gun)
# print(ay)
# print(yil)

t = '29 July 2020 hour 00:34:30'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

print(dt)
print(dt.year)

birthday = datetime(2001,11,16,4,26,58)
print(birthday)

result = datetime.timestamp(birthday) # datetime to second (1970'den o tarihe kadarki süre)
result = datetime.fromtimestamp(result) # second to datetime
result = datetime.fromtimestamp(0)

print(result)

fark = simdi - birthday  # timedelta

print(fark)
print(fark.days)
print(fark.seconds)

timedeltax = simdi + timedelta(15)  # 15 gün ekler
timedeltax = simdi - timedelta(500)

print(timedeltax)

