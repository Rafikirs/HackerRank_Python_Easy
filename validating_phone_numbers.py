# Exercise: Validating Phone Numbers
# URL: https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# Description: Checking whether a phone number is valid or not

import re

n = int(input())
for _ in range(n):
    s = input()
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")


