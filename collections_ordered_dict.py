# Exercise: collections.OrderedDict
# URL: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Description: Using a dictionnary taking into account the order of appearance of items

N = int(input())

duos = {}

for _ in range(N):
    duo = input().split()
    item = " ".join(duo[:-1])
    price = int(duo[-1])
    
    if item in duos:
        duos[item] += price
    else:
        duos[item] = price
        
for duo in duos.items():
    print(duo[0], duo[1])  
