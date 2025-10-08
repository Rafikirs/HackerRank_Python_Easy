# Exercise: Input()
# URL: https://www.hackerrank.com/challenges/input/problem?isFullScreen=true
# Description: Given x, k, and a polynomial, check whether P(x) = k or not

x, k = map(int, input().split())
P = input()

print(eval(P) == k)
