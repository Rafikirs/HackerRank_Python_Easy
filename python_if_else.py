# Exercise: Python If-Else
# URL: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# Description: Simple use of if/else statements

if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:  # n > 20
        print("Not Weird")
