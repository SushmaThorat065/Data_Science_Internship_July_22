# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:33:31 2022

@author: Sushma Thorat
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean = 70
std = 10

cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-cdf(80))*100,2))

print(round((1-cdf(60))*100,2))

print(round((cdf(60))*100,2))