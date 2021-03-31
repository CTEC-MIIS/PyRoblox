#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
cwd = os.getcwd()


# In[17]:


os.chdir("C:\\Users\\Alex\\pyroblox")


# In[18]:


from robloxwrapper import friends
from pytest import fixture
import vcr
#@vcr.use_cassette('tests\\vcr_cassettes\\friends-info.yml')


# In[4]:


os.chdir(cwd)


# In[5]:


@fixture
def friends_keys():
    return ["data"]


# In[13]:


def test_friends_info():
    friends_instance = friends(2469648521)
    response = friends_instance.info()
    
    assert isinstance(response, dict)
    assert response['id'] == 2469648521, "The user ID should be in response"
    assert set(friends_keys).issubset(response.keys()), "All keys should be in the response"


# In[14]:


test_friends_info()


# In[ ]:




