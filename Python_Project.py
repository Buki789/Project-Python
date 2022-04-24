#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


ss = pd.read_excel(r'C:\Users\bukif\Desktop\Sales-Analysis-master\Sales-Analysis-master\superstore.xlsx')


# In[3]:


ss.head()


# In[4]:


ss.shape


# In[5]:


ss.columns


# In[6]:


ss.info()


# In[7]:


ss.describe()


# In[8]:


ss.isnull().sum()


# # What is the overall sales trend?

# In[9]:


# Q1. What is the overall sales trend? 
# Q2. Which are the Top 10 products by sales?
# Q3. Which are the Most Selling Products?
# Q4. Which is the most preferred Ship Mode?
# Q5. Which are the Most Profitable Category and Sub-Category?


# In[10]:


ss['order_date'].min()


# In[11]:


ss['order_date'].max()


# In[13]:


ss['month_year'] = ss['order_date'].apply(lambda x: x.strftime('%Y-%m'))


# In[14]:


ss_trend = ss.groupby('month_year').sum()['sales'].reset_index()


# In[15]:


plt.figure(figsize=(15,6))
plt.plot(ss_trend['month_year'], ss_trend['sales'], color='purple')
plt.xticks(rotation='vertical',size=10)
plt.show()


# # Which are the Top 10 products by sales?

# In[16]:


prod_sales = pd.DataFrame(ss.groupby('product_name').sum()['sales'])


# In[17]:


prod_sales= prod_sales.sort_values('sales',ascending=False)


# In[18]:


prod_sales[:10]


# # Which are the Most Selling Products?

# In[19]:


most_sell_prod = pd.DataFrame(ss.groupby('product_name').sum()['quantity'])


# In[20]:


most_sell_prod= most_sell_prod.sort_values('quantity',ascending=False)


# In[21]:


most_sell_prod[:10]


# # Which is the most preferred Ship Mode?

# In[27]:


import seaborn as sns
sns.countplot(ss['ship_mode'])
plt.show()


# # Which are the Most Profitable Category and Sub-Category?

# In[28]:


cat_subcat_profit = pd.DataFrame(ss.groupby(['category','sub_category']).sum()['profit'])


# In[29]:


cat_subcat_profit.sort_values(['category','profit'],ascending=False)


# In[ ]:




