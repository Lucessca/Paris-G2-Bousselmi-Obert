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
# Create a dataset
df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])

# plot a heatmap with annotation
sns.heatmap(df, cmap='rainbow', annot=True, annot_kws={"size": 7})