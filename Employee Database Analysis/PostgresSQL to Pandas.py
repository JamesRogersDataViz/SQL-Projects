#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


from sqlalchemy import create_engine


# In[3]:


engine = create_engine('postgres://postgres:Postg####@localhost:5###/SQLHW')


# In[4]:


connection = engine.connect()


# In[18]:


#result_set = connection.execute("SELECT * FROM salaries")
#print(result_set)
#for r in result_set:
#    print(r)


# In[6]:


salaries = pd.read_sql("SELECT * FROM salaries", connection)
salaries.head()


# In[7]:


titles = pd.read_sql("SELECT * FROM titles", connection)
titles.head()


# In[8]:


employees_title_salary = pd.read_sql("SELECT e.emp_no, t.title, s.salary                          FROM employees e                          RIGHT JOIN titles t                         ON (e.emp_no = t.emp_no)                         RIGHT JOIN salaries s                         ON (t.emp_no = s.emp_no)", connection)
employees_title_salary.head()


# In[13]:


avg_salary_per_title = pd.DataFrame(employees_title_salary.groupby(["title"]).mean()["salary"]).reset_index()


# In[17]:


plt.bar(np.arange(len(avg_salary_per_title)), avg_salary_per_title.salary, align = "center")
plt.xticks([lable for lable in np.arange(len(avg_salary_each_title))], avg_salary_each_title["title"],
           rotation = 75)
plt.title("Average Salary Per Title")
plt.xlabel("Titles")
plt.ylabel("Average Salaries")


# In[11]:


employees_title_salary.loc[employees_title_salary["emp_no"] == 499942]


# In[ ]:




