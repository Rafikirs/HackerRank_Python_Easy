# Exercise: ginortS
# URL: https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
# Description: Rearrange a string by sorting its characters depending on their nature

s = input() 
lower = []
upper = []
odd = []
even = []

for char in s:
    if char.isalpha():
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
    elif char.isnumeric():
        if int(char)%2 == 0:
            even.append(char)
        else:
            odd.append(char)

print("".join(sorted(lower)) + "".join(sorted(upper)) + "".join(sorted(odd)) + "".join(sorted(even)))
