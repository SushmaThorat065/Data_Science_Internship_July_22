# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 17:27:07 2022

@author: Sushma Thorat
"""

regex_pattern = r"[,.]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))