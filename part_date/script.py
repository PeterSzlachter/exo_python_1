#l'epoch UNIX 1er janvier 1970 00:00:00 UTC Coordinated Universal Time
#Norme ISO 8601
# import time
from datetime import date, time, datetime

print(date(1995,3,30))
print(date.today())
print(time(22,19,00))
print(datetime(2022,3,30,22,18,00))
print(datetime.now())
print(datetime.utcnow())
print(datetime.now().year)