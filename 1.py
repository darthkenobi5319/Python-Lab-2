# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:08:46 2017

@author: ZHENGHAN ZHANG
"""
#define x
x = 'pony stash token'
#Print the first letter
print(x[0])
#Print the last letter
print(x[-1])
#Print all letters except the first and the last
print(x[1:-1])
#Print every other character
print(x[::2])
#Produce the string python
print(x[::3])
#Print the last word in reverse
print(x[:-6:-1])
#replace
x=x[:5]+'tony'+x[-6:]
print(x)