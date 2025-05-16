# Exercise: Check Subset
# URL: https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Description: Checks whether all elements of a set are in another set

t = int(input())
for _ in range(t):
    int(input())
    a = set(input().split())
    int(input())
    b = set(input().split())
    print(a.issubset(b))
