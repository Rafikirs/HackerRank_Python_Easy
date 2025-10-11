# Exercise: Array Mathematics
# URL: https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
# Description: Print different types calculations made on elements of two arrays


import numpy as np 

n, m = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(n):
    B.append(list(map(int, input().split())))

A = np.array(A)
B = np.array(B)

print(A+B)
print(A-B)   
print(A*B)  
print(np.array(np.floor(A/B), dtype=int))  
print(A % B)
print(A**B)
