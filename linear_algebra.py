# Exercise: Linear Algebra
# URL: https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
# Description: Using np.linalg.det to retrieve the determinant of a square matrix

import numpy as np 

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(float, input().split())))
arr = np.array(arr)

print(round(np.linalg.det(arr), 2))
