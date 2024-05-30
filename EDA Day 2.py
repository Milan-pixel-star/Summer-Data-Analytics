#!/usr/bin/env python
# coding: utf-8

# 4. diag --> this function creates a two dimensional array with all the diagonal
# element as the given value and rest ar ezero

# In[2]:


import numpy as np
a=np.diag([1,8,4,9])
a


# 5) randit --> This function is used to generate a random number between a given range
# 
# Syntax --> randint(min_value,max_value,total_numbers)

# In[7]:


import numpy as np
a=np.random.randint(1,10,3)
a


# 6) rand() --> This function is used to generate a random number between 0 and 1

# In[9]:


import numpy as np
a=np.random.rand(5)
a


# 7) randn --> This is function used to generate a random no from -3 to close 3. This may return 
# positive as well as negative numbers

# In[10]:


a=np.random.randn(5)
a


# Reshaping data

# In[13]:


a=np.random.randint(1,50,12)
a


# In[14]:


a.shape


# In[15]:


a=a.reshape(2,6)
a


# In[16]:


a=a.reshape(6,2)
a


# In[17]:


a=a.reshape(12,1)
a


# In[18]:


a=np.random.randint(1,100,32)
a


# In[19]:


a.shape


# In[20]:


a=a.reshape(32,1)
a


# In[21]:


a=a.reshape(16,2)
a


# In[22]:


a=a.reshape(4,8)


# In[23]:


a


# principal of -1

# seed function() --> we know that randint function generate random numbers.
# Every time we run the program, now set of a random number is generated. So,
# solve problem we will use seed function.

# In[25]:


np.random.seed(12)
a=np.random.randint(1,100,10)
a


# In[26]:


np.random.seed(11)
a=np.random.randint(1,500,30)
print(a)
a.reshape(6,5)


# view as copy --> when we slice a sub_array from an array,it may be done by two ways 

# In[27]:


b=a[3:6]
b[:]=0
print("a : ", a)
print("b : ", b)


# In[29]:


b=a[3:6].copy()
b[:]=0
print("a : ", a)
print("b : ", b)


# conditional statement

# In[32]:


a=np.array([10,20,30,40,50,60,70,80,90])


# In[34]:


a=np.arange(1,16)
a


# In[35]:


a>10


# In[36]:


a<10


# In[37]:


b=a>10
a[b]


# In[38]:


a[a%2==0]


# In[40]:


a=np.arange(1,5)
a*2


# In[41]:


a+2


# In[42]:


a**2


# In[43]:


a=np.array([1,2,3,4]).reshape(2,2)
a


# In[45]:


b=np.array([5,6,7,8]).reshape(2,2)
b


# In[46]:


a+b


# In[47]:


a*b


# In[48]:


a-b


# In[49]:


b-a


# In[50]:


b/a


# In[51]:


a*b


# In[52]:


a.dot(b)


# In[ ]:




