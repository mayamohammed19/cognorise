#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


df1=pd.read_csv("C:/Users/dell/Downloads/archive (8)/Unemployment in India.csv")
df2=pd.read_csv("C:/Users/dell/Downloads/archive (8)/Unemployment_Rate_upto_11_2020.csv")


# In[4]:


#load the dataset
df2.head()


# In[5]:


df2.describe()


# In[6]:


df2.info()


# In[32]:


#data cleaning and preprocessing
df2.isna().sum()


# In[8]:


# Print column names to identify any issues
print("Original Column Names:")
print(df2.columns)

# Remove any leading or trailing spaces from column names
df2.columns = df2.columns.str.strip()

# Print column names to confirm the changes
print("\nCleaned Column Names:")
print(df2.columns)


# In[14]:


#Verify the presence of the 'Date' column
if 'Date' in df2.columns:
    # Remove any leading or trailing spaces from the 'Date' column values
    df2['Date'] = df2['Date'].str.strip()

    # Convert 'Date' to datetime format
    df2['Date'] = pd.to_datetime(df2['Date'], format='%d-%m-%Y')

    # Display the data types to confirm the changes
    print("\nData types after conversion:")
    print(df2.dtypes)

    # Display the first few rows of the dataframe
    df2.head()
else:
    print("The 'Date' column was not found. Please check the dataset for any discrepancies.")


# In[39]:


# Adding Day, Month, and Year
df2['Date'] = pd.to_datetime(df1['Date'])
df2['Day'] = df1['Date'].dt.day
df2['Month'] = df1['Date'].dt.month_name()
df2['Year'] = df1['Date'].dt.year


# In[22]:


# Rename columns for easier reference
df2.rename(columns={
    'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'Labour_Participation_Rate',
    'Region.1': 'Region_Category'
}, inplace=True)

# Display the first few rows after preprocessing
df2.head()


# In[24]:


#statistical analysis
mean_unemployment = df2["Unemployment_Rate"].mean()
median_unemployment = df2["Unemployment_Rate"].median()
std_unemployment = df2["Unemployment_Rate"].std()


# In[26]:


#grouping data by Date  and unemployment rate
mean_unemployment_Rate_date=df2.groupby("Date")["Unemployment_Rate"].mean()
# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(mean_unemployment_Rate_date.index, mean_unemployment_Rate_date.values, marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Estimated Unemployment Rate (%)")
plt.title("Unemployment Rate Over Time")
plt.grid(True)

plt.show()



# In[27]:


# Calculate correlation matrix
correlation = df2[['Unemployment_Rate', 'Employed', 'Labour_Participation_Rate']].corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# In[29]:


# Unemployment Rate vs. Labour Participation Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Labour_Participation_Rate', y='Unemployment_Rate', data=df2)
plt.title('Unemployment Rate vs. Labour Participation Rate')
plt.xlabel('Labour Participation Rate (%)')
plt.ylabel('Unemployment Rate (%)')
plt.show()

# Calculate and display the correlation between these variables
correlation = df2['Labour_Participation_Rate'].corr(df2['Unemployment_Rate'])
print(f"Correlation between Labour Participation Rate and Unemployment Rate: {correlation:.2f}")


# In[30]:


# Unemployment Rate by Region
plt.figure(figsize=(12, 8))
sns.scatterplot(x='longitude', y='latitude', hue='Unemployment_Rate', size='Unemployment_Rate', data=df2, palette='viridis', sizes=(20, 200))
plt.title('Unemployment Rate by Region')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# In[ ]:




