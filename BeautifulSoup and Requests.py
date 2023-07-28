#!/usr/bin/env python
# coding: utf-8

# # BeautifulSoup and Requests

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://www.scrapethissite.com/pages/forms/'


# In[4]:


page = requests.get(url)


# In[6]:


soup = BeautifulSoup(page.text, 'html')


# In[7]:


print(soup)


# In[8]:


print(soup.prettify())


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




