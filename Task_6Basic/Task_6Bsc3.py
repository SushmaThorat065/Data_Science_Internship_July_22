# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 15:46:57 2022

@author: SuShma Thorat
"""

import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print (array.transpose())
print (array.flatten())