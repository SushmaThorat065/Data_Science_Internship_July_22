# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:22:53 2022

@author: sushma thorat
"""

import numpy
n, m = map(int,input().split(' '))
numpy.set_printoptions(sign=' ')
print(numpy.eye(n, m))
