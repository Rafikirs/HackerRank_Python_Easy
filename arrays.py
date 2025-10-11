# Exercise: Arrays
# URL: https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
# Description: Manipulating a numpy array

import numpy

def arrays(arr):
    return numpy.array([float(char) for char in reversed(arr)], dtype=float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
