#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing relevant libraries
import pandas as pd
import numpy as np
from matplotlib.pyplot import subplots


# In[7]:


# Loading dataset and fixing na values
auto = pd.read_csv('Downloads/Auto.csv', index_col = 'name', na_values=['?'])
auto


# In[9]:


# Classifying quantitative and qualititative variables
qual = ['cylinders', 'year', 'origin']
quant = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']


# In[37]:


# Finding the min and max values of each qualitative variable
results = []

for var in quant:
    min_max = auto[var].min(), auto[var].max()
    results.append(min_max)
df = pd.DataFrame(results, columns = ['Minimum', 'Maximum'], index = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration'])
df


# In[39]:


# Finding the mean and standard deviation of each qualitative variable
results2 = []

for var in quant:
    mean_std = auto[var].mean(), auto[var].std()
    results2.append(mean_std)
df2 = pd.DataFrame(results2, columns = ['Mean', 'Standard Deviation'], index = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration'])
df2


# In[15]:


# Removing the 10th through the 85th observations
auto2 = auto.drop(auto.index[10:86], axis=0)
auto2


# In[43]:


# Finding the min and max values of each qualitative variable after removing observations
results3 = []

for var in quant:
    min_max = auto2[var].min(), auto2[var].max()
    results3.append(min_max)
df3 = pd.DataFrame(results3, columns = ['New Minimum', 'New Maximum'], index = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration'])
df3


# In[51]:


# Finding the mean and standard deviation of each qualitative variable after removing observations
results4 = []

for var in quant:
    mean_std = auto2[var].mean(), auto2[var].std()
    results4.append(mean_std)
df4 = pd.DataFrame(results4, columns = ['New Mean', 'New Standard Deviation'], index = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration'])
df4


# In[23]:


# Investigating relationship among predictors visually
pd.plotting.scatter_matrix(auto[quant], figsize=(10,10));

