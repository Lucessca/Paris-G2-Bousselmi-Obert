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

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as 

#HEATMAP, Exercise 1.-------------------------------------------------------------
# Create a dataset
df = pd.DataFrame(np.random.random((5,5)), columns=["a","b","c","d","e"])
# numpy.random.random() is one of the function for doing random sampling in numpy. 
#It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).


# Default heatmap            ------- plot first heatmap
p1 = sns.heatmap(df)