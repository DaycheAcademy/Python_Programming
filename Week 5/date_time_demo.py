# time, datetime, calendar

# time aware, time naive
import datetime
import pytz

print(datetime.date.today())
print(type(datetime.date.today()))

today = datetime.date.today()
three_weeks_from_now = datetime.timedelta(weeks=3)

print(today + three_weeks_from_now )

print(datetime.datetime.now())

print('=' * 40)

# print(type(pytz.all_timezones))
# for tz in pytz.all_timezones:
#     print(tz)

print(pytz.country_names)
print(pytz.country_timezones)

# for tz in pytz.country_names:
#     print(tz, pytz.country_names[tz], pytz.country_timezones.get(tz, '[NO TIME ZONE]'))


# for tz in pytz.country_timezones:
#     print(tz, pytz.country_timezones[tz])

utc_time = datetime.datetime.utcnow()
print(pytz.utc.localize(utc_time).astimezone())









