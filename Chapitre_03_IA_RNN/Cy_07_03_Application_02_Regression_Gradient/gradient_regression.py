# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:19:50 2023

@author: xpess
"""

# On cherche la droite passant au mieux de 3 points

x0,y0 = 1,2
x1,y1 = 1.5,3.5
x2,y2 = 2,4

import matplotlib.pyplot as plt

def cout(a,b):
    return (y0-a*x0-b)**2+(y1-a*x1-b)**2+(y2-a*x2-b)**2

def dcouta(a,b):
    return 2*a*(x0**2+x1**2+x2**2)+2*b*(x0+x1+x2)-2*(x0*y0+x1*y1+x2*y2)

def dcoutb(a,b):
    return 6*b + 2*a*(x0+x1+x2)- 2*(y0+y1+y2)


def grad(eta):
    cpt = 0
    a=1
    b=0
    
    cc = [cout(a,b)]
    while cpt<30:
        a2 = a - eta*dcouta(a,b)
        b2 = b - eta*dcoutb(a,b)
        cc.append(cout(a2,b2))
        a,b = a2,b2
        cpt+=1
    print(a,b)
    return cc

cc1= grad(0.001)
cc2= grad(0.1)
cc3= grad(0.01)
plt.plot(cc1,label="0.001")
plt.plot(cc2,label="0.1")
plt.plot(cc3,label="0.01")
plt.legend()
plt.show()

plt.figure()
plt.plot([x0,x1,x2],[y0,y1,y2],"rs")
import numpy as np
lesx = np.linspace(x0,x2)
lesy = 1.8059761364223472*lesx+ 0.47085679136609987
plt.plot(lesx,lesy)
plt.show()