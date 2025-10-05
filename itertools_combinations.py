# Exercise: itertools.comnbinations() 
# URL: https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
# Description: Using itertools combinations

from itertools import combinations

S, n = input().split()
n = int(n)
S = sorted(S)

for i in range(1, n+1):
    combis = sorted(["".join(combi) for combi in list(combinations(S, i))])
    for combi in combis:
        print(combi)
    
