# -*- coding: utf-8 -*-
"""task_2_adv1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mu2jEGTg8XSmfxoBhOEjqVpsQk84ZMkp
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
