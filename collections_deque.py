# Exercise: collections.deque()
# URL: https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
# Description: Using collections.deque

from collections import deque

d = deque()
N = int(input())

for _ in range(N):
    op = input().split()
    if op[0] == "append":
        d.append(op[1])
    if op[0] == "pop":
        d.pop()
    if op[0] == "popleft":
        d.popleft()
    if op[0] == "appendleft":
        d.appendleft(op[1])

print(*d)
