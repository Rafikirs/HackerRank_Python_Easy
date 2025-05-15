# Exercise: Write a function
# URL: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
# Description: Given a year, determine whether it is a leap year

def is_leap(year):
    leap = False

    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            leap = True

    return leap
