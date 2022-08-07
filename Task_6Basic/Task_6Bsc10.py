# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:51:57 2022

@author: sushma thorat
"""

import numpy

n, m = map(int,input().split())

lst=[list(map(int,input().split())) for i in range(n)]

arr = numpy.array(lst)

print(max(numpy.min(arr,axis=1)))