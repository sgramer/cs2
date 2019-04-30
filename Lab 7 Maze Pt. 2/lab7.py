#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:02:42 2019

@author: Sergio Gramer
Instructor: Dr. Olac Fuentes
TA: Anindita Nath, Maliheh Zargaran
Purpose: The purpose of this lab is to use the previous lab (lab 6) and create a maze 
         and to remove (< n-1) walls and (n-1 < ) walls and see what happens and display a message depending
         which one you chose. Build an adjacency list based on the maze and implement the following:
         Breadth-First Search, Depth First Search using a stack and Depth First Search using recursion.
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
import queue
##############################################################################
#                                                                           #
#                       """ GIVEN """                                       #
#                                                                           #
##############################################################################

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
    return ax

def path(plot, prev, vert, edgex, edgey) : #we used our axplot to generate the path(Red) from beginning to end if it exists
    if prev[vert] != -1: #when prev does not equal -1 it will continue. 
        if (vert - 1) == prev[vert] : #if the prev vertice is equal to vert -1
            x1 = edgex - 1
            y1 = edgey
            path(plot, prev, prev[vert], x1, y1)
            plot.plot([x1, edgex], [y1, edgey], linewidth = 2, color = 'r')         
        if (vert + 1) == prev[vert] :
            x1 = edgex + 1
            y1 = edgey
            path(plot, prev, prev[vert], x1, y1)
            plot.plot([x1, edgex],[y1, edgey], linewidth = 2, color = 'r')
        if (vert - maze_cols) == prev[vert] :
            x1 = edgex
            y1 = edgey - 1
            path(plot, prev, prev[vert], x1, y1)
            plot.plot([x1, edgex], [y1, edgey], linewidth = 2, color = 'r')
        if  (vert + maze_cols) == prev[vert] :
            x1 = edgex
            y1 = edgey + 1
            path(plot, prev, prev[vert], x1, y1)
            plot.plot([x1, edgex], [y1, edgey], linewidth = 2, color = 'r')       
        
    
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


##############################################################################
#                                                                           #
#                       """LAB 6 """                                        #
#                                                                           #
##############################################################################
    
def MazeStandardUnion(S) : #will use the standard union method to create the maze
    while NumSets(S) > 1 : #will execute so long as the number of sets is greater than 1
        d = random.randint(0, len(walls)-1) # d is the random integer we create to remove walls based on that integer
        if union(S, walls[d][0], walls[d][1]) is True : #uses the true or false statement inside of the union 
            walls.pop(d)                                #to decide if we execute

def MazeCompression(S) : #will use the Union_c with compression to create the maze
    while NumSets(S) > 1 : 
        d = random.randint(0, len(walls)-1)
        if union_c(S, walls[d][0], walls[d][1]) is True :
            walls.pop(d)
            
##############################################################################
#                                                                           #
#                       """ LAB 7 """                                       #

def MazeWalls(S, m) : #will use the Union_c with compression to create the maze
    wall_pop = [] #this list is used to keep track of the walls that we are popping
                    #for the purpose of creating an adjacency list
    while m > 0 : 
        d = random.randint(0, len(walls)-1)
        if m > len(walls)-1 : #m is the variable input by the user, if M is greater than the number of walls. jump out
            print('Number of walls you want to remove is greater than the number of walls that exist.')
            return
        
        if NumSets(S) == 1 : #when there is 1 set in the disjoint set forest start removing walls without union
            wall_pop.append(walls.pop(d))
            m = m - 1
            
        elif union(S, walls[d][0], walls[d][1]) is True: #keep removing walls with a union to create a set in the dsf
            wall_pop.append(walls.pop(d))
            m = m - 1
            
    return wall_pop #returns the list to use for creating the adjacency list

#def MazeSearch(M, i) : #
#    for j in M :
#        if j == i :
#            j += 1
#            
#        if find(M, i) == find(M, j) :
#            return True
#        
#    return False

def MazeAdjacencyList(M, wall_pop) : #used to create an adjacency list
    G = [] #this will be the list that our adjacency list goes into
    for i in range(maze_rows * maze_cols) : #we are creating a list of size rows* cols 
        G.append([])                        #full of empty lists ([])

    for i in range(len(wall_pop)) : #we are now populating the empty lists with the list of popped walls we generated on the last method
        fi = wall_pop[i][0] #by popping from this list and saving the variable we ensure proper insertion of items
        se = wall_pop[i][1]
        G[fi].append(se) #we now append what was in the second item into the index of the first
        G[se].append(fi) #we now append what was in the first item into the index of the second
        #this is done to ensure that we populate the correct indexes with the correct numbers
    
    for j in range(len(G)) : #we sort the individual lists inside of our adjancency list for readabililty
        G[j].sort()
    
    return G

def BreadthFirstSearch(adj_list) :
    vis = [False] * len(adj_list) #generating an array with False inside the size of the adjacency list
    prev = [-1] * len(adj_list) #Generating an array with -1 to see what was our previous -1 means there was no previous
    Q = queue.Queue() #creating our Queue
    Q.put(0) #we put 0 in our q because we always begin with this and to jump into our while loop
    vis[0] = True #the list with false now at 0 is true because we have visited this according to our q
    
    while Q.empty() is False : #while our q is not empty we get the next item in the list and save it as v
        v = Q.get()
        for i in adj_list[v] : #for every variable inside of index v in our adjacency list we 
            if not vis[i] :   #check to see if it has been visited if not we visit and put true
                vis[i] = True
                prev[i] = v  #now our previous list will show which number was the previous
                Q.put(i) #and put the items of i inside of the Q
                
    return prev

def DepthFirstSearch(adj_list) : #same comments as BreathFirstSearch method except
    vis = [False] * len(adj_list)
    prev = [-1] * len(adj_list)
    st = []     #we are using a list as a stack
    st.append(0) 
    vis[0] = True
    
    while st :
        v = st.pop()
        for i in adj_list[v] :
            if not vis[i] :
                vis[i] = True
                prev[i] = v
                st.append(i)
                
    return prev

def DepthFirstSearchRecursively(adj_list, s) : 
    vis[s] = True #same concept as the first depthfirstsearch except recursively
    #we created the visitied (vis) list outside of the method. populated the Source(s) with true
    for c in adj_list[s] : #for every element of the source(s) inside of the adjacency list
        if not vis[c] : #is has not been visited
            prev[c] = s #populate our list previous(prev) with the items (this list was also generated outside of the method)
            DepthFirstSearchRecursively(adj_list, c) #recursively call the method thus shortening our problem
            
    return prev #once done. return the list prev populated
##############################################################################
#                                                                           #
#                       """ MAIN """                                        #                                                                          #
plt.close("all") 
maze_rows = 5
maze_cols = 5

walls = wall_list(maze_rows,maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
TimeStart = datetime.now()
M = DisjointSetForest(maze_rows * maze_cols)
print('The Number of cells in this maze are: ', maze_rows * maze_cols)

print('Please enter the number of walls you would like to remove.')
m = int(input())
if m > ((maze_rows * maze_cols) - 1) :
    print('There is at least one path from source to destination.')
if m == ((maze_rows * maze_cols) - 1) :
    print('There is a unique path from source to destination.')
if m < ((maze_rows * maze_cols) - 1) :
    print('A path from source to destination is not guaranteed to exist.')
wall_pop = MazeWalls(M, m)
adj_list = MazeAdjacencyList(M, wall_pop)
print('Adjacency List: ', adj_list)
az = draw_maze(walls,maze_rows,maze_cols)
plt.show()
print('Disjoint Set Forest Maze: ', M)
bsf = BreadthFirstSearch(adj_list)
print('Breadth First Search: ', bsf)
dfs = DepthFirstSearch(adj_list)
print('Depth First Search: ', dfs)
vis = [False] * len(adj_list)
prev = [-1] * len(adj_list)
dfsr = DepthFirstSearchRecursively(adj_list, 0)
print('Depth First Search Recursively: ', dfsr)
path(az, bsf, (maze_rows * maze_cols)-1, maze_cols-.5, maze_rows-.5)
TimeEnd = datetime.now()
print('Time to build and print maze: ', TimeEnd - TimeStart, ' seconds.')
