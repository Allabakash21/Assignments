#!/usr/bin/env python
# coding: utf-8

# In[5]:


def mean_value(given_list):
    total = sum(given_list)
    average_value = total/len(given_list)
    return average_value


# In[7]:


l =[1,2,3,4,5,6,7,8,9,10]
mean_value(l)


# In[33]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)
    if l%2 == 0:
        median = (num_list[int(l/2)] + num_list[int(l/2)-1])/2
    else:
        median = (num_list[int(l/2)])
    return median


# In[35]:


median_value(1,2,3,4,5,6,7,8,9,10)


# In[ ]:





# In[ ]:




