from datetime import date
from datetime import timedelta



dt = input().split()
d = date(int(dt[0]), int(dt[1]), int(dt[2]))

t = timedelta(int(input()))

new_d = d + t

print(str(new_d.year) + " " + str(new_d.month) + " " + str(new_d.day))