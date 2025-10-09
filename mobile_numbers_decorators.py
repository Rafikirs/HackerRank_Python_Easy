# Exercise: Standardize Mobile Numbers Using Decorators
# URL: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true
# Description: Standardizing mobile numbers using decorators

def wrapper(f):
    def fun(l):
        formatted = []
        base_numbers = [number[-10:] for number in l]
        for base_number in base_numbers:
            formatted.append(f"+91 {base_number[:5]} {base_number[5:]}")
        return f(formatted)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
