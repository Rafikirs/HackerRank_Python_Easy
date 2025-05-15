# Exercise: Text Wrap
# URL: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Description: Print substrings of a given size from a string 

def wrap(string, max_width):
    wrapped_string = ""
    for i in range(0, len(string), max_width):
        wrapped_string += string[i:i+max_width] + '\n'
    return wrapped_string.strip()  
