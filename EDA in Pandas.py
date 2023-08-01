#!/usr/bin/env python
# coding: utf-8

# # EDA in Pandas

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv(r"C:\Users\ethanm\Downloads\world_population.csv")
df


# In[4]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[7]:


df.info()


# In[8]:


df.describe()


# In[12]:


df.isnull().sum()


# In[13]:


df.nunique()


# In[20]:


df.sort_values(by="World Population Percentage", ascending=False).head(10)


# In[21]:


df.corr()


# In[31]:


sns.heatmap(df.corr(), annot = True)

plt.rcParams['figure.figsize'] = (15,8)

plt.show()


# In[38]:


df.groupby('Continent').mean('numeric_only').sort_values(by="2022 Population", ascending=False)


# In[37]:


df[df['Continent'].str.contains('Oceania')]


# In[51]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean('numeric_only').sort_values(by="2022 Population", ascending=False)
df2


# In[45]:


df.columns


# In[53]:


df3 = df2.transpose()
df3


# In[54]:


df3.plot()


# In[58]:


df.boxplot(figsize=(20,10))


# In[ ]:





# In[59]:


df


# In[63]:


df.select_dtypes(include='object')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




