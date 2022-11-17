#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os

from robloxwrapper import friends, groups
from pytest import fixture
import vcr

@fixture
def friends_keys():
    return ["data"]


# In[13]:

@vcr.use_cassette('tests/vcr_cassettes/friends-info.yml')
def test_friends_info():
    friends_instance = friends(724484845)
    response = friends_instance.info()
    #print(response)
    assert isinstance(response, dict)
    #assert set(friends_keys).issubset(response.keys()), "All keys should be in the response"

@vcr.use_cassette('tests/vcr_cassettes/groups-info.yml')
def test_groups_info():
    groups_instance = groups(5351020)
    response = groups_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 5351020

test_friends_info()
test_groups_info()


# In[ ]:
