# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:47:10 2022

@author: sushma thorat
"""

import numpy

a = int(input())

n = numpy.array([list(map(int,input().split())) for _ in range(a)])

m = numpy.array([list(map(int,input().split())) for _ in range(a)])

print(numpy.dot(n, m))