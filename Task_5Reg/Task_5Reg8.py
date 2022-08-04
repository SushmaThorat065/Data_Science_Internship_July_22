# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 22:33:01 2022

@author: Sushma Thorat
"""

import re
N = int(input())
for i in range(N):
    if re.match(r'[7-9]\d{9}$',input()):
        print('YES')
    else:
        print('NO')  