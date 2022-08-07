# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:52:01 2022

@author: sushma thorat
"""

import numpy
N, M = map(int, input().strip().split())
my_array = numpy.array([ input().strip().split() for _ in range(N) ], int)

print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array, axis = None),11))