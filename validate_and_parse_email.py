# Exercise: Validating and Parsing Email Addresses
# URL: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
# Description: Using regex to validate and parsing email addresses

import re
import email.utils

n = int(input())
pattern = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

for _ in range(n):
    s = input()
    name, addr = email.utils.parseaddr(s)
    if pattern.match(addr):
        print(email.utils.formataddr((name, addr)))
