# -*- coding: utf-8 -*-
"""Task_3Adv3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kcf77sd6DRZszh0GjUuxCIcCbYbZ04DG
"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans=0
        m=zip(startTime, endTime)
        for s, e in m:
            if s<=queryTime<=e:
                ans+=1
        return ans