# Exercise: Zipped!
# URL: https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
# Description: Using zip on lists

N, X = map(int, input().split())
marks_lines = []
for _ in range(X):
    marks_lines.append(list(map(float, input().split())))
    
all_marks = zip(*marks_lines)
averages = [sum(marks)/len(marks) for marks in all_marks]

for avg in averages:
    print(avg)
