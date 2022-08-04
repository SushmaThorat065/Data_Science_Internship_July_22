# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:28:06 2022

@author: Sushma Thorat
"""

import re
S = input()
k = input()    
matches = list(re.finditer(r'(?={})'.format(k), S))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')