#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# ![download.png](attachment:download.png)

# In[1]:


def first_func():
    print('Wed did it')


# In[2]:


first_func()


# In[3]:


def number_squared(number):
    print(number**2)


# In[4]:


number_squared(5)


# In[5]:


def number_squared(number,power):
    print(number**power)


# In[6]:


number_squared(5,3)


# In[29]:


args_tuple = (5,6,1,2,8)

def number_args(*number):
    print(number[1]*number[4])


# In[30]:


number_args(*args_tuple)


# In[6]:


def number_squared(number,power):
    print(number**power)


# In[7]:


number_squared(power = 5,number = 3)


# In[13]:


def number_kwarg(**number):
    print('My number is: ' + number['integer'] + ' My other number:' + number['integer2'])


# In[14]:


number_kwarg(integer = '2309', integer2 = '349')


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




