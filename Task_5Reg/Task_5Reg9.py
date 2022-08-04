# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:44:00 2022

@author: Sushma Thorat
"""

import re
import email.utils
n = int(input())
for _ in range(n):
    a, b = input().split(' ')
    m = re.match(r'<[a-zA-Z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', b)
    if m:
        print(a,b)