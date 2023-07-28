#!/usr/bin/env python
# coding: utf-8

# # Reading in Files

# In[ ]:


import pandas as pd


# In[53]:


df = pd.read_csv(r"C:\Users\ethanm\Downloads\Pandas Tutorial\countries of the world.csv")
df


# In[57]:


#df = pd.read_csv(r"C:\Users\ethanm\Downloads\Pandas Tutorial\countries of the world.txt", sep = '\t')
#df

df = pd.read_table(r"C:\Users\ethanm\Downloads\Pandas Tutorial\countries of the world.txt")
df


# In[66]:


df = pd.read_json(r"C:\Users\ethanm\Downloads\Pandas Tutorial\json_sample.json")
df


# In[68]:


df2 = pd.read_excel(r"C:\Users\ethanm\Downloads\Pandas Tutorial\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')
df2


# In[65]:


pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 40)


# In[69]:


df2.info()


# In[70]:


df2.shape


# In[72]:


df2.head(10)


# In[73]:


df2.tail(10)


# In[75]:


df2['Rank']


# In[76]:


df2.loc[225]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




