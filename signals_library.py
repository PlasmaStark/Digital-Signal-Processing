# -*- coding: utf-8 -*-
"""
@author: Ztark
signals must be defined as lambda functions, e.g.
    s = lambda x : u(x) +5*delta(-x+7)
the library mpmath works well with finite signals, I am 
trying to work with integrals to study infinite signals as well
"""



import matplotlib.pyplot as plt
import numpy as np
from mpmath import nsum, inf
# import scipy.integrate as integrate
from matplotlib.ticker import MaxNLocator

delta = lambda x : int(x==0)
u = lambda x : int(x>=0)
exp = lambda a,x : a**x
test1 = lambda x : 2*u(x)+ u(x+3) + delta(x-3) - delta(x-10) + u(-x-10+5)-3*u(x-20)-u(-x+20)
test2 = lambda x : 3*u(x)- u(4*x) + delta(x-3) + u(-x-10)-2*u(x-20)-u(-x+20)

def display(s,minim=-20,maxim=20):
    """
    display signal s between minim and maxim
    """

    x = np.linspace(minim,maxim,maxim-minim+1)
    y = np.zeros(maxim-minim+1)
    for i in range(len(x)):
        y[i] = s(x[i])
    
    fig, ax = plt.subplots()
    ax.stem(x, y,basefmt= 'C0')
    
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))   
    # plt.plot(x, y, color = "blue",linestyle='None',marker='.')
    plt.show()
    
def multiplication(a,b):
    return lambda x : a(x)*b(x) 

def convolution(a,b):
    return lambda n : int(nsum(lambda k : a(k)*b(n-k),[-inf,inf])) 

def correlation(a,b):
    return lambda n : int(nsum(lambda k : a(k)*b(k-n),[-inf,inf]))

def display_convolution(a,b,minim=-20,maxim=20):
    fig, ax = plt.subplots(3,1)
    x = np.linspace(minim,maxim,maxim-minim+1)
    ya = np.zeros(maxim-minim+1)
    yb = np.zeros(maxim-minim+1)
    conv = convolution(a,b)
    yc = np.zeros(maxim-minim+1)
    for i in range(len(x)):
        ya[i] = a(x[i])
        yb[i] = b(x[i])
        yc[i] = conv(x[i])
    ax[0].stem(x, ya,'b',markerfmt='bo',basefmt= 'C0',label='input 1')
    ax[0].yaxis.set_major_locator(MaxNLocator(integer=True))  
    ax[0].get_xaxis().set_visible(False)
    ax[1].stem(x, yb,'g',markerfmt='go',basefmt= 'C0')
    ax[1].yaxis.set_major_locator(MaxNLocator(integer=True)) 
    ax[1].get_xaxis().set_visible(False)
    ax[2].stem(x, yc,'r',markerfmt='ro')
    ax[2].yaxis.set_major_locator(MaxNLocator(integer=True)) 
    plt.show()

# def is_finite(s):
#    return (nsum(lambda k : s(k), [-inf,inf]) < (inf))

# def int_convolution(a,b):
#    return lambda n : integrate.quad(lambda k : a(k)*b(n-k),-inf,inf)[1]


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
