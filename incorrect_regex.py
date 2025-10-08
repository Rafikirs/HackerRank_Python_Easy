# Exercise: Incorrect Regex
# URL: https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
# Description: Print True when the pattern is a correct Regex, False otherwise

import re

for _ in range(int(input())):
    pattern = input()
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)
