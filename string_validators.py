# Exercise: String Validators
# URL: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
# Description: Find whether a string has any alphabetical characters, alphanumeric characters, digits, lower and upper characters

if __name__ == '__main__':
    s = input()

    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
