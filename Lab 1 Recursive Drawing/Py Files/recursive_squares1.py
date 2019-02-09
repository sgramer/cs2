#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 11:12:01 2019

@author: SergioGramer
"""
import numpy as np
import matplotlib.pyplot as plt

#this function will draw the square
def draw_square(ax,p):
        ax.plot(p[:,0],p[:,1],color='k') ## key operation to plot

#this function will determine which "level" the square is on
#n deteremines the "level"
def square_level(ax,n,p,w): 
    if n > 0:
        draw_square(ax,p) #will ensure a square is drawn given parameters.
        q = p*w
        square_level(ax,n-1,q + [-x , -y],w) #These parameters ensure the recursion
        square_level(ax,n-1,q + [x , y],w)  #call repeats itself enough times to 
        square_level(ax,n-1,q + [x, -y],w)  #make all of the squares while modifying its 
        square_level(ax,n-1,q + [-x, y],w)  #x & y values 
    else :
        return
        

plt.close("all")
orig_size = 1000 #to simplify numbers i chose 1000 arbitrarily
x = orig_size / 2 #will control the x axis point
y = orig_size / 2 #will control y could have been the same var X but for readability  
p = np.array([[-x,-y],[-x,y],[x,y],[x,-y],[-x,-y]])
fig, ax = plt.subplots()
square_level(ax,4,p,.5) #changing n will control variables.
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('squares.png')