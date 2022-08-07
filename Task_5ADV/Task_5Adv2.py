# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 17:57:43 2022

@author: Sushma Thorat
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x==y:
            return 0
        
        _x = bin(x).replace('0b','')
        _y = bin(y).replace('0b','')
        
        x1 = len(_x)
        y1 = len(_y)
        
        if x1 > y1:
            rem_len = x1-y1
            _y = _y.rjust(x1, '0')
            y1 = len(_y)
        else:
            rem_len = y1-x1
            _x = _x.rjust(y1, '0')
            x1 = len(_x)
            
        i = 0
        j = 0
        diff = 0
        
        while i < x1 and j < y1:
            if _x[i] != _y[j]:
                diff+=1
            i+=1
            j+=1
        return diff