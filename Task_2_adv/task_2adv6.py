# -*- coding: utf-8 -*-
"""task_2adv6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13-avWD3hcHjpzQg7ys8i4dRuP4_F2P9j
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        answer = 0
        for i in range(start,start+(n*2),2):
            answer ^= i
        return answer