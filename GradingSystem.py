# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:33:06 2019

@author: woodl
"""

#A program to grade scores that are input from the user

newGrade = 0
sum = 0

for x in range(5):
    newGrade = (input('Enter grade between 0 and 20'))
    newGrade=int(newGrade)
    print('You entered ',newGrade)
    
    sum = sum + newGrade
    
    print('New total = ',sum)
    
if sum >= 85:
    print('A')
elif 75 <= sum < 85:
    print('B')    
elif 65 <= sum < 75:
    print('C')   
elif 50 <= sum < 65:
    print('D')     
else:
    print('F')     
    