# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:18:07 2019

@author: User
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv ('activation.csv')
print (df)
df = pd.read_csv('activation.CSV', nrows=100, header=[59])
df.drop(['Unnamed: 0'], axis=1)
print (df)
df.drop(df.columns[[0, 1]], axis = 1, inplace = True) 
print (df)
df.plot (x='s', y='V vs. Ref.')
print (df)