#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Homework 2 :  Functions


# defining the song name
song_name = "Lonely"

#Artist name
def Artist():
    Artist = "Akon"
    return Artist

#Released_Year
def Released_Year():
    Released_Year = 2005
    return Released_Year

#Genre
def Genre():
    Genre = "hip hop soul"
    return Genre


# In[2]:


# checks if the song name is listed or not
def is_song_listed(name):
    if name == song_name:
        return True
    else:
        return False


# In[ ]:




