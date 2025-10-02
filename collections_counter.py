# Exercise: collections.Counter
# URL: https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Description: Sell shoes and check if size is available using collections.Counter()

from collections import Counter

X = int(input())
available_sizes = list(map(int, input().split()))
sizes_count = Counter(available_sizes)

N = int(input())
bought_sizes = {}
total_earned = 0

for _ in range(N):
    size, price = map(int, input().split())
    
    if sizes_count[size] > 0:
        total_earned += price
        sizes_count[size] -= 1
        
print(total_earned)
    
