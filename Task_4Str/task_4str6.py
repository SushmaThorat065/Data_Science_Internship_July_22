# -*- coding: utf-8 -*-
"""Task_4Str6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hiQdYVY2kBYZ4Qj-szIHQDCOWZleg1aZ
"""

def merge_the_tools(string, k):
    split_string=(string[i:i+k] for i in range(0,len(string),k))
    for i in split_string:
        u=[]
        u.append(i[0])
        for j in range(1,len(i)):
            if i[j] in u:
                continue
            else:
                u.append(i[j])

        print(''.join(str(e) for e in u))
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)