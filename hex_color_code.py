# Exercise: Hex Color Code
# URL: https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
# Description: Find Hex color codes within CSS code without using regex


N = int(input())

def is_valid_hex(word):
    return (
        word.startswith("#")
        and len(word) in [4, 7]
        and all(char.isdigit() or char.lower() in "abcdef" for char in word[1:])
    )

for _ in range(N):
    line = input()
    line = line.replace(";", " ").replace(",", " ").replace(":", " ").replace(")", " ")
    words = line.split()

    for word in words[1:]:
        if is_valid_hex(word) and len(words) > 1:
            print(word)
