# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:21:53 2022

@author: Sushma Thorat
"""

import re
Test = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    if Test.search(input()):
        print('Valid')
    else:
        print('Invalid')
    