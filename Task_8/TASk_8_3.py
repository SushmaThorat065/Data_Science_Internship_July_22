# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 17:35:14 2022

@author: Sushma Thorat
"""

import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

print('{:.3f}'.format(cdf(19.5)))


print('{:.3f}'.format(cdf(22) - cdf(20)))