#!/usr/bin/env python
# coding: utf-8

# # Indexing

# In[2]:


import pandas as pd


# In[4]:


df = pd.read_csv(r"C:\Users\ethanm\Downloads\world_population.csv")
df


# In[5]:


df = pd.read_csv(r"C:\Users\ethanm\Downloads\world_population.csv", index_col = 'Country')
df


# In[6]:


df.reset_index(inplace=True)
df


# In[9]:


df.set_index('Country', inplace = True)
df


# In[12]:


df.iloc[1]


# In[16]:


df.loc['Albania']


# In[30]:


df.reset_index(inplace = True)


# In[31]:


df.set_index(['Continent','Country'], inplace = True)
df


# In[41]:


df.sort_index(ascending=[False, True])

#pd.set_option('display.max.rows', 235)


# In[43]:


df.loc['Africa','Angola']


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




