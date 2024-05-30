#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df=pd.read_csv("F:\\New folder\\ML\\CSV files\covid_toy.csv")
df


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df.shape


# In[7]:


df=df.dropna()


# In[8]:


df.shape


# In[9]:


df.describe()


# In[10]:


df.head(10)


# In[11]:


df.loc[2]


# In[12]:


covid=df[df["has_covid"]=="Yes"]
covid.count()


# In[13]:


covid_male=df[(df["has_covid"]=="Yes")& (df["gender"]=="Male")]
covid_male


# In[14]:


covid_female=df[(df["has_covid"]=="Yes")& (df["gender"]=="Female")]
covid_female


# In[15]:


covid_female.count()


# In[16]:


covid_male.count()


# In[17]:


covid_group=df.groupby(["city","has_covid","gender","cough"])
covid_group.city.count()


# In[18]:


covid_cough=df.groupby("cough")
covid_cough.cough.count()


# In[19]:


df2=pd.read_csv("F:\\New folder\\ML\\CSV files\\placement.csv")
df2


# In[20]:


df2.describe()


# In[21]:


df2=df2.groupby("placed")
df2.placed.count()


# In[30]:


df2=pd.read_csv("F:\\New folder\\ML\\CSV files\\insurance.csv")
df2


# In[39]:


df2.head()


# In[37]:


df2.tail()


# In[44]:


df2.info()


# In[41]:


df2.describe()


# In[42]:


df2.isnull().sum()


# In[43]:


df2.shape


# In[45]:


df.columns


# In[48]:


df2['children'].value_counts() 


# In[49]:


df2['region'].value_counts() 


# In[52]:


df2.sort_values("children")


# In[56]:


child=df2[(df2["children"]==5)& (df2["sex"]=="male")]
child


# In[57]:


child=df2[(df2["children"]==5)& (df2["sex"]=="male") & (df2["age"]>30)]
child


# In[59]:


child["charges"].sum()


# In[60]:


child_female=df2[(df2["children"]==5)& (df2["sex"]=="female") & (df2["age"]>30)]
child_female


# In[61]:


child_female["charges"].sum()


# In[62]:


df2['smoker'].value_counts() 


# In[63]:


df3=pd.read_csv("F:\\New folder\\ML\\CSV files\\placement.csv")
df3


# In[66]:


df3.shape


# In[67]:


df3.head()


# In[68]:


df3.tail()


# In[69]:


df3.info()


# In[70]:


df3.describe()


# In[71]:


df3["placed"].value_counts()


# In[75]:


df4=df3.astype(int)


# In[76]:


df4


# In[79]:


good_student=df4[(df4["placed"]==1)& (df4["cgpa"]>=8) & (df4["resume_score"]>=8)]
good_student


# In[81]:


df4.max()


# In[82]:


df4.min()


# In[84]:


df4.median()


# In[85]:


df.mean()


# In[87]:


df4.filter(items=["cgpa","resume_score"])


# In[89]:


df4['half']=df4['cgpa'].where(df4['cgpa']>5.00, other=0)
df4.head(10)


# In[ ]:




