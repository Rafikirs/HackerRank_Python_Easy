# Exercise: Re.start() & Re.end()
# URL: https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
# Description: Using re.start() and re.end()

import re

S = input().strip()
k = input().strip()

if not k:
    print((-1, -1))
else:
    pattern = re.compile(r'(?=(%s))' % re.escape(k))
    matches = list(pattern.finditer(S))

    if matches:
        for m in matches:
            start = m.start()
            end = start + len(k) - 1
            print((start, end))
    else:
        print((-1, -1))
