# Exercise: Check Strict Superset
# URL: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Description: Check whether a set is a strict superset of another set 

A = set(input().split())
n = int(input())
result = all(A > set(input().split()) for _ in range(n))
print(result)
