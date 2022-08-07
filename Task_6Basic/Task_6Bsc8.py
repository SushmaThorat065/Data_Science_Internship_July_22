# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:48:39 2022

@author: Sushma THorat
"""

import numpy

numpy.set_printoptions(sign=' ')

n = numpy.array(input().split(),float)

print(numpy.floor(n))
print(numpy.ceil(n))
print(numpy.rint(n))