
"""
Created on Fri Feb  8 11:43:29 2019

@author: SergioGramer
"""

import matplotlib.pyplot as plt
import numpy as np
import math 

def circle(cx, cy, rad) :
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = (cx+rad*np.sin(t))
    y = (cy+rad*np.cos(t))
    return x,y

def draw_circle(ax, cx, cy, radius) :
        x,y = circle(cx, cy, radius)
        ax.plot(x,y,color='k')
        
def circle_level(ax, n, cx, cy, radius, w) :
    if n > 0 :
        draw_circle(ax, cx, cy, radius*w)
        circle_level(ax, n-1, cx-(radius-(radius*w))*w, cy, (radius*w), w)

    elif n == 0 :
        return

orig_size = 1000
fig, ax = plt.subplots()   
plt.close("all") 
fig, ax = plt.subplots() 
circle_level(ax, 10, orig_size, orig_size, 500, .5)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')


