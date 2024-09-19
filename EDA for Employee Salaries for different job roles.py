#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo 
import plotly.figure_factory as ff
import plotly.io as pio
from wordcloud import WordCloud
color_pal = sns.color_palette()
plt.style.use('seaborn-dark-palette')
plt.style.use('dark_background')

import nltk
import re
import warnings
warnings.filterwarnings('ignore')
sns.set_theme(style='darkgrid', palette='colorblind')
from sklearn.preprocessing import LabelEncoder 
le = LabelEncoder()


# In[37]:


data =pd.read_csv("C:/Users/dell/Downloads/archive (7)/ds_salaries.csv")


# In[38]:


data.head()


# In[39]:


data.info()


# In[40]:


data.shape


# In[41]:


data.describe()


# In[42]:


cols=data.columns
cols


# In[43]:


uniqueValues=data.nunique()
uniqueValues


# In[44]:


#checking Null values
data.isna().sum()


# In[45]:


# Finding duplicate rows
duplicate_rows = data[data.duplicated(keep='first')]

# Number of duplicate rows
num_duplicates = duplicate_rows.shape[0]

# Displaying the duplicate rows
print(f"Number of duplicate rows: {num_duplicates}")
duplicate_rows


# In[59]:


#dealing with categorical values 
# Select columns with object (categorical) data types
num_cols = data.select_dtypes(include='object').columns.tolist()

# Initialize the LabelEncoder
le = LabelEncoder()

# Apply Label Encoding to the selected numerical columns
for x in num_cols:  
    data[x] = le.fit_transform(data[x])

# Now, your categorical columns (excluding column 0) have been converted to numerical values
data.head()


# In[60]:


Corr_Matrix = data.corr()

# Set up the figure and plot the heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(Corr_Matrix, annot=True, cmap='coolwarm', center=0)
plt.show()


# In[61]:


print('Top 5 Most Positively Correlated to the To salary_in_usd')
Corr_Matrix['salary_in_usd'].sort_values(ascending=False).head(5)


# In[62]:


print('Top 5 Most Negatively Correlated to salary_in_usd ')
Corr_Matrix['salary_in_usd'].sort_values(ascending=True).head(5)


# In[63]:


get_ipython().system('pip install ydata-profiling #visualization ')


# In[64]:


# Import the ProfileReport class from the ydata_profiling library
from ydata_profiling import ProfileReport

# Create a comprehensive profile report for the DataFrame 'data'
# This report will contain various statistics, insights, and visualizations about the data
profile = ProfileReport(data)


# In[65]:


pip install matplotlib


# In[66]:


profile.to_notebook_iframe() # use this line to show the output


# In[67]:


#vizualisations

plt.figure(figsize=(12, 6))
sns.barplot(x='experience_level', y='salary', data=data)
plt.title('Salary Distribution Across Experience Levels')
plt.xlabel('Experience Level')
plt.ylabel('Salary')
plt.show()


# In[68]:


plt.figure(figsize=(12, 6))
sns.barplot(x='employment_type', y='salary', data=data)
plt.title('Salary Distribution Across Employment Types')
plt.xlabel('Employment Type')
plt.ylabel('Salary')
plt.show()


# In[69]:


plt.figure(figsize=(10, 6))
sns.barplot(x='company_size', y='salary', data=data)
plt.title('Impact of Company Size on Salary')
plt.xlabel('Company Size')
plt.ylabel('Salary')
plt.show()


# In[70]:


sns.catplot(x='employment_type' , data=data , hue='experience_level', col='company_size' ,palette='ch:.25', kind='count')
#in the large company most of workers are intermediate and senior level
#in medium company the most of workers are senior level
#in small company most of workers are mid level and junior level


# In[77]:


data.groupby("experience_level")["salary_in_usd"].sum().plot(kind = 'pie' ,autopct='%1.1f%%')
#highest salaries goes to senior level records experts


# In[78]:


data['experience_level'].value_counts()
#highest records was for seniorlevel expert


# In[80]:


data.groupby("work_year")["salary_in_usd"].max().sort_values(ascending=False).plot.bar()
#highest salaries have been taken in 2021 


# In[ ]:




