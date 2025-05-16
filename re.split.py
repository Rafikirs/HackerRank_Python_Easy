# Exercise: Re.split()
# URL: https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true
# Description: Use regex to split a string based on the commas and dots

regex_pattern = r"(?<=\d)[,.](?=\d)"

import re
print("\n".join(re.split(regex_pattern, input())))
