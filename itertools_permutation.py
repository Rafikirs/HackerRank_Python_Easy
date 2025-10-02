# Exercise: itertools.permutations()
# URL: https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Description: Use itertools.permutations()

from itertools import permutations

s, r = input().split()
r = int(r)

s_permutations = sorted(permutations(s, r))

for permut in s_permutations:
    print("".join(permut))
