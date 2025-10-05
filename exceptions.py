# Exercise: Exceptions
# URL: https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Description: Use try and except with ZeroDivisionError and ValueError

N = int(input())

for _ in range(N):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error code:", e)
    except ValueError as e:
        print("Error code:", e)
