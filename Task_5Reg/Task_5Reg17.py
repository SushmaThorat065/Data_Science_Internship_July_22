# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 23:34:41 2022

@author: Ganesh kadam
"""

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
stra = "".join([matrix[j][i] for i in range(m) for j in range(n)])
print(re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])',' ',stra))
