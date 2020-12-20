#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


elements = np.random.randn(5,5)


# In[3]:


elements


# In[4]:


elements + 3


# In[5]:


elements.shape


# In[6]:


elements.dtype


# In[9]:


anotherArray=[[12,23,34,54,64],[588, 688, 799, 800,900]]


# In[10]:


saveIn = np.array(anotherArray)


# In[11]:


saveIn


# In[12]:


saveIn.ndim


# In[13]:


saveIn.shape


# In[14]:


saveIn.dtype


# In[16]:


np.zeros(10)


# In[24]:


np.empty((2,3))


# In[35]:


a1 = [[6,6,6,66,6,6,6],[3,5,5,5,55,5,5]]


# In[36]:


np.asarray(a1)


# In[37]:


a2 = np.asarray(a1)


# In[38]:


len(np.asarray(a1))


# In[39]:


np.asarray(a1).astype(int)


# # arithmetic operations

# In[40]:


arr1 = [1,2,3,4]


# In[41]:


arr2 = [5,6,7,8]


# In[42]:


np.subtract(arr1,arr2)


# In[43]:


np.add(arr1,arr2)


# In[44]:


np.divide(arr1,arr2)


# In[45]:


np.multiply(arr1,arr2)


# In[47]:


np.exp(arr1)


# In[48]:


np.sqrt(arr2)


# In[49]:


np.sin(arr2)


# In[50]:


np.cos(arr2)


# In[51]:


np.log(arr1)


# In[52]:


np.log(arr2)


# # comparisons

# In[65]:


arr=np.array([0,1,2,3,4,5,6,7,8,9])


# In[67]:


arr[arr<6]


# In[68]:


arr[arr>1]


# In[69]:


#like others


# # aggregate functions

# In[72]:


arr5 = np.array([[3,3,3,3,4,4,5,8,4,5],[0,1,2,3,4,5,6,7,8,9]])


# In[73]:


arr5.sum()


# In[74]:


arr5.min()


# In[75]:


arr5.max(axis=1)


# In[76]:


arr5.cumsum(axis=0)


# In[78]:


arr5.mean()


# In[81]:


N = arr5.view()


# In[82]:


np.copy(arr5)


# In[83]:


N = arr5.copy()


# In[84]:


N


# In[90]:


H = np.array([9,8,7,6,5,4,3,2,1,0])


# In[92]:


H


# In[94]:


H.sort()


# In[96]:


H


# In[97]:


H.sort(axis=0)


# In[98]:


H


# # subsetting, slicin, indexing

# In[99]:


a=np.array([1,2,3])


# In[100]:


a[0]


# In[102]:


b=np.array([[1,2,3,4],[5,6,7,8]])


# In[103]:


b


# In[110]:


b[1,1]


# In[111]:


s=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[112]:


s[0:4]


# In[126]:


b=np.array([[1,2,3,4],[5,6,7,8]])


# In[128]:


b[1:2,2]


# In[129]:


wh=np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[130]:


np.where(wh<5,'l',wh)


# In[131]:


b=np.array([[1,2,3,4],[5,6,7,8]])


# In[136]:


b.transpose((1,0))


# In[137]:


b.all()


# In[138]:


b.any()


# In[139]:


b.sum()


# In[141]:


b.flatten()


# In[153]:


b.ravel()


# In[155]:


a=[[1,2,3,4,5],[3,34,3,34,3]]


# In[156]:


b=[[1,2,3,4,5],[3,34,3,34,3]]


# In[159]:


arr8=np.array(a)


# In[160]:


arr9= np.array(b)


# In[161]:


np.vstack((arr8,arr9))


# In[162]:


np.hstack((arr8,arr9))


# In[ ]:




