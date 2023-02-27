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
e="hello my team - I am Benjamin"
print(a,b,c,d,e)

#modif
#Exercise2-----------------------------------Measuring Correlations-------------------
# Create a dataset
df = pd.DataFrame(np.random.random((100,5)), columns=["a","b","c","d","e"])
 
# Calculate correlation between each pair of variable
corr_matrix=df.corr()            # gives me matrix 5/5
 
# plot it
sns.heatmap(corr_matrix, cmap='PuOr')
# cmap='PuOr' : for color option
#Change it 
# https://matplotlib.org/stable/gallery/color/colormap_reference.html
sns.heatmap(corr_matrix, cmap='seismic')