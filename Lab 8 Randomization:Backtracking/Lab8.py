#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 21:44:35 2019

@author: SergioGramer
Instructor: Dr. Fuentes
TA: Anindita Nath
Purpose: The purpose of this lab is to use our randomizing skills and create 
         an algorithm that takes the functions provided by Dr. Fuentes and checks
         (randomly) which are equal and which are not.
         Also, we are to take a set of numbers, and use our backtracking knowledgee
         to split the list and see if any combination of numbers in the set; when summed
         is equal.
"""

import random
import numpy as np
from math import *
import math

def randomized_alg(trig_func) : #the method to check if the functions are equal randomly
    total = 0 #will keep track of which functions are equal
    while trig_func != [] : 
        comp1 = trig_func.pop(0) #setting comparator 1 to the first element in trig func (by popping we ensure correct traversal)
        for j in range(len(trig_func)) :
            comp2 = trig_func[j] #comparator 2 will go through the remaining list 
            eq = equal(comp1, comp2) #sends our 2 comparators to our equal function (given by the instructor with minor modifications)
            if eq : #check to see if equal sent back true
                print(comp1, '=', comp2) #if so, print out the 2 comparators used
                total += 1 #increment total
    print('Out of 16 Trigonometric Functions, ', total, ' are equal.')
                

def equal(f1, f2,tries=1000,tolerance=0.0001): #the method we will use to check if the 2 comparators are equal
#    print('This is F1: ', f1)
#    print('This is F2: ', f2)
    for i in range(tries): 
        x = random.uniform(-(math.pi), math.pi)
        if f1 == 'sec(x)' : #sec(x) was not defined so used the trig identity
            f1 = '1/math.cos(x)' #sets f1 to the trig identity of sec
        if f2 == 'sec(x)' : #same for f2 sec
            f2 = '1/math.cos(x)' 
        if f1 == 'sin^2(x)' : #power function not defined so used math.pow
            f1 = 'math.pow(math.sin(x), 2)' 
        if f2 == 'sin^2(x)' :
            f2 = 'math.pow(math.sin(x), 2)'
        y1 = eval(f1) 
        y2 = eval(f2)
        if np.abs(y1-y2)>tolerance:
            return False
    return True


def sets(s1, s2, last) : #this method is our partition method it will take a list split it and return true if it was able to be partitioned
    if last < 0 :#if last is less than 0 jump out no partition was found
        return False, s1, s2, s1+s2
    
    if sum(s1) == sum(s2) : #if the sum of the 2 sets are equal jump out a partition was found
        return True, s1, s2, s1+s2  
    
    if sum(s1) < sum(s2) : #while the sum of all elements in s1 is less than the sum of the elements in s2
        s1.append(s2[-1]) #add item in s2 to s1
        s2.remove(s2[-1]) #remove the item from the other list
        
    if sum(s1) > sum(s2) : #while the sum of elements in s1 is greater than sum of elements in s2
        s2.append(s1[last])  #add item from s1 to s2
        s1.remove(s1[last]) #remove the item from the other list
        
    return sets(s1, s2, last-1)

print('Part 1: Randomized Algorithms')
trig_func = ['sin(x)', 'cos(x)', 'tan(x)', 'sec(x)', '-sin(x)', '-cos(x)', '-tan(x)', 'sin(-x)', 'cos(-x)', 'tan(-x)', 'sin(x)/cos(x)', '2*sin(x/2)*cos(x/2)', 'sin^2(x)', '1-(cos(x)*cos(x))', '(1-cos(2*x))/2', '1/(cos(x))']
randomized_alg(trig_func)

S0 = [2, 4, 5, 9, 12]
S2 = [2, 4, 5, 9, 13]
F2 = [2, 4, 5, 9, 13]
S3 = []
B, s1, s2, S0 = sets(S0, S3, len(S0)-1)
B2, s3, s4, S2 = sets(S2, S3, len(S2)-1)
print()
print('Part 2: Backtracking')
S0.sort()
print('This is s3 ', s3)
print('This is s4 ', s4)
if B :
    print('Set: ', S0, ' has a partition of: ', s1, s2)
if not B :
    print('Set: ', S0, ' has no partition.')
    
if B2 :
    print('Set: ', S2, ' has a partition of: ', s3, s4)
if not B2 :
    print('Set: ', F2, ' has no partition.')