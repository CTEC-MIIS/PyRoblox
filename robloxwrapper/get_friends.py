#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
cwd = os.getcwd()
os.chdir("C:\\Users\\Alex\\pyroblox")
from . import session
os.chdir(cwd)


# In[11]:


class friends(object):
    def __init__(self, id):
        self.id = id
    def info(self):
        path = 'https://friends.roblox.com/v1/users/{}/friends'.format(self.id)
        response = session.get(path)
        return response.json()


# In[ ]:




