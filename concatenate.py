# Exercise: Concatenate
# URL: https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
# Description: Concatenate arrays

import numpy as np 

n, m, p = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(m):
    B.append(list(map(int, input().split())))
    
print(np.concatenate((np.array(A), np.array(B)), axis=0))
