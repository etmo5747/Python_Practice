#!/usr/bin/env python
# coding: utf-8

# # Filtering and Ordering

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"C:\Users\ethanm\Downloads\world_population.csv")


# In[3]:


df


# In[5]:


df[df['Rank'] <= 10]


# In[7]:


specific_countries = ['Bangladesh','Brazil']

df[df['Country'].isin(specific_countries)]


# In[8]:


df[df['Country'].str.contains('United')]


# In[9]:


df2 = df.set_index('Country')
df2


# In[14]:


df2.filter(items = ['Continent','CCA3'], axis = 1)


# In[21]:


df2.filter(items = ['Zimbabwe'], axis = 0)


# In[19]:


df2.filter(like = 'United', axis = 0)


# In[22]:


df2.loc['United States']


# In[23]:


df2.iloc[3]


# In[34]:


df[df['Rank'] < 10].sort_values(by=['Continent','Country'],ascending=[False,True])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




