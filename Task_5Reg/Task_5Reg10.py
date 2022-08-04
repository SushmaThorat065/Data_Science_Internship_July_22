# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:35:21 2022

@author: Sushma Thorat
"""

import re
pattern = r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for x in re.findall(pattern,input()):
        print(x)