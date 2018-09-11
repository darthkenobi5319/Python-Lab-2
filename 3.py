# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:38:02 2017

@author: ZHENGHAN ZHANG
"""

#prompt
x=input('Please enter a list of words separated by commas: ').split(',')
x.sort()
print(x)
#extend
y=input('Please enter another list of words separated by commas: ').split(',')
x.extend(y)
x.sort()
print(x)
#index
z=x.index(input('Enter a word: '))
print(z)
#pop
x.pop(z)
print(x)