#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:58:47 2021

@author: cadecastro.com
"""
import numpy as np
import matplotlib.pyplot as plt
n=int(input("Cantidad de puntos:"))
if n<=5000:
    t=np.linspace(0,2*np.pi,n)
    x=np.zeros(n)
    y=np.zeros(n)
    r=np.sin(np.cos(np.tan(t)))
    x=r*np.cos(t);
    y=r*np.sin(t);
    plt.figure(1)
    plt.plot(x,y,'b')
    plt.axis(False)
    plt.axis('square')
    plt.title('tutor.cadecastro.com')
else:
    print('Puntos exceden máximo permitido de 5000.')