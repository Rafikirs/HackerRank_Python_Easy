# Exercise: Map and Lambda Function
# URL: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
# Description: Using map and lambda function along with the Fibonacci sequence

cube = lambda x: x**3

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    elif n > 2:
        base = [0, 1]
        for _ in range(n-2):
            base.append(base[-2] + base[-1])
        return base
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
