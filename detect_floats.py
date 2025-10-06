# Exercise: Detect Floating Point Number
# URL: https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
# Description: Detect floats

T = int(input())
for i in range(T):
    N= input()
    if ('.') in N:
        try:
            N= float(N)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)
