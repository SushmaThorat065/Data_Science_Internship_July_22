# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:49:59 2022

@author: sushma thorat
"""

import numpy

n = list(map(float,input().split()))
m = input()
print(numpy.polyval(n,int(m)))