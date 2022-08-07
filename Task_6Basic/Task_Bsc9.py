# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:51:28 2022

@author: sushma thorat
"""

import numpy
n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)],int)
print(numpy.prod(numpy.sum(arr, axis=0), axis=0))