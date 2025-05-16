# Exercise: Set Mutations
# URL: https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
# Description: This program demonstrates how to apply mutating set operations in Python—such as .update(), 
# .intersection_update(), .difference_update(), and .symmetric_difference_update()—on a set A

n = int(input())
A = set(map(int, input().split()))
num_operations = int(input())

for _ in range(num_operations):
    operation, size = input().split()
    size = int(size)
    other_set = set(map(int, input().split()))
    
    if operation == "intersection_update":
        A.intersection_update(other_set)
    elif operation == "update":
        A.update(other_set)
    elif operation == "difference_update":
        A.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

print(sum(A))







