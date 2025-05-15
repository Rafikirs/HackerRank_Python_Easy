# Exercise: Finding the percentage
# URL: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Description: This script reads student names with their exam scores, stores them in a dictionary, 
# and calculates the average score for a given student, displaying it with two decimal places

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average:.2f}")
