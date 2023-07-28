#!/usr/bin/env python
# coding: utf-8

# # Group by and Aggregating

# In[2]:


import pandas as pd


# In[4]:


df = pd.read_csv(r"C:\Users\ethanm\Downloads\Flavors.csv")
df


# In[6]:


group_by_frame = df.groupby('Base Flavor')


# In[10]:


group_by_frame.mean(numeric_only = True)


# In[12]:


df.groupby('Base Flavor').mean(numeric_only = True)


# In[14]:


df.groupby('Base Flavor').count()


# In[18]:


df.groupby('Base Flavor').sum(numeric_only = True)


# In[20]:


df.groupby('Base Flavor').agg({'Flavor Rating': ['mean','max','count','sum'], 'Texture Rating': ['mean','max','count','sum']})


# In[26]:


df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Rating': ['mean','max','count','sum']})


# In[28]:


df.groupby('Base Flavor').describe()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




