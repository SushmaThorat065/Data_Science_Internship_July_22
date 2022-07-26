# -*- coding: utf-8 -*-
"""Task_4Adv4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ewInuW23ml4DzTgcsrE2EidknSN60Lyg
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
         self.sol = []
         self._subsets(nums,[], 0)
         return self.sol
    def _subsets(self, nums:List[int], current: List[int], index:int):        
        if index>=len(nums):           
            self.sol.append(current)
            return
        
        self._subsets(nums, current+[nums[index]], index+1)
        
        self._subsets(nums, current, index+1)