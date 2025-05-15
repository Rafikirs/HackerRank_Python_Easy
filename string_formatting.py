# Exercise: String Formatting
# URL: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Description: Given an integer n, print the decimal, octal, hexadecimal and binary values for each integer from 1 to n

def print_formatted(number):
    width = len(bin(number)) - 2  

    for i in range(1, number + 1):
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")
