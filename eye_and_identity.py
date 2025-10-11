# Exercise: Eye and Identity
# URL: https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
# Description: Using np.eye 

import numpy as np 

n, m = map(int, input().split())
print(np.eye(n, m))
