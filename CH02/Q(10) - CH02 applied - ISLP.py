#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib.pyplot import subplots


# In[117]:


bos = pd.read_csv('Downloads/Boston.csv', index_col=0)
bos.rename_axis('suburb')


# In[33]:


# How many rows and columns in the dataframe?
rows = bos.shape[0]
columns = bos.shape[1]
print('This dataset has {0} rows and {1} columns'.format(rows, columns))


# In[51]:


# Making pairwise scatterplots for quantatitive variables
quant = bos.drop('chas', axis=1)
pd.plotting.scatter_matrix(quant, figsize=(10,10));


# In[41]:


corr = quant.corr() #for numerical confirmation
corr.style.background_gradient(cmap='coolwarm')


# In[39]:


#Highest crimes rates, tax rates and pupil-teacher ratios
vars = ['crim', 'tax', 'ptratio']

for var in vars:
    sorted_var = bos.loc[:,var].sort_values(ascending=False)
    print(pd.DataFrame(sorted_var))


# In[25]:


# Calculating each predictors' range
ranges = []
for var in quant.columns:
    range_value = quant[var].max() - quant[var].min()
    ranges.append([var, range_value])
# Create a DataFrame for better formatting
range_df = pd.DataFrame(ranges, columns=['Variable', 'Range']).transpose()
range_df


# In[19]:


# How many of the suburbs set bound the Charles river?
print('There are' ,np.sum(bos['chas'] == 1, axis = 0), 'suburbs bound to the charles river')


# In[17]:


# What is the median pupil-teacher ratio among the towns?
print('The median pupil-teacher ratio among the towns is {0}'.format(np.median(bos['ptratio'])))


# In[103]:


# Which suburb of Boston has lowest median value of owner occupied homes?
low_medv = bos.sort_values('medv')
print('The suburbs with lowest median values of owner occupied homes has a median of',bos['medv'].min()) 
# Suburbs number 399 & 406 has the lowest median values of owner occupied homes
preds = []

for suburb in [398,405]:
    low_medv_pred = quant.iloc[suburb,]
    preds.append(low_medv_pred)
df = pd.DataFrame(preds)
df


# In[75]:


# How many of the suburbs average more than seven rooms per dwelling? More than eight rooms per dwelling?
for val in [7,8]:
    avg_per_dwelling = bos[bos['rm'] > val].value_counts().sum()
    print('There are',avg_per_dwelling, 'suburbs with more than {0} rooms per dwelling'.format(val))

