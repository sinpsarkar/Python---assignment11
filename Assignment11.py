#!/usr/bin/env python
# coding: utf-8

# It happens all the time: someone gives you data containing malformed strings, Python,
# lists and missing data. How do you tidy it up so you can get on with the analysis?
# Take this monstrosity as the DataFrame to use in the following puzzles:
# 
# df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
# 'Budapest_PaRis', 'Brussels_londOn'],
# 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
# 'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
# 'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
# '12. Air France', '"Swiss Air"']})
# 
# 

# In[66]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[4]:


df


# 1. Some values in the the FlightNumber column are missing. These numbers are meant
# to increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in
# these missing numbers and make the column an integer column (instead of a float
# column).

# In[67]:


Flight_Number = []      #Create empty list

for i in df['FlightNumber']:
    if np.isnan(i):
        i = prev_i+10
    prev_i = i
    Flight_Number.append(int(i))
    
df['FlightNumber']= Flight_Number


# In[10]:


print(df)


# 2. The From_To column would be better as two separate columns! Split each string on
# the underscore delimiter _ to give a new temporary DataFrame with the correct values.
# Assign the correct column names to this temporary DataFrame.

# In[32]:


temp_df=pd.DataFrame({'From': [x.split('_', 1)[0] for x in df['From_To'].values],
                      'To':[x.split('_', 1)[1] for x in df['From_To'].values]})


# In[33]:


temp_df


# 3. Notice how the capitalisation of the city names is all mixed up in this temporary
# DataFrame. Standardise the strings so that only the first letter is uppercase (e.g.
# "londON" should become "London".)

# In[35]:


temp_df['From'] = [x.capitalize() for x in df['From'].values]
temp_df['To'] = [x.capitalize() for x in df['To'].values]


# In[55]:


temp_df


# 4. Delete the From_To column from df and attach the temporary DataFrame from the
# previous questions.

# In[68]:


pd.DataFrame(df.drop(['From_To'], axis=1, inplace=True))
df=pd.concat([df,temp_df], axis=1,join='inner')


# In[64]:


df


# 5. In the RecentDelays column, the values have been entered into the DataFrame as a
# list. We would like each first value in its own column, each second value in its own
# column, and so on. If there isn't an Nth value, the value should be NaN.
# Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
# delay_2, etc. and replace the unwanted RecentDelays column in df with delays.

# In[71]:


delays = df['RecentDelays'].apply(pd.Series)
delays = delays.rename(columns = lambda x : 'delay_' + str(x+1))
delays


# In[72]:


df=df.drop('RecentDelays', axis=1).join(delays)
df

