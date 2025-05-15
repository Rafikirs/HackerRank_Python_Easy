# Exercise: Print function
# URL: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# Description: Print the list of integers from 1 to n as a string, without spaces and without using strings

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')
