# Exercise: Symmetric Difference
# URL: https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Description: Using sets and classic functions on sets

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

d1 = a.difference(b)
d2 = b.difference(a)

diffs = sorted(list(d1) + list(d2))

for d in diffs:
    print(d)
