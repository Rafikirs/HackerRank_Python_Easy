# Exercise: Any or All
# URL: https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Description: Use any and all functions on Booleans

N = int(input())
arr = list(map(int, input().split()))

condition_1 = all(n >= 0 for n in arr)
condition_2 = any(int("".join(list(reversed(list(str(n)))))) == n 
for n in arr if n >= 0)

print(condition_1 & condition_2)
