# -*- coding: utf-8 -*-
"""task_2_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hK602BbiYzEE5H2sHUSbvh_Bc78ngQID
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output)
print("%.2f" % per)