# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 18:10:44 2022

@author: Sushma Thorat
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst =[]
        def solve(idx, nums, ds):
            if idx == len(nums):
                lst.append(list(ds))
                return
            ds.append(nums[idx])
            solve(idx+1, nums, ds)
            ds.pop()
            solve(idx+1, nums, ds)
        solve(0, nums, [])
        return lst
