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

#Exercise 3.----------------------------------------------------------------------
#HALF CORRELATION MATRIX
import seaborn as sns
import pandas as pd
import numpy as np
np.random.seed(0)
 
# Create a dataset
df = pd.DataFrame(np.random.random((100,5)), columns=["a","b","c","d","e"])

# Calculate correlation between each pair of variable
corr_matrix=df.corr()
 
# Can be great to plot only a half matrix
# Generate a mask for the upper triangle
mask = np.zeros_like(corr_matrix)
mask[np.triu_indices_from(mask)] = True

# Draw the heatmap with the mask
sns.heatmap(corr_matrix, mask=mask, square=True, cmap='rainbow')


#TESTTESTETSTETSTETS