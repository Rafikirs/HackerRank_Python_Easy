# Exercise: Group(), Groups() & Groupdict()
# URL: https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
# Description: Using functions like .group() to find the first occurrence of an alphanumeric character 
# in a string that has consecutive repetitions.

import re

s = input()

match = re.search(r'([a-zA-Z0-9])\1', s)
print(match.group(1) if match else -1)
