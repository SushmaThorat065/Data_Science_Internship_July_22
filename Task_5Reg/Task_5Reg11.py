# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 22:43:23 2022

@author: Sushma Thorat
"""

import re
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
MyParser = MyHTMLParser()
for _ in range(int(input())):
    MyParser.feed(''.join([input().strip()]))