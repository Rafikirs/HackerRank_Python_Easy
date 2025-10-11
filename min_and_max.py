# Exercise: Min and Max
# URL: https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Description: Using np.min and np.max

import numpy as np 

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
arr = np.array(arr)

print(np.max(np.min(arr, axis=1)))
