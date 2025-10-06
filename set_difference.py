# Exercise: Set .difference()
# URL: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Description: Using the difference function on sets

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))

print(len(A.difference(B)))
