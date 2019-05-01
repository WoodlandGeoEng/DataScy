# -*- coding: utf-8 -*-
"""
Created on Wed May  1 15:12:36 2019

@author: woodl
"""

#count: count the number of elements in the list
#sum: calculate the sum of all elements in the list
#average: calculate the average of the list elements
#max: find and return the value and index of the maximum element of the list as a tuple
#min: find and return the value and index of the minimum element of the list as a tuple

#creating a program file that can call count, sum, average, max and min


def count(providedList):
    return (len(providedList))

def sumcalc(providedList):
    return sum(providedList)

def average(providedList):
    average = sum(providedList)/len(providedList) 
    return average

def maxcalc(providedList):
    maxValue = (max(providedList),providedList.index(max(providedList))) 
    return maxValue

def mincalc(providedList):
    minValue = (min(providedList),providedList.index(min(providedList)))       
    return minValue    
    
