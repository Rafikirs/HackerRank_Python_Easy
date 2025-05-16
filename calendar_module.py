# Exercise: Calendar Module
# URL: https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
# Description: Find the day of a certain date

import calendar

def find_day(month, day, year):
    day_name = calendar.day_name[calendar.weekday(year, month, day)]
    print(day_name.upper())
