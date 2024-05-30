#!/usr/bin/env python
# coding: utf-8

# ## Pandas --> It is an open source liberary that is used to handle data manipulation

# Data Structures : 
#     1) Series
#     2) Data Frame

# In[1]:


import pandas as pd


# In[2]:


a=pd.Series([1,23,67,90])
a


# In[3]:


type(a)


# ## DataFrame

# In[4]:


a={
    "Emp_id":[1,2,3,4,5,6,7,8],
    "Name":["Sam","Mohit","Gaurav","Aniket","Raj","Rahul","Deepak","Kunal"],
    "Departement":["IT","HR","HR","IT","Operations","IT","Operations","HR"],
    "Working_Hours":[8,9,9,9,9,9,6,7]
}
a


# In[5]:


type(a)


# In[6]:


df=pd.DataFrame(a)
df


# In[7]:


df.columns


# In[8]:


df.head() #it returns top 5 rows


# In[9]:


df.tail()  # it returns bottom 5 rows


# In[10]:


df.tail(2)


# In[11]:


df.head(3)


# In[12]:


df.sample(4)  # it returns random index row 


# In[13]:


df.describe()  # it returns statical view of data


# In[14]:


df.info() # complete overview of data


# ## How to read a CSV file

# In[26]:


df=pd.read_csv("F:\\New folder\\ML\\CSV files\\covid_toy.csv")


# In[27]:


df


# In[28]:


df.head()


# In[29]:


df['gender'].value_counts()


# df.loc["row range","Column Range"]
# df.iloc["row range", "Column Range"]

# In[31]:


df.loc[2]


# In[33]:


df.loc[2,"gender"]


# In[34]:


df.loc[2:5,"age"]


# In[36]:


df.loc[2:5,["age","gender"]]


# In[38]:


df.iloc[2:5,[1,2]]


# In[39]:


df.iloc[2]


# In[40]:


df.iloc[2:5,[1,3]]


# In[41]:


df.iloc[1:5,2:3]


# In[42]:


df.isnull()  # returns true if not null else false


# In[43]:


df.isnull().sum()  # counts the total no. of null values in each column 


# In[44]:


df=df.dropna()


# In[45]:


df


# In[46]:


df.isnull().sum()


# In[ ]:




