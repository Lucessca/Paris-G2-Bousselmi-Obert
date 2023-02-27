#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:32:52 2023

@author: lucobert
"""

a="hello my team - I am Luc"
b="hello my team - I am Matheo"
c="hello my team - I am Quentin"
d="hello my team - I am Martin"

print(a,b,c,d,)

#modif

#Exercise 5--------------------------------------------------------------------------

import matplotlib.pyplot as plt

column_labels = list('ABC')
row_labels = list('WXYZ')
data = np.array([[1, 2, 3], [0, 3, 2], [1, 2, 3], [4, 3, 2]]) 
fig, axis = plt.subplots() 
heatmap = axis.pcolor(data, cmap=plt.cm.Greens)
plt.savefig('test.png')
plt.show() 
