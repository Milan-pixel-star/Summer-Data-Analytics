#!/usr/bin/env python
# coding: utf-8

# Map Funtion

# In[19]:


def add_elements(list1):
    total = sum(map(lambda x: x, list1))
    return total

list1 = [1, 23, 56, 89, 620, 156]
sum_of_elements = add_elements(list1)
print("The sum of the elements is:", sum_of_elements)


# In[21]:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = list(map(lambda fruit: fruit if "a" in fruit else None, fruits))
print(newlist)  


# In[22]:


x = [5,2,3,6]
newlist = list(map(lambda x: x*x,x))
print(newlist)  


# In[28]:


x = [5, 2, 3, 6]
newlist = list(map(lambda num: num if num % 2 == 0 else None, x))
print(newlist)  


# In[29]:


words = ["apple", "banana", "cherry"]
uppercase_words = list(map(str.upper, words))
print(uppercase_words)  


# Filter function

# In[30]:


words = ["basket", "banana", "cherry", "dog", "elephant"]
b_words = list(filter(lambda word: word[0] == 'b', words))
print(b_words)


# In[32]:


def is_positive(num):
    return num > 0

numbers = [1, -2, 3, -4, 5]
positive_numbers = list(filter(is_positive, numbers))

print(positive_numbers)  


# In[35]:


strings = ["apple", "", "banana", None, "cherry"]
non_empty_strings = list(filter(None, strings))  
print(non_empty_strings)


# Lambda function

# In[42]:


a= lambda x: x*x*x
print(a(6))


# In[45]:


echo_word = (lambda word1, echo: word1 * echo)
a=input("Enter a string : ")
b=int(input("Enter the number of times you want to echo : "))
result = echo_word(a,b)
print(result)


# In[47]:


string_length = lambda text: len(text)
text = input("Enter a string : ")
print(string_length(text))


# In[48]:


reverse_string = lambda text: text[::-1]
text = input("Enter a string : ")
print(reverse_string(text))


# In[50]:


is_vowel = lambda char: char.lower() in "aeiou"
character = input("Enter a character : ")
print(is_vowel(character))


# --------------------------------------------------------------------------------------------------------------------------------

# In[51]:


import numpy as np


# In[52]:


a=np.zeros(6)


# In[53]:


a


# In[54]:


a=np.ones(5)


# In[55]:


a


# In[56]:


a=np.eye(2)


# In[57]:


a


# In[59]:


a=np.zeros((2,2))
a


# In[60]:


a=np.ones((2,2))
a


# In[61]:


a=np.eye(2,2)
a


# In[63]:


a=np.ones((4,4))
a # symmetic matrix


# In[64]:


a=np.ones((3,4))
a # asymmetrin matrix


# In[66]:


a=np.eye(4,4)
a # diagonal matrix


# In[ ]:




