from datetime import date, datetime, timedelta

# d = date(2022, 8, 1)
# dt = datetime(2022, 8, 1,16,50,00,28055)

d = date.today()
dt = datetime.today()

delta = timedelta(days=5)
date_final = d - delta

date_str = d.strftime("%d %b %Y")
date_str_bis = d.strftime("%A %d %B %Y %Z")

date_stylish = d. strftime("%d %B %y")

print(date_stylish)
# print(d)
# print(dt)
# print(delta)
# print(date_final)