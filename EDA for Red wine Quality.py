#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as ex
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=pd.read_csv("C:/Users/dell/Downloads/archive (9)/winequality-red.csv")


# In[3]:


df.head(10)


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df["quality"].value_counts()


# In[8]:


df["pH"].values


# In[9]:


#cleaning data
#missing values
df.isnull().sum()


# In[10]:


#data redundancy
# Check for duplicates across all columns
duplicated = df.duplicated()

# Print the number of duplicated instances
print("Number of duplicated instances:", duplicated.sum())

# Print the duplicated instances
df[duplicated]


# In[11]:


df = df.drop_duplicates()


# In[12]:


# Make sure there is no more duplicates.
duplicated = df.duplicated()

print("Number of duplicated instances:", duplicated.sum())
df[duplicated]


# In[13]:


#checking wine quality (>7 ==1 ) else (==0)
df["quality"] = np.where(df["quality"] >= 7, 1, 0)
df['quality'].value_counts()


# In[14]:


corr = df.corr()
sns.heatmap(corr, cmap="coolwarm");


# In[15]:


# Alcohol vs wine quality
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
ax = sns.barplot(x="quality", y="alcohol", data=df)
plt.title("Most Positive Relationship", fontsize=16)
ax.set_xlabel("quality", fontsize=12)
ax.set_ylabel("alcohol", fontsize=12)
plt.tight_layout()
plt.show()


# In[16]:


# acidity vs wine quality
plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
ax = sns.barplot(x="quality", y="volatile acidity", data=df)
plt.title("Most Negative Relationship", fontsize=16)
ax.set_xlabel("quality", fontsize=12)
ax.set_ylabel("volatile acidity", fontsize=12)
plt.tight_layout()
plt.show()


# In[21]:


# Create a 4x3 grid of subplots
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(20, 20))

# Modify the color list to match the number of columns in your dataset
colors = ['#491D8B', '#6929C4', '#8A3FFC', '#A56EFF',
          '#7D3AC1', '#AF4BCE', '#DB4CB2', '#EB548C',
          '#EC96E0', '#A2128E', '#E8D9F3', '#641811']

# Loop through each column in your wine_df dataset
for index, column in enumerate(df.columns):
    if index < 12:  # Limit the iteration to the number of subplots
        ax = axes.flatten()[index]
        ax.hist(df[column], color=colors[index], label=column)
        ax.legend(loc="best")

plt.suptitle("Histograms", size=20)
plt.tight_layout()
plt.show()


# In[ ]:




