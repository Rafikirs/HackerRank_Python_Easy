# Exercise: Shape and reshape
# URL: https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
# Description: Turning a list into a numpy array and reshaping it

import numpy as np

base = np.array(list(int(char) for char in input().split()))

print(np.reshape(base, (3,3)))
