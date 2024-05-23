#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


df=pd.read_csv('Downloads/Zomatodataset/zomato.csv', encoding='latin-1')
# df=pd.read_csv('Downloads/Zomatodataset/zomato.csv', encoding='cp437')


# In[14]:


df.head()


# In[15]:


df.columns


# In[17]:


df.info()


# In[18]:


df.describe()


# In[23]:


# # In Data Analysis what all things we do first:-
# 1.Missing values
# 2.Explore about numerical variables
# 3.Explore about categorical variables
# 4.Finding relationship between features(means diffrent columns)


# In[25]:


df.isnull().sum()


# In[31]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[89]:


sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

df.shape


# In[40]:


df_country=pd.read_excel('Downloads/Zomatodataset/Country-Code.xlsx')
df_country.head()


# In[42]:


final_df = pd.merge(df, df_country, on='Country Code', how='left')


# In[43]:


final_df.head(2)


# In[44]:


final_df.dtypes


# In[45]:


final_df.Country.value_counts()


# In[47]:


country_names=final_df.Country.value_counts().index


# In[49]:


country_val=final_df.Country.value_counts().values


# In[88]:


plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# # Observation:- Zomato maximum record or transaction are from India

# In[52]:


final_df.columns


# In[78]:


ratings=final_df.groupby(['Aggregate rating','Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating_Count'})


# In[79]:


ratings


# ## Observation 
# 1.When Rating is between 4.5 to 4.9____>Excellent
# 
# 2.When Rating is between 4.0 to 4.4____>very good
# 
# 3.When Rating is between 3.5 to 3.9____>good
# 
# 4.When Rating is between 3.0 to 3.4____>average
# 
# 5.When Rating is between 2.5 to 2.9____>average
# 
# 6.When Rating is between 2.0 to 2.4____>poor

# In[81]:


ratings.head()


# In[97]:


# plt.figure(figsize=(12, 6))
import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6) 
sns.barplot(x="Aggregate rating",y="Rating_Count",hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# Observation:
# 
# 1.Not rated count is high
# 
# 2.Maximum ratings are between 2.5 to 3.4
# 

# In[98]:


# In countplot we use it for ploting w.r.t categorical variables.
sns.countplot(x='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[107]:


# Find the countries names who have given a zero rating
final_df['Country'][final_df['Aggregate rating']==0].unique()


# In[111]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# # Observations :- Max. no. of zero ratings are from indian customers

# In[122]:


# find out which currency is used by which country?

final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[126]:


# Which countries have online deliveries option
final_df.columns


# In[148]:


final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# In[ ]:


final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()


# Observations:
# 1. Online deliveries are available in india and UAE

# In[ ]:


# Create a pie chart for cities distribution


# In[163]:


city_labels=final_df.City.value_counts().index


# In[161]:


city_values=final_df.City.value_counts().values


# In[176]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.3f%%')


# ## Assignment
# Find the top 10 cusines

# In[178]:


final_df.columns


# In[193]:


final_df.groupby(['Cuisines']).size().max()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




