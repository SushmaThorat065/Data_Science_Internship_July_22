# -*- coding: utf-8 -*-
"""Task_3Adv2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17hpdUIozBzURjlU7yTGt1PXMXokjZJF7
"""

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp = [[0, 0] for i in range(n)]
        res = 0
        for k in range(1, n):
            for j in range(0, k):
                if rating[j]<rating[k]:
                    res += dp[j][0]
                    dp[k][0] += 1
                if rating[j]>rating[k]:
                    res += dp[j][1]
                    dp[k][1] += 1
        return res