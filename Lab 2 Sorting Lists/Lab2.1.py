#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:24:11 2019

@author: SergioGramer
"""
import copy
import random

def Copy(L):
    ptr = L.head
    L1 = List()
    
    while ptr is not None:
        Append(L1,ptr.item)
        ptr = ptr.next
        
    return L1

def Median(L):
    C = copy.copy(L)
    return ElementAt(C, SizeList(C)//2)

def ElementAt(L, n) :
    ptr = L.head
    count = 1
    
    if IsEmpty(L) :
        return
    
    else :
        
        while count != n :
            ptr = ptr.next
            count += 1
            
        if count == n :
            return ptr.item
        
        else :
            return None
                   
#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print() 

def SizeList(L) :
    counter = 1
    co = L.head
    
    while co.next is not None : 
        counter += 1
        co = co.next
        
    return counter

def BubbleSort(L) :
    global bubblecount
    swap = True #variable to make sure we swap again and check list when at least 1 was swapped
    ptr = L.head 
    
    while swap  == True :
        ptr = L.head
        swap = False
        
        while ptr.next is not None : 
            bubblecount += 1
            
            if ptr.item > ptr.next.item : 
                temp = ptr.next.item #swapping variables from 1 node to another 
                ptr.next.item = ptr.item
                ptr.item = temp
                ptr = ptr.next
                swap = True
                
            else : 
                ptr = ptr.next #will ensure traversal of list in none applies
                
    return L

def MergeSort(L) :
    if IsEmpty(L): #ensures we don't send empty lists recursively
        return L   #need to check these 2 first before assigning ptr to L.head
    
    if SizeList(L) == 1 : #we don't have anything to split if list is of size 1
        return L
    
    ptr = L.head
    L1 = List() #Will be the 2 lists we use to split the original list into smaller 
    L2 = List() #problems for recursion
    mid = SizeList(L) // 2 #will be used to know when to stop the first list
    
    for i in range(mid) :
        Append(L1, ptr.item) #begins creating the first list
        ptr = ptr.next
        
    while ptr is not None :
        Append(L2, ptr.item) #begins creating the second list
        ptr = ptr.next
        
    L1 = MergeSort(L1) #recursively makes the first list smaller until it cant
    L2 = MergeSort(L2) #recursively makes the second list smaller until it cant
    L = Merge(L1, L2) #my method to merge the 2 lists
    
    return L
           
def Merge(L1, L2) : #Will Merge the 2 lists for merge sort
    global mergecount
    L3 = List()
    temp1 = L1.head #will be used to traverse the lists and comapre
    temp2 = L2.head
    
    while temp1 is not None and temp2 is not None : #ensuring we are not comparing
        if(temp1.item > temp2.item) : #if the first item is greater add the second to the final list
            mergecount += 1 #global counter to keep track of compares
            Append(L3, temp2.item)
            temp2 = temp2.next
            
        else : #meaning second item is greater so add the other 
            mergecount += 1
            Append(L3, temp1.item)
            temp1 = temp1.next
        
    if temp1 == None : # we ran out of temp 1 variables to compare
        while temp2 is not None : #adding temp2 to list meanwhile not none
            Append(L3, temp2.item)
            temp2 = temp2.next
            
    if temp2 == None :
        while temp1 is not None : #we ran out of temp 2 variables to compare
            Append(L3, temp1.item) #adding left over temp1 variables to list meanwhile not none
            temp1 = temp1.next
            
    return L3
      
def QuickSort(L) :
    global qscount
    L1 = List() #will be the 2 lists used to split the problem into smaller pieces
    L2 = List()
    
    if IsEmpty(L) : #checks if list is empty before assigning pivot to anything
        return L     #return if empty
    
    if SizeList(L) == 1 : #if list is 1 we don't need to split it into smaller list
        return L
    
    else:
        piv = L.head #pivot will be used as the point where we start comparing 
        ptr = L.head.next #our pointer will start after pivot because its the 2 item in list
        
        while ptr != None : #while pointer is not none begin assignation of varibles
            
            if ptr.item < piv.item : #all items smaller than pivot go into one list
                Append(L1, ptr.item)
                qscount += 1
                
            else :
                Append(L2, ptr.item) #all other items are greater so go into another list
                qscount += 1
                
            ptr = ptr.next #doesn't let iteration stop
            
        L1 = QuickSort(L1) #recursively make problem smaller
        L2 = QuickSort(L2) #recursivelt make second lsit smaller 
        L = QuickSortMerge(L1, L2, piv) #this method will merge both lists sends pivot as well to add to list
    return L
        
def QuickSortMerge(L1, L2, piv) : #quick sort merging method
    L3 = List() #will be our final list
    temp = L1.head #will allow us to iterate the first list
    temp2 = L2.head #will allow us to iterate the second list 
    
    while temp is not None : # going through smaller list to add before pivot
         Append(L3, temp.item)
         temp = temp.next
    
    Append(L3, piv.item) #adds the pivot before adding the bigger elements 
    
    while temp2 is not None : #going through bigger list to add after pivots
        Append(L3, temp2.item)
        temp2 = temp2.next
        
    return L3
                
bubblecount = 0 #comparisons counters
mergecount = 0  
qscount = 0
  
n = 5
L = List() #Creates a random list of size 6 from random ints of 0 to 100
for i in range(n+1) :
    Append(L,random.randint(0,101))
    
#copying list to all the other lists so we can use the same list for all sorting
LBS = Copy(L) #this is the BubbleSort list
LMS = Copy(L) #this is the MergeSort list
LQS = Copy(L) #this is the QuickSort list

print('BubbleSort begin.') #LBSF = List Bubble Sort Final
Print(LBS)
LBSF = BubbleSort(LBS)
Print(LBSF)
print('Bubble Sort Median: ',Median(LBSF))
print('Bubble sort compared: ', bubblecount, ' times.', "\r\n")

print('MergeSort begin.') # LMSF = List Merge Sort Final
Print(LMS)
LMSF = MergeSort(LMS)
Print(LMSF)
print('Merge Sort Median: ',Median(LMSF))
print('Merge compared: ', mergecount, ' times.', "\r\n")

print('QuickSort begin: ')
Print(LQS)
LQSF = QuickSort(LQS)
Print(LQSF)
print('Quick Sort Median: ', Median(LQSF))
print('Quick Sort compared: ', qscount, ' times.', "\r\n")