#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:24:47 2019

@author: SergioGramer
"""

# Starting point for program to build and draw a maze
# Modify program using disjoint set forest to ensure there is exactly one
# simple path joiniung any two cells
# Programmed by Olac Fuentes
# Last modified March 28, 2019

import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime



def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w
# Implementation of disjoint set forest 
# Programmed by Olac Fuentes
# Last modified March 28, 2019

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
   
  
def dsfToSetList(S):
    #Returns aa list containing the sets encoded in S
    sets = [ [] for i in range(len(S)) ]
    for i in range(len(S)):
        sets[find(S,i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r
    
def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri #uses true or false to return for whether the method 
        return True #should execute or skip
    return False
         
def union_by_size(S,i,j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree 
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        if S[ri]>S[rj]: # j's tree is larger
            S[rj] += S[ri] #uses true or false to return for whether the method 
            S[ri] = rj     #should execute or skip
        else:
            S[ri] += S[rj]
            S[rj] = ri

def NumSets(S):
    count =0
    for i in S:
        if i < 0:
            count += 1
    return count

def MazeStandardUnion(S) : #will use the standard union method to create the maze
    while NumSets(S) > 1 : #will execute so long as the number of sets is greater than 1
        d = random.randint(0, len(walls)-1) # d is the random integer we create to remove walls based on that integer
        if union(S, walls[d][0], walls[d][1]) is True : #uses the true or false statement inside of the union 
            walls.pop(d)                                #to decide if we execute

def MazeCompression(S) : #will use the Union_c with compression to create the maze
    while NumSets(S) > 1 : 
        d = random.randint(0, len(walls)-1)
        if union_c(S, walls[d][0], walls[d][1]) is True:
            walls.pop(d)

plt.close("all") 
maze_rows = 10
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
M = DisjointSetForest(maze_rows * maze_cols)
print('Type "standard" to use Standard Union \nType "comp" for Union by Compression')
choice = input()
if choice == "standard" :
    TimeStart = datetime.now()
    print('Chose standard')
    MazeStandardUnion(M)
    draw_maze(walls,maze_rows,maze_cols)
    plt.show()
    TimeEnd = datetime.now()
    print('It took ', TimeEnd - TimeStart, ' seconds to create the maze using Standard Union.')
    
elif choice == "comp" :
    TimeStart = datetime.now()
    print('Chose size')
    MazeCompression(M)
    draw_maze(walls,maze_rows,maze_cols)
    plt.show()
    TimeEnd = datetime.now()
    print('It took ', TimeEnd - TimeStart, ' seconds to create the maze using Path Compression.')
else :
    print("Please type the provided choices")
 
