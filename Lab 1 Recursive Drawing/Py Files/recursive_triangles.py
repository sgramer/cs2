#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 20:13:04 2019

@author: SergioGramer
"""

import numpy as np
import matplotlib.pyplot as plt

def draw_triangle(ax,p) :
        ax.plot(p[:,0],p[:,1],color='k') ## key operation to plot
        
def triangle_level(ax,n,p,w) :
    if n > 0 :
        draw_triangle(ax, p)
        q = (p * [w, 1])
        triangle_level(ax, n-1, q-[(orig_size*w)*w,orig_size],w) #will draw triangles on left hand side
        triangle_level(ax, n-1, q+[orig_size - (orig_size * (w/2)), -orig_size], w) #will draw triangles on right hand

plt.close("all") 
orig_size = 1000
p = np.array([[orig_size,0], [500,orig_size], [0,0]])
fig, ax = plt.subplots()
triangle_level(ax,5,p,.5)
ax.set_aspect(1.0)
#ax.axis('off')
plt.show()
fig.savefig('triangle.png')