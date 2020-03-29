#!/usr/bin/env python
# coding: utf-8

# In[1]:


# download the CSV datafile for a state. Now, try to import that data into Python.

import os
print(os.getcwd())


# In[9]:


import pandas as pd
df = pd.read_csv("all_040_in_01.P1.csv")
#df.head
df
df.to_csv(index=False)


# In[8]:


# Can you export the dataframe created by the code in Listing 2-8 to CSV?

import pandas as pd 
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0] 
phddegrees = [0,1,0,0,0] 
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees) 
columns = ['Names','Grades','BS','MS','PhD'] 
df = pd.DataFrame(data = Degrees, columns=['Names','Grades','BS','MS','PhD']) 
df
df.to_csv(index=False)


# In[10]:


import pandas as pd
df = pd.read_csv("all_040_in_01.P1.csv")
#data.head
df
df.to_csv(index=False)


# In[ ]:




