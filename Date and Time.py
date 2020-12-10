import datetime
import pytz
# datetime.datetime(Y, M, D, H, M, S, MS)
# datetime.date(Y, M, D)

# Finding today date
today = datetime.date.today()
print(today)
# Finding days since birth
birthday = datetime.date(2002,11,8)
print(today - birthday)
# Adding 'n' no.of days to current date
time = datetime.timedelta(days=10)
print(today - time)
print (today.month)
print(today.weekday())

# Monday = 0, Tuesday = 1, Wednesday = 2, Thursday = 3, Friday = 4, Saturday = 5, Sunday = 6.

# datetime.datetime(Y, M, D, H, M, S, MS)
# datetime.time(H, M, S, MS)
print(datetime.time(14,30,0,100))
# Adding 'n' no.of hours to current time
hour = datetime.timedelta(hours=24)
print(datetime.datetime.now ())
print(datetime.datetime.now () + hour)
datetime_today = datetime.datetime.now (tz=pytz.UTC)
datetime_India = datetime_today.astimezone(pytz.timezone('Asia/Kolkata'))
print(datetime_India) 
#for all_countries in pytz.all_timezones:
  #print(all_countries)
print(datetime_India.strftime('%B-%d-%Y'))
print(datetime.datetime.strptime('November 8, 2002', '%B %d, %Y'))