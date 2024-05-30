#!/usr/bin/env python
# coding: utf-8

# Q1 Write satement to import numpy?

# In[1]:


import numpy as np


# Q2 Create an array using numpy?

# In[2]:


a=np.array([10,20,30,40,50,60])
a


# Q3 Create an arrray of 10 random integers?

# In[4]:


a=np.random.randint(1,50,10)
a


# Q4 Create an array of elements from 10-20?

# In[7]:


a=np.random.randint(10,20,5)
a


# Q5 create an array which contains value 5, 10 times?

# In[9]:


a=np.repeat(5,10)
a


# Q6 Create a one dimensional array and convert it into 3*3 matrix?

# In[15]:


np.random.seed(9)
a=np.random.randint(1,100,9)
a.reshape(3,3)


# Q7 Create a 2D array and convert it into 3*3 matrix and number should be between 0 and 1?

# In[28]:


a=np.diag(np.random.rand(3))
a


# Q8 Concatenate 2D array horizontally and vertically?

# In[31]:


a=np.array([10,20,30])
b=np.array([96,98,63])
ans=np.vstack((a,b))
ans


# In[32]:


a=np.array([10,20,30])
b=np.array([96,98,63])
ans=np.hstack((a,b))
ans


# In[ ]:




