import datetime as dt


print()
x = float(input("kilometers = "))
a = int(input("seconds  = "))
b = int(input("minutes = "))
c = dt.timedelta(minutes=b, seconds=a)
c = c.total_seconds()
hour = c / 3600
miles = x / 1.6
print("average speed in mph = ", miles / hour)


