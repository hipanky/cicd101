#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sqlite3


# In[13]:


# Extract
df = pd.read_csv('data/data101.csv')

# Transform
df['age'] = df['age'].fillna(0)
df['salary'] = df['salary'] * 1.1

# Load
# conn = sqlite3.connect('test.db')
# df.to_sql('users', conn, if_exists='replace', index=False)

print("ETL Completed")



# In[9]:


df


# In[6]:


# Load
conn = sqlite3.connect('test.db')
df.to_sql('users', conn, if_exists='replace', index=False)


# In[10]:


res = pd.read_sql('Select * from users',con=conn)


# In[12]:


res


# In[ ]:




