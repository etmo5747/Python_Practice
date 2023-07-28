#!/usr/bin/env python
# coding: utf-8

# # While Loops
# 
# ![download.png](attachment:download.png)

# In[1]:


number = 0

while number < 5:
    print(number)
    number = number + 1


# In[7]:


number = 0

while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1


# In[3]:


number = 0

while number < 5:
    print(number)
    if number == 6:
        break
    number = number + 1
else:
    print('no longer < 5')


# In[9]:


number = 0

while number < 5:
    number = number + 1
    if number == 3:
        continue
    print(number)
else:
    print('no longer < 5')


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




