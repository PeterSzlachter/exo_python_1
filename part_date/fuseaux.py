#UTC 
#EDT EST
#eastern Standard time zone
#eastern daylight time
# PST PDT -> Pacific Daylight Time, Pacific Standard Time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

now = datetime.now()
montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020,3,7,13,0,0,tzinfo=montreal_tz)
march_7_utc = march_7.astimezone(ZoneInfo("UTC"))
march_8 = datetime(2020,3,8,13,0,0,tzinfo=montreal_tz)
march_10 = datetime(2020,3,10,13,0,0, tzinfo=montreal_tz)
march_10_utc = march_10.astimezone(ZoneInfo("UTC"))
print(march_7)
print(march_8)

march_8bis = march_7 + timedelta(days=1)
print(march_8bis)
march_8bis = march_7_utc + timedelta(days=1)
march_8bis = march_8bis.astimezone(montreal_tz)
print(march_8bis) #non prise en compte du changement d'heure

print(march_7.tzname())
print(march_8.tzname())

print(march_10 - march_7)
print(march_10_utc - march_7_utc) #changement d'heure

now_in_15_days_minus_5_hours = now + timedelta(days=15,hours=-5)
print(now_in_15_days_minus_5_hours)