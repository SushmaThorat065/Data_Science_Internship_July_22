# -*- coding: utf-8 -*-
"""Task_4Adv1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Q3Q3PddGqaogyLEVx24BX74YQX7hZR4
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]