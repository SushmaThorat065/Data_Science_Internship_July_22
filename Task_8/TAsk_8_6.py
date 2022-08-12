# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 18:05:05 2022

@author: Sushma Thorat
"""

import math
from math import erf

max_num = float(input())
n = int(input())
m = float(input())
std = float(input())

mean = n * m
stan = std * (n**0.5)
f = lambda x : 0.5 * (1+erf((x-mean)/(stan*(2**0.5))))
pro = f(max_num)
pro = round(pro, 4)
print(pro)