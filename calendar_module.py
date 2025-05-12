import calendar

def find_day(month, day, year):
    day_name = calendar.day_name[calendar.weekday(year, month, day)]
    print(day_name.upper())
