# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:53:38 2022

@author: Sushma Thorat
"""
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
