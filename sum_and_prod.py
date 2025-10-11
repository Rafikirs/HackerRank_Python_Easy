# Exercise: Find a string
# URL: https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
# Description: Using np.sum and np.prod

import numpy as np

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = np.array(arr)
sum_arr = np.sum(arr, axis=0)

print(np.prod(sum_arr))
