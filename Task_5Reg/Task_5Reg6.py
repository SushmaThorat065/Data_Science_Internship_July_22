# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:36:53 2022

@author: Sushma Thorat
"""

import re
N = int(input())


for i in range(0,N):
   txt = input()
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   txt = re.sub(r"\ \&\&\ "," and ",txt)
   txt = re.sub(r"\ \|\|\ "," or ",txt)
   print(txt)