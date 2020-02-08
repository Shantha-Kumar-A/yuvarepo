import datetime
import pytz

# d = datetime.date(2020, 1, 17)

# print(d)

# t = datetime.time(13,59,00,100000)

# print(t)

# dt = datetime.datetime(2020,1,17,14,6,15,tzinfo=pytz.UTC)

# print(dt)

dt_today = datetime.datetime.today()
dt_now  = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)