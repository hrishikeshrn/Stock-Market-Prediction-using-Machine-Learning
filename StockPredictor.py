
# coding: utf-8

# In[76]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[77]:


data = pd.read_csv('GOOGL_2006-01-01_to_2018-01-01.csv')


# In[ ]:





# In[ ]:





# In[78]:


data.head()


# In[79]:


data = data.drop('Name',axis=1)


# In[80]:


data.head()


# In[81]:


data1 = data


# In[82]:


type(data1)


# In[83]:


data.index


# In[111]:


X_1 = data.drop('Close',axis=1)


# In[112]:


Y_1 = data['Close']


# In[113]:


from sklearn.model_selection import train_test_split


# In[115]:


X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X_1, Y_1, test_size=0.33, random_state=42)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[84]:


abc=[]
for i in range(len(data)):
    abc.append(data['Date'][i].split('-'))
    data['Date'][i] = ''.join(abc[i])


# In[85]:


data['Date'].tail()


# In[86]:


X = data.drop('Close',axis=1)


# In[87]:


X.head()


# In[88]:


y = data['Close']


# In[89]:


y.head()


# In[90]:


y.index


# In[91]:


from sklearn.model_selection import train_test_split


# In[92]:


X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.33, random_state=42)


# In[93]:


from sklearn.ensemble import RandomForestRegressor


# In[94]:


rfg = RandomForestRegressor()


# In[95]:


type(data['Date'][1])


# In[ ]:





# In[96]:


data['Date'].head()


# In[ ]:





# In[ ]:





# In[97]:


rfg.fit(X_train,y_train)


# In[98]:


y_pred = rfg.predict(X_test)


# In[99]:


y_pred[1]


# In[100]:


y_test[1]


# In[101]:


from sklearn.neural_network import MLPRegressor


# In[102]:


mlp = MLPRegressor()


# In[103]:


mlp.fit(X_train,y_train)


# In[104]:


y_test[1] - y_pred[1]


# In[105]:


y_pred_1 = mlp.predict(X_test)


# In[ ]:





# In[106]:


y_test[1] -y_pred_1[1]


# In[131]:


y_test[2] == y_test_1[2]


# In[132]:



x_test_2['Date'] = pd.to_datetime(data1.Date,format='%Y-%m-%d')
x_test_2.index = x_test_2['Date']

plt.figure(figsize=(16,8))
plt.plot(y_test,'-r',label='Close Price History')


# In[127]:


x_test_2['Date'] = pd.to_datetime(data1.Date,format='%Y-%m-%d')
x_test_2.index = x_test_2['Date']

plt.figure(figsize=(16,8))
plt.plot(y_pred,'-b',label='Close Price History')


# In[128]:


x_test_2['Date'] = pd.to_datetime(data1.Date,format='%Y-%m-%d')
x_test_2.index = x_test_2['Date']

plt.figure(figsize=(16,8))
plt.plot(y_pred_1,'-g',label='Close Price History')


# In[51]:





# In[61]:





# In[ ]:




