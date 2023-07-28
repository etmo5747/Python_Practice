#!/usr/bin/env python
# coding: utf-8

# # For Loops
# 
# 
# ![download.png](attachment:download.png)

# In[2]:


integers = [1,2,3,4,5]


# In[3]:


for number in integers:
    print(number)


# In[4]:


for number in integers:
    print('yep!')


# In[ ]:


integers = [1,2,3,4,5]


# In[5]:


for Jelly in integers:
    print(Jelly + Jelly)


# In[6]:


ice_cream_dict = {'name': 'Ethan Moskowitz', 'weekly intake': 5, 'favorite ice creams': ['MCC', 'Chocolate']}


# In[7]:


for cream in ice_cream_dict.values():
    print(cream)


# In[8]:


for key, value in ice_cream_dict.items():
    print(key, '->',value)


# In[12]:


flavors = ['Vanilla','Chocolate','Cookie Dough']
toppings = ['Hot fudge','oreos','Marshmallows' ]


# In[13]:


for one in flavors:
    for two in toppings:
        print(one, 'topped with', two)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




