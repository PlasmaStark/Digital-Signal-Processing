# -*- coding: utf-8 -*-
"""
@author: Ztark
signals must be defined as lambda functions, e.g.
    s = lambda x : u(x) +5*delta(-x+7)
"""



import matplotlib.pyplot as plt
import numpy as np
from mpmath import nsum, inf

delta = lambda x : int(x==0)
u = lambda x : int(x>=0)
exp = lambda a,x : a**x

def display(minim,maxim,s):
    """
    display signal s between minim and maxim
    """
    x = np.linspace(minim,maxim,maxim-minim+1)
    y = np.zeros(maxim-minim+1)
    for i in range(len(x)):
        y[i] = s(x[i])
        
    fig, ax = plt.subplots()
    ax.stem(x, y,basefmt= 'C0')
    # plt.plot(x, y, color = "blue",linestyle='None',marker='.')
    plt.show()
    
def multiplication(a,b):
    return lambda x : a(x)*b(x) 

def convolution(a,b):
    return lambda n : nsum(lambda k : a(k)*b(n-k),[-inf,inf])   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    