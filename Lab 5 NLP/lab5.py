#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:41:32 2019

@author: SergioGramer
"""
import numpy as np
import math
import time
# Implementation of hash tables with chaining using strings

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.item = []
        self.num_items = 0
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k):
    if H.num_items // len(H.item) == 1:
        H = DoubleLoadFactor(H)
    b = h(k[0], len(H.item))
    H.item[b].append([k[0], np.array(k[1:]).astype(np.float)])
    H.num_items += 1
    return H

def DoubleLoadFactor(H) :
    H2 = HashTableC((len(H.item) * 2) + 1)
    for i in H.item : 
        if i is not [] :
            for j in i :
                H2.item[h(j[0], len(H2.item))].append([j[0], j[1]])
                H2.num_items += 1
    return H2
   
def FindC(H,k):
    b = h(k,len(H.item))
    for a in range(len(H.item[b])):
        if H.item[b][a][0] == k:
            return H.item[b][a][1]
    return -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r * n + ord(c)) % n
    return r

#############################
    #BST#
    #Copy/Pasted from lab 3
############################
    
class BST(object) :
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T, newItem) :
    if T == None:
        T = BST(newItem)
    elif T.item[0] > newItem[0]:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T

def height(T) : #finds the height of a BST
    if T is None :
        return -1
    else :
        l = 1 + height(T.left) #calculates height of left side + 1 because we already passed root
        r = 1 + height(T.right) #calcules height of right side 
    if l >= r : #if left side is greater or equal send left, no need to go further if equal
        return l
    else : #else right is greater send right
        return r
    
def Search(T, k) : #Searches a BST 'T' for item "k"
    while T is not None : #Ensures we don't traverse and empty BST
        if T.item[0] == k :
             return T.item[1]
        elif T.item[0] > k : #Compares the number are looking for to the item we are
            T = T.left    #currently at to see if it is greater, goes to left
        else : #else goes to the right side
            T = T.right
    return None

def numberOfNodes(T) : #Will count number of number if BST (T) is not none
    if T is not None :
        return 1 + numberOfNodes(T.left) + numberOfNodes(T.right) #Adds 1 because of root.
    return 0

    
#############################
    #RUN#
############################
    
print('Type "hash" for Hash Table or "bst" for Binary Search Tree')
ans = input() #will save the input as ANS
if ans == "hash" : 
        InitialTable = 69 
        print("Chose Hash Table")
        TimeStart = int(time.time()) #begins counting the time it takes to build the hash table
        H = HashTableC(InitialTable) 
        with open("glove.6B.50d.txt", encoding='utf-8') as file : #opens the glove file as 
            for line in file : #goes line by line in the file
                word = line.split(' ') #saves them as word splitting them every space
                H = InsertC(H, word) #inserts the word into the HashTable 
                
        with open("similar.words.txt", encoding='utf-8') as file2 : #opens the second file that i have the words saved in
            for line2 in file2 : #goes line by line
                word2 = line2.split() #saves the lines in word splitting them by space
                e0 = FindC(H, word2[0]) #searches the first word in the hash table and saves the numbers as e0
                e1 = FindC(H, word2[1]) #searches the second work in the hash table and saves the numbers as e1
                TimeEnd = int(time.time())
                print('Similarity of ', word2[0], ' and ', word2[1], 'is :')
                print((np.sum(e0 * e1) / (math.sqrt(np.sum(e0 * e0)) * math.sqrt(np.sum(e1 * e1)))))
            print('Time it took to build tables: ', TimeEnd - TimeStart, ' seconds.')
        count = 0
        m = H.num_items / len(H.item)
        k = 0
        for a in H.item:
            k += len(a) - m
            if a is [] : #adds one if finds an empty list
                count += 1
        d = (1 / len(H.item)) * k
        print('Initial Table Size: ', InitialTable) #prints initial hash table size
        print('Fnal Table Size: ', len(H.item)) #prints ending hash table size
        print("Percentage of empty lists:", count / len(H.item) * 100) # divides count by the length *100 to get percentage of empty lists
        print("Standard deviation of the lengths of the lists:", d) 

elif ans == "bst" :
    print("Chose Binary Search Tree")
    TimeStart = int(time.time())
    T = None
    with open("glove.6B.50d.txt", encoding='utf-8') as file :
            for line in file :
                word = line.split()
                T = Insert(T, [word[0], np.array(word[1:]).astype(np.float)])
                
    with open("similar.words.txt", encoding='utf-8') as file2 :
            for line2 in file2 :
                word2 = line2.split()
                e0 = Search(T, word2[0])
                e1 = Search(T, word2[1])
                TimeEnd = int(time.time())    
                print('Similarity of ', word2[0], ' and ', word2[1], 'is :')
                print((np.sum(e0 * e1) / (math.sqrt(np.sum(e0 * e0)) * math.sqrt(np.sum(e1 * e1)))))
            print('Time it took to build BST: ', TimeEnd - TimeStart, ' seconds.')
            print('Height of the BST: ', height(T))
            print('Number of nodes in BST: ', numberOfNodes(T))
                
else : 
    print('Try again. \nPlease type "bst" or "hash".')
                
                
