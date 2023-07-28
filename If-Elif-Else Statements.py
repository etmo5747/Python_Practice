#!/usr/bin/env python
# coding: utf-8

# # If - Elif- Else Statements![Screenshot%202021-06-07%20at%201.08.41%20PM.png](attachment:Screenshot%202021-06-07%20at%201.08.41%20PM.png)

# In[1]:


if 25 > 10:
    print('It worked!')


# In[4]:


if 25 < 10:
    print('It worked!')
else:
    print('It did not work...')


# In[9]:


if 25 < 10:
    print('It worked!')
elif 25 < 20:
    print('Elif worked!')
elif 25 < 21:
    print('Elif 2 worked!')
elif 25 < 40:
    print('Elif 3 worked!')
elif 25 < 50:
    print('Elif 4 worked!')
else:
    print('It did not work...')


# In[10]:


if (25 < 10) or (1 < 3):
    print('It worked!')
elif 25 < 20:
    print('Elif worked!')
elif 25 < 21:
    print('Elif 2 worked!')
elif 25 < 40:
    print('Elif 3 worked!')
elif 25 < 50:
    print('Elif 4 worked!')
else:
    print('It did not work...')


# In[11]:


print('it worked!') if 10>30 else print ('it did not work...')


# In[13]:


if (25 < 10) or (1 < 3):
    print('It worked!')
    if 10>5:
        print('this nested if statement worked!')
elif 25 < 20:
    print('Elif worked!')
elif 25 < 21:
    print('Elif 2 worked!')
elif 25 < 40:
    print('Elif 3 worked!')
elif 25 < 50:
    print('Elif 4 worked!')
else:
    print('It did not work...')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




