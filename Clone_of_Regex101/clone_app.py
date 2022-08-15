# -*- coding: utf-8 -*-
"""
@author: Sushma Thorat
"""

from flask import Flask, render_template, request
import re
clone_app = Flask(__name__)

@clone_app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        regex = request.form['rexp']
        test_str = request.form['tstring']
        matches = re.finditer(regex, test_str, re.MULTILINE) 
        for matchNum, match in enumerate(matches, start=1):
            print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
        
            print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

    return render_template("regix_clone.html")

    
@clone_app.route('/about_us')
def about_us():
    return 'This is About us page'






if __name__ =='__main__':
    clone_app.run()
    