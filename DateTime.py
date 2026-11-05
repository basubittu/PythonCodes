import datetime as dt
today=dt.date.today()
print(today)
timing= dt.datetime.now()
print(timing)
print(timing.hour)
print(timing.minute)
print(timing.second)
print(today.strftime("%d/%m/%Y"))
