
# coding: utf-8

# Pandas Learning

# In[1]:

import pandas as pd


# In[2]:

ice_cream = ["choclote","vanilla","strawberry","kulfi"]
pd.Series(ice_cream)


# In[3]:

lottery= [4,6,7,4,5,7]
pd.Series(lottery)


# In[4]:

game=[True,False,True]
pd.Series(game)


# In[6]:

Dreamteam = {'Kohli':92,'Kuldeep':40,'Buvi':60}
pd.Series(Dreamteam)


# To know about  methods in a modules..help(pd) and dir(pd)

# In[12]:

dir(pd)


# In[18]:

cricketrs= ["Sachin","Sehwaag","Dravid","Kohli"]
cric = pd.Series(cricketrs)
cric


# Attributes

# In[20]:

cric.all


# In[21]:

cric.index


# In[22]:

cric.dtype


# In[23]:

prices =[3.5,6.7,8.3]
p=pd.Series(prices)
p


# In[24]:

p.sum()


# In[25]:

p.mean()


# In[26]:

p.mode()


# Parameter and Arguements

# In[27]:

fruits = ["Apple","orange","grapes","mangos","Bananas"]
weekdys =["monday","Tuesday","wednesday","Trusday","Friday"]
pd.Series()#parameters ---shift + tab
#Arguments --values  (data =none, index = none) --parameters are data and index --arguments are corresponding values 


# In[39]:

fruits = ["Apple","orange","grapes","mangos","Bananas"]
weekdays =["monday","Tuesday","wednesday","Trusday","Friday"]
pd.Series(fruits,weekdays )


# In[40]:

fruits = ["Apple","orange","grapes","mangos","Bananas"]
weekdays =["monday","Tuesday","wednesday","Trusday","Friday"]
pd.Series(index = fruits,data = weekdays )


# In[42]:

fruits = ["Apple","orange","grapes","mangos","Bananas"]
weekdays =["monday","Tuesday","wednesday","Trusday","Friday"]
pd.Series(index = fruits,weekdays )


# In[ ]:



