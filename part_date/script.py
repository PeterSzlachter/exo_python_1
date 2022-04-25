#l'epoch UNIX 1er janvier 1970 00:00:00 UTC Coordinated Universal Time
#Norme ISO 8601
# import time
from datetime import date, time, datetime
# from time import strptime 
from zoneinfo import ZoneInfo #depuis 3.9
# from dateutil import parser
# import dateparser #installé avec pip
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

print(date(1995,3,30))
print(date.today())
print(time(22,19,00))
print(datetime(2022,3,30,22,18,00))
print(datetime.now())
print(datetime.utcnow())
print(datetime.now().year)

zone = ZoneInfo("Pacific/Kwajalein")

print(date.fromisoformat("2022-03-31")) 
print(datetime.strptime("31 Mar 2022", "%d %b %Y")) # strftime.org
print(datetime.now().strftime("%d %B %Y"))
print(datetime.now().tzinfo) #date naïve
now_in_vancouver = datetime.now(tz=ZoneInfo("America/Vancouver")) #date aware
now_in_paris = now_in_vancouver.astimezone(ZoneInfo("Europe/Paris"))
print(now_in_vancouver)
print(now_in_paris)
print(datetime.now(tz=ZoneInfo("Europe/London")))
print(now_in_paris.tzname())