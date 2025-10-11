# Exercise: Validating Credit Card Numbers
# URL: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Description: Validating Credit Card Numbers based on certains constraints

def is_valid_card_number(num):
    return (
        num.startswith(("4", "5", "6"))
        and sum(char.isdigit() for char in num) == 16
        and all(char.isdigit() for char in num.replace("-", ""))
        and ("-" not in num or all(len(group) == 4 for group in num.split("-")))
        and " " not in num
        and "_" not in num
        and not any(num.replace("-", "")[i] == num.replace("-", "")[i+1] == num.replace("-", "")[i+2] == num.replace("-", "")[i+3] for i in range(len(num) - 7))
    )
    
N = int(input())
for _ in range(N):
    if is_valid_card_number(input()):
        print("Valid")
    else:
        print("Invalid")
