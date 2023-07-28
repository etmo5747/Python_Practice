#!/usr/bin/env python
# coding: utf-8

# # Find and Find_all

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


url = 'https://www.scrapethissite.com/pages/forms/'


# In[4]:


page = requests.get(url)


# In[5]:


soup = BeautifulSoup(page.text, 'html')


# In[6]:


print(soup)


# In[7]:


soup.find('div')


# In[15]:


soup.find_all('p', class_ = 'lead')


# In[17]:


soup.find('p', class_ = 'lead').text.strip()


# In[21]:


soup.find_all('th')


# In[24]:


soup.find('th').text.strip()


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




