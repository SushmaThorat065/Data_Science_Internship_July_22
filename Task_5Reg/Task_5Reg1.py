# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:24:39 2022

@author: Sushma Thorat
"""

import re
for _ in range(int(input())):
    print(bool(re.search(r'^[-+]?[0-9]*\.[0-9]+$', input())))
    True