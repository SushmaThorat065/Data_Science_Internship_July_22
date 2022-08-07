# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:47:41 2022

@author: sushma thorat
"""

import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A,B), numpy.outer(A,B), sep='\n')