# Exercise: Polynomials
# URL: https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
# Description: Find the value of a polynomial at a certain point

import numpy as np

coefficients = list(map(float, input().split()))
x = float(input())

print(np.polyval(coefficients, x))






