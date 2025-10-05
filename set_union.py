# Exercise: Set .union()
# URL: https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true
# Description: Union union function on sets

n = int(input())
set_1 = set(map(int, input().split()))
m = int(input())
set_2 = set(map(int, input().split()))

print(len(set_1.union(set_2)))
