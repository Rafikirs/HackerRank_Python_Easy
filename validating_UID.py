# Exercise: Validating UID
# URL: https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true
# Description: Checking whether a word is a valid UID

N = int(input())

for _ in range(N):
    word = input()
    if (
        sum(char.isupper() for char in word) >= 2
        and sum(char.isdigit() for char in word) >= 3
        and all(char.isalnum() for char in word)
        and len(word) == len(set(word))
        and len(word) == 10
        ):
        print("Valid")
    else:
        print("Invalid")
