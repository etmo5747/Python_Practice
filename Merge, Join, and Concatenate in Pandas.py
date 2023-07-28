#!/usr/bin/env python
# coding: utf-8

# # Merge, Join, and Concatenate

# In[1]:


import pandas as pd


# In[5]:


df1 = pd.read_csv(r"C:\Users\ethanm\Downloads\LOTR.csv")
df1


# In[6]:


df2 = pd.read_csv(r"C:\Users\ethanm\Downloads\LOTR 2.csv")
df2


# In[10]:


df1.merge(df2, how = 'inner', on = ['FellowshipID','FirstName'])


# In[11]:


df1.merge(df2, how = 'outer')


# In[12]:


df1.merge(df2, how = 'left')


# In[13]:


df1.merge(df2, how = 'right')


# In[14]:


df1.merge(df2, how = 'cross')


# In[16]:


df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left', rsuffix = '_Right')


# In[18]:


df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left', rsuffix = '_Right', how = 'outer')
df4


# In[27]:


pd.concat([df1,df2], join = 'outer', axis = 1)


# In[28]:


df1.append(df2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




