# Exercise: Validating Roman Numerals
# URL: https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true
# Description: Check whether the expression is a valid Roman numeral or not

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"  

import re
print(str(bool(re.match(regex_pattern, input()))))
