#!/usr/bin/env python
# coding: utf-8

# # Converting Data Types

# In[1]:


num_int = 7

type(num_int)


# In[2]:


num_str = '7'

type(num_str)


# In[4]:


num_str_conv = int(num_str)

type(num_str_conv)


# In[8]:


num_sum = num_int + num_str_conv

print(num_sum)


# In[9]:


list_type = [1,2,3]

type(list_type)


# In[11]:


type(tuple(list_type))


# In[12]:


list_type = [1,2,3,3,2,1,2,3,2,1]


# In[14]:


type(set(list_type))


# In[15]:


dict_type = {'name': 'Ethan', 'age': 23, 'hair': 'N/A'}

type(dict_type)


# In[16]:


dict_type.items()


# In[17]:


dict_type.values()


# In[18]:


dict_type.keys()


# In[20]:


type(list(dict_type.keys()))


# In[21]:


type(list(dict_type.values()))


# In[23]:


long_str = "I like to party"

set(long_str)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




