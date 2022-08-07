# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:16:11 2022

@author: Sushma Thorat
"""
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = b = 0
        for n in nums:
            a = ~b & (a ^ n)
            b = ~a & (b ^ n)
        return a