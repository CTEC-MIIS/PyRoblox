#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
from . import sess


# In[11]:


class friends(object):
    def __init__(self, id):
        self.id = id
    def info(self):
        path = 'https://friends.roblox.com/v1/users/{}/friends'.format(self.id)
        response = sess.get(path)
        return response.json()
    def user_info(self):
        path = 'https://users.roblox.com/v1/users/{}'.format(self.id)
        response = sess.get(path)
        return response.json()

# In[ ]:
