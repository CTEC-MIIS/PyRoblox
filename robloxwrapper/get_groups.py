#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
from . import sess


# In[11]:

class groups(object):
    def __init__(self, id):
        self.id = id
    def allies(self):
        path = "https://groups.roblox.com/v1/groups/{}/relationships/Allies?model.startRowIndex=0&model.maxRows=100000".format(self.id)
        response = sess.get(path)
        return response.json()
    def enemies(self):
        path = "https://groups.roblox.com/v1/groups/{}/relationships/Enemies?model.startRowIndex=0&model.maxRows=100000".format(self.id)
        response = sess.get(path)
        return response.json()
    def user_list(self):
        path = "https://groups.roblox.com/v1/groups/{}/users?sortOrder=Asc&limit=10".format(self.id)
        response = sess.get(path)
        return response.json()
    def info(self):
        path = "https://groups.roblox.com/v1/groups/{}".format(self.id)
        response = sess.get(path)
        return response.json()


# In[ ]:
