# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:28:59 2017

@author: ZHENGHAN ZHANG
"""

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

#deal with the alignment
character=len(list1[listNumber])
placeHolder=6-character
placeHolderFront=placeHolder//2
placeHolderHind=placeHolder-placeHolderFront

print('+','-'*6,'+',sep='')
print('|',' '*placeHolderFront,list1[listNumber],' '*placeHolderHind,'|',sep='')
print('+','-'*6,'+',sep='')

#congratulate the user
list2=['Better luck next time!','Congratulations! You are right!']
print(list2[int(userNumber==randomNumber)])
