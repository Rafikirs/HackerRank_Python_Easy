# Exercise: Floor, Ceil and Rint
# URL: https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
# Description: Using floor, ceil and round functions on an array

import numpy as np 

arr = np.array(list(map(float, input().split())))

np.set_printoptions(legacy="1.13")
print(np.floor(arr))
print(np.ceil(arr))
print(np.round(arr))
