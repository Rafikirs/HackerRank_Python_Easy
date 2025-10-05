# Exercise: Set .add()
# URL: https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# Description: Using sets

N = int(input())
countries = []

for _ in range(N):
    country = input()
    countries.append(country)

print(len(set(countries)))
