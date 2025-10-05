# Exercise: itertools.combinations_with_replacement()
# URL: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
# Description: Using combinationns_with_replacements function from itertools

from itertools import combinations_with_replacement

S, N = input().split()
S = sorted(S)
N = int(N)

combis = combinations_with_replacement(S, N)

for combi in combis:
    print("".join(combi))
