# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:00:36 2022

@author: Sushma Thorat
"""

import re
v = "aeiouAEIOU"
c = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))