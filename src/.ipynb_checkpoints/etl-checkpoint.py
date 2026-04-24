#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import sqlite3


# In[8]:


# Extract
df = pd.read_csv('data/data101.csv')

# Transform
df['age'] = df['age'].fillna(0)
df['salary'] = df['salary'] * 1.1

# Load
# conn = sqlite3.connect('test.db')
# df.to_sql('users', conn, if_exists='replace', index=False)

print("You  are inside Github Actions ETL Completed have fun inside ETL Using Github Action")









