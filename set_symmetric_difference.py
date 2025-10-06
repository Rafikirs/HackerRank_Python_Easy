# Exercise: Set .symmetric_difference()
# URL: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Description: Using symmetric_dfference function on sets

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))

print(len(A.symmetric_difference(B)))
