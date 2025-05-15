# Exercise: Mutations
# URL: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
# Description: Change one letter from a string at a given position

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
