#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
from . import sess


# In[11]:


class group_games(object):
    def __init__(self, id):
        self.id = id
    def info(self):
        path = 'https://games.roblox.com/v2/groups/{}/games?sortOrder=Asc&limit=100'.format(self.id)
        response = sess.get(path)
        return response.json()


class user_games(object):
    def __init__(self, id):
        self.id = id
    def games_list(self):
        path = 'https://games.roblox.com/v2/users/{}/games?sortOrder=Asc&limit=50'.format(self.id)
        response = sess.get(path)
        return response.json()
    def favorites_list(self, cursor=None):
        if cursor is not None:
            path = "https://games.roblox.com/v2/users/{}/favorite/games?sortOrder=Asc&limit=50&cursor={}".format(self.id, cursor)
            response = sess.get(path)
            return response.json()
        else:
            path = "https://games.roblox.com/v2/users/{}/favorite/games?sortOrder=Asc&limit=50".format(self.id)
            response = sess.get(path)
            return response.json()
