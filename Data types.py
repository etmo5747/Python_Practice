#!/usr/bin/env python
# coding: utf-8

# # Data Types

# In[2]:


type(-12 + 100)


# In[3]:


type(12 + 10.25)


# In[6]:


type(12 + 3J)


# In[9]:


#Boolean

type(1 > 5)


# In[15]:


1 > 5


# In[16]:


#Strings

'Single Quote'


# In[18]:


"double quote"


# In[28]:


multiline = """
Meghan Gobuty,
I lover her morely
except when she gives me a swirly,
so poorely.

"""


# In[29]:


print(multiline)


# In[30]:


"""
I've always wanted to eat a gallon of "ice cream"
"""


# In[31]:


type(multiline)


# In[34]:


a = 'Hello World!'


# In[38]:


print(a[2:5])


# In[41]:


a*3


# In[42]:


a + a


# In[ ]:





# In[43]:


# List

[1,2,3]


# In[44]:


['Cookie Dough','Strawberry','Chocolate']


# In[46]:


['Vanilla', 3, ['Scoops','spoon'],True]


# In[48]:


ice_cream = ['Cookie Dough','Strawberry','Chocolate']

ice_cream.append('Salted Caramel')

ice_cream


# In[49]:


ice_cream[0] 


# In[50]:


ice_cream[0] = 'Butter Pecan'

ice_cream


# In[52]:


nested_list = ['Vanilla', 3, ['Scoops','spoon'],True]


# In[57]:


nested_list[2][1]


# In[ ]:





# In[59]:


# Tuple

tuple_scoops = (1,2,3,2,1)


# In[60]:


type(tuple_scoops)


# In[61]:


tuple_scoops[0]


# In[62]:


tuple_scoops.append(3)


# In[ ]:





# In[63]:


# sets

daily_pints = {1,2,3}


# In[64]:


type(daily_pints)


# In[65]:


daily_pints


# In[67]:


daily_pints_log = {1,2,31,2,3,4,1,2,5,6,3,2}


# In[68]:


daily_pints_log 


# In[69]:


wifes_daily_pints_log = {1,3,5,7,3,24,5,7,3,2,0}


# In[70]:


print(daily_pints_log | wifes_daily_pints_log)


# In[71]:


print(daily_pints_log & wifes_daily_pints_log)


# In[72]:


print(daily_pints_log - wifes_daily_pints_log)


# In[73]:


print(daily_pints_log ^ wifes_daily_pints_log)


# In[ ]:





# In[75]:


# dictionaries
# key/value pair

dict_cream = {'name': 'Ethan Moskowitz', 'weekly intake': 5, 'favorite ice creams':['MCC','Chocolate']}


# In[76]:


type(dict_cream)


# In[77]:


dict_cream


# In[78]:


dict_cream.values()


# In[79]:


dict_cream.keys()


# In[80]:


dict_cream.items()


# In[81]:


dict_cream['name']


# In[82]:


dict_cream['name'] = 'Meghan Gobuty'

print(dict_cream)


# In[88]:


dict_cream.update({'name': 'Ethan Moskowitz', 'weekly intake': 5, 'weight':300})

print(dict_cream)


# In[89]:


del dict_cream['weight']

print(dict_cream)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




