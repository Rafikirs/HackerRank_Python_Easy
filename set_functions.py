# Exercise: Set .discard(), .remove() & .pop()
# URL: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
# Description: Using discard, remove and pop functions on sets

n = int(input())
ar = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == "pop":
        if ar: 
            ar.pop()
    elif cmd[0] == "remove":
        ar.discard(int(cmd[1]))  
    elif cmd[0] == "discard":
        ar.discard(int(cmd[1]))

print(sum(ar))
