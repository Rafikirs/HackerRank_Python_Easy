# Exercise: Transpose and Flatten
# URL: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
# Description: Turn a list of lists into an numpy array, transpose and flatten it


import numpy as np 

n, m = map(int, input().split())
full_arr = []

for _ in range(n):
    arr = list(map(int, input().split()))
    full_arr.append(arr)

full_arr = np.array(full_arr)

print(np.transpose(full_arr))
print(full_arr.flatten())
