# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 18:08:08 2022

@author: Sushma Thorat
"""

import math
from math import sqrt

sq = int(input())
mean = int(input())
std = int(input())
itl = float(input())
z = float(input())
print(round(mean - (std / sqrt(sq)) * z, 2))
print(round(mean + (std / sqrt(sq)) * z, 2))