#!/usr/bin/env python
# coding: utf-8

# ### string function-in built functions

# In[3]:


str="Nikhitha"
print(str.upper())
print(str.lower())


# In[4]:


s='python is easy programming to learn and interesting'
s1="python"
print(s.islower())
print(s1.islower())


# In[7]:


s="Application"
s1='NIKHITHA'
print(s.isupper())
print(s1.isupper())


# In[8]:


s="5678"
s1="App1889"
print(s.isnumeric())
print(s1.isnumeric())


# In[11]:


s="Application"
s1="App1889"
print(s.isalpha())
print(s1.isalpha())


# In[15]:


s="python programming"
s1="python Programming"
print(s.istitle())
print(s1.istitle())


# In[16]:


s="python"
s1="python Programming"
print(s.isspace())
print(s1.isspace())


# In[17]:


str="python"
print(" ".join(str))


# In[18]:


print(",".join(["python","programming","easy"]))


# In[19]:


lst=["",""]
print(",".join(lst))


# In[20]:


s="python"
s1=" "
print(s.isspace())
print(s1.isspace())


# In[25]:


s="python,programming,is,easy,to,learn"
print(s.split())
print(s.split("a"))
print(s.split(","))


# In[26]:


s="Nikhitha"
print(s.split())


# In[29]:


s="python programming is easy to learn"
lst=s.split()
print(lst)
print(lst.index("is"))


# In[30]:


s="python programming is easy to learn"
lst=list(s)
print(lst)


# In[31]:


s="python programming"
print(s.replace("gra","application"))


# In[ ]:




