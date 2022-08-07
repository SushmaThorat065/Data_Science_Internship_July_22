# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:46:08 2022

@author: Sushma Thorat
"""
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return(numpy.array(arr[::-1], float))
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
