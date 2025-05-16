# Exercise: Inner and Outer 
# URL: https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
# Description: Print the inner and outer products of two arrays

import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

print(np.inner(A, B))
print(np.outer(A, B))






