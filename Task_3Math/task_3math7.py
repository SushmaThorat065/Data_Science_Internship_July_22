# -*- coding: utf-8 -*-
"""task_3Math7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzVXaP_0pDuiHMm09awJGXiJHUZ_83kB
"""

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*sum(map(lambda x:10**x, range(i))))