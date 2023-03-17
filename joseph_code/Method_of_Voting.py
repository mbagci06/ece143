#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import os 


# In[2]:


survey_data=pd.read_csv('../survey/survey_nonvote.txt').fillna(method='ffill')
census_data_table_14_a=pd.read_excel('../US_census/table14.xlsx',skiprows=4,skipfooter= 58,header=[0, 1],index_col=[0,1]).fillna(method='ffill')


# In[3]:


census_data_table_14_a.name='Table 14.  Method of Voting, By Selected Characteristics'
census_data_table_14_a.tail()
Update_col_names=[]
for col in census_data_table_14_a.columns:
    Update_col_names.append(' '.join(col))
Update_index_names=[]
for ind in census_data_table_14_a.index:
    Update_index_names.append(' '.join(ind))
index_dic={map(Update_index_names,census_data_table_14_a.index)}
b=census_data_table_14_a.values[:,:]
census_data_table_14_a=pd.DataFrame(b,columns=Update_col_names,index=Update_index_names)
census_data_table_14_a.head()


# In[4]:


survey_table=census_data_table_14_a


# In[5]:


in_person_on=survey_table.iat[0,1]
in_person_before=survey_table.iat[0,2]
by_mail=survey_table.iat[0,3]
not_sure=survey_table.iat[0,4]


# In[6]:


y=np.array([in_person_on,in_person_before,by_mail,not_sure])
mylabels=["In-person on election day","In-person before election day","By mail","Refuse to answer"]
mycolors=plt.get_cmap('inferno')(np.linspace(0.3, 0.7, len(y)))


# In[7]:


pie=plt.pie(y,labels=mylabels,colors=mycolors,autopct='%1.1f%%')
plt.legend(pie[0],mylabels, bbox_to_anchor=(1,-0.1), loc="lower right", fontsize=10, 
           bbox_transform=plt.gcf().transFigure)
plt.title("Percent distribution of methods of voting in 2020")
plt.show()


# In[8]:


Q24=survey_data.pivot_table(index = ['Q24'], aggfunc ='size')
Q24


# In[9]:


totalnum=2328+1217+2091+127
survey_mail=2328/totalnum
survey_ip_before=1217/totalnum
survey_in_on=2091/totalnum
survey_not=127/totalnum


# In[10]:


x=np.array([survey_in_on,survey_ip_before,survey_mail,survey_not])
mlabels=["In-person on election day","In-person before election day","By mail","Not sure"]

plt.pie(x,labels=mlabels,colors=mycolors,autopct='%1.1f%%')

plt.title("Non-voters'preferred way of voting")
plt.show()


# In[ ]:





# In[ ]:




