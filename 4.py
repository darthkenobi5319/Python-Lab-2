# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:11:08 2017

@author: ZHENGHAN ZHANG
"""

#ask the user for a number
userNumber=int(input('Enter a number from 1 to 6: '))

#roll the dice
import random
randomNumber=random.randint(1, 6)

#print out the number of the die
list1=['one','two','three','four','five','six']
listNumber=randomNumber-1
print(list1[listNumber])

#congratulate the user
list2=['Better luck next time!','Congratulations! You are right!']
print(list2[int(userNumber==randomNumber)])