# -*- coding: utf-8 -*-
"""task_2_12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YwnO5ZWnMj0JI4DDGzb7XRfVThw-AcXf
"""

def minion_game(string):
    # your code goes here
    scores = {"Kevin": 0, "Stuart": 0}
    for i in range(len(string)):
        if string[i] in "AEIOU":
            scores["Kevin"]+=len(string)-i
        else:
            scores["Stuart"]+=len(string)-i
    if scores["Stuart"] == scores["Kevin"]:
        print("Draw")
    elif scores["Stuart"] > scores["Kevin"]:
        print("%s %s" %("Stuart", scores["Stuart"]))
    else:
        print("%s %s" %("Kevin", scores["Kevin"]))


if __name__ == '__main__':
    s = input()
    minion_game(s)