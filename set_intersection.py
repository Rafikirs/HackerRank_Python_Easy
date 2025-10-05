# Exercise: Set .intersection()
# URL: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
# Description: Using intersection on sets

n = int(input())
set_1 = set(map(int, input().split()))
m = int(input())
set_2 = set(map(int, input().split()))

print(len(set_1.intersection(set_2)))
