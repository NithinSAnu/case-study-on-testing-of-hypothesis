#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from scipy.stats import ttest_rel, chi2_contingency


# In[6]:


df = pd.read_csv("C:/Users/ACER/Downloads/Sales_add.csv")


# In[7]:


df['Increase_in_Sales'] = df['Sales_After_digital_add(in $)'] - df['Sales_before_digital_add(in $)']

t_statistic, p_value = ttest_rel(df['Sales_After_digital_add(in $)'], df['Sales_before_digital_add(in $)'])


# In[8]:


print("Hypothesis Testing - Increase in Sales:")
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
if p_value < 0.05:
    print("There is a significant increase in sales after the digital marketing campaign.")
else:
    print("There is no significant increase in sales after the digital marketing campaign.")


# In[9]:


dependency_table = pd.crosstab(df['Region'], df['Manager'])
chi2_stat, p_value, _, _ = chi2_contingency(dependency_table)


# In[10]:


print("\nHypothesis Testing - Dependency between Region and Manager:")
print(f"Chi-square statistic: {chi2_stat}")
print(f"P-value: {p_value}")
if p_value < 0.05:
    print("There is a significant dependency between Region and Manager.")
else:
    print("There is no significant dependency between Region and Manager.")


# In[ ]:




