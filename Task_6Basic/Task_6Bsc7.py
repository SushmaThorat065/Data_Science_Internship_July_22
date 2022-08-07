# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:44:08 2022

@author: Sushma Thorat
"""
import numpy
n, m = map(int, input().split())
a, b = (numpy.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')