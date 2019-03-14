#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:38:43 2019

@author: SergioGramer
"""

# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified February 27, 2019
import numpy as np
import matplotlib.pyplot as plt
import math 

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
    
###### Sergio Gramer Code Begins #######  


def circle(cx, cy, rad) :
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = (cx+rad*np.sin(t))
    y = (cy+rad*np.cos(t))
    return x,y

def draw_circle(ax, cx, cy, radius) :
        x,y = circle(cx, cy, radius)
        ax.plot(x,y,color='k')
        
def circle_level(ax, n, cx, cy, radius) :
    if n > 0 :
        draw_circle(ax, cx, cy, radius)
        circle_level(ax, n-1, cx - orig_size//2, cy - 1000, radius)

    elif n == 0 :
        return

def draw_triangle(ax,p) :
        ax.plot(p[:,0],p[:,1],color='k') ## key operation to plot
        
def triangle_level(ax,n,p,w) :
    if n > 0 :
        draw_triangle(ax, p)
        q = (p * [w, 1])
        triangle_level(ax, n-1, q-[(orig_size*w)*w,orig_size],w) #will draw triangles on left hand side
        circle_level(ax, n-1, [(orig_size*w)*w], [orig_size], 100)
        triangle_level(ax, n-1, q+[orig_size - (orig_size * (w/2)), -orig_size], w) #will draw triangles on right hand
        circle_level(ax, n-1, [orig_size - (orig_size * (w/2))], [-orig_size], 100)

plt.close("all") 
orig_size = 1000
p = np.array([[orig_size,0], [500,orig_size], [0,0]])
fig, ax = plt.subplots()
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('triangle.png')

def Search(T, k) : #Searches a BST 'T' for item "k"
    while T is not None : #Ensures we don't traverse and empty BST
        if T.item == k :
             print(T.item, 'found') #Will print found once the item is found
             return T.item
        elif T.item > k : #Compares the number are looking for to the item we are
            T = T.left    #currently at to see if it is greater, goes to left
        else : #else goes to the right side
            T = T.right
    if T == None : #If we get to the end of the BST and haven't found it
        print(k, 'Not found') #print Not Found
        return T
    
def BuildList(A) : #Builds a list in O(n) time from a sorted native py list "A"
    if A is None or len(A) is 0 : #will ensure the list is not none or empty
        return None
    if len(A) == 1 : #If theres only one item in the list will return a tree of size 1
        return BST(A[0])
    else :
        mid = len(A)//2 #splits the list into 2 based on the middle item in the list
        T = BST(A[mid]) #Creates the first node in the BST with the middle value
        T.left = BuildList(A[:mid]) #Recursively makes the list shorter for the left and builds the left
        T.right = BuildList(A[mid+ 1:]) #recursively makes the list shorter for the right and builds the right
        return T

def height(T): #finds the height of a BST
    if T is None :
        return -1
    else :
        l = 1 + height(T.left) #calculates height of left side + 1 because we already passed root
        r = 1 + height(T.right) #calcules height of right side 
    if l >= r : #if left side is greater or equal send left, no need to go further if equal
        return l
    else : #else right is greater send right
        return r

def Depth(T, h) : #method that prints keys at certain depth
    for j in range(h + 1): #send in calculated height
        print('Keys at depth', j, ':') #j will let us know what level we are on
        PrintLevels(T, j) #calls print levels
        print()
    
def PrintLevels(T, j) : #print levels will ptin out the items in that particular depth of a tree
    if T is None :
        return
    if j == 0 : # if j is 0 we are at root
        print (T.item) 
    else :
        PrintLevels(T.left, j - 1) #recursively calls itself to print left child of node
        PrintLevels(T.right, j - 1) #recursively calls itself to print right child of node

    
# Code to test the functions above
i = 0
v = 0
T = None
A = [10, 4, 15, 2, 8, 1, 3, 5, 9, 7, 12, 18] #built with insert
S = [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 15, 18] #built with Sorted python list
for a in A:
    T = Insert(T,a)
T = BuildList(S)  
InOrder(T)
print()
InOrderD(T,'')
print()
Search(T, 10)
h = height(T)
Depth(T, h)
