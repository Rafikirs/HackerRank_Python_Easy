# Exercise: Dot and Cross
# URL: https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
# Description: Print the dot product of two arrays

import numpy as np

n = int(input())
A = np.array([list(map(int, input().split())) for _ in range(n)])
B = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.dot(A, B))






