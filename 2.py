# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:26:34 2017

@author: ZHENGHAN ZHANG
"""

#get the name of the user
name=input('Please enter your full name: ')
#generate a computer name
computerName=name.lower()[0]+name.lower().split()[-1][4::-1]
print(computerName)