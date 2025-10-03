# Exercise: Using a dictionnary to find positions of words in a set
# URL: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Description: DefaultDict

n, m = map(int, input().split())
pos_dict = {}
A = []
B = []

for i in range(n):
    A.append(input())
for j in range(m):
    B.append(input())

for i, word in enumerate(A):
    if word not in pos_dict:
        pos_dict[word] = []
    pos_dict[word].append(i+1)
    
for word in B:
    if word in pos_dict:
        print(*pos_dict[word])
    else:
        print(-1)
