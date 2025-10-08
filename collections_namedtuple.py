# Exercise: Using Collections.namedtuple()
# URL: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Description: Using collections.namedtuple()

from collections import namedtuple
n, cols = int(input()), input().split()
Student = namedtuple('Student', cols)
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")
