
# coding: utf-8

# In[3]:

import pandas as pd 
import numpy as np


# In[37]:

data98 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/1998.csv') 
data99 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/1999.csv') 
data00 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2000.csv') 
data01 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2001.csv') 
data02 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2002.csv') 
data03 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2003.csv') 
data04 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2004.csv') 
data05 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2005.csv') 
data06 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2006.csv')
data07 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2007.csv')
data08 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2008.csv')
data09 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2009.csv')
data10 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2008.csv')
data11 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2008.csv')
data12 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2008.csv')
data13 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2013.csv')
data14 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2014.csv')
data15 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2015.csv')
data16 = pd.read_csv('/Users/annettechiu/Desktop/USA_csv/2016.csv')


# In[38]:

data = pd.merge(data_98,data_99,on=['PHONE','STABR','LIBNAME'],how='right')  
data = pd.merge(data,data_00,on=['PHONE','STABR','LIBNAME'],how='right')  
data = pd.merge(data,data_01,on=['PHONE','STABR','LIBNAME'],how='right')  
data = pd.merge(data,data_02,on=['PHONE','STABR','LIBNAME'],how='right')
data = pd.merge(data,data_03,on=['PHONE','STABR','LIBNAME'],how='right') 
data = pd.merge(data,data_04,on=['PHONE','STABR','LIBNAME'],how='right') 
data = pd.merge(data,data_05,on=['PHONE','STABR','LIBNAME'],how='right') 


# In[39]:

data.head()


# In[40]:

data = pd.merge(data_98,data_99,on=['PHONE','STABR','LIBNAME'],how='outer')  
data = pd.merge(data,data_00,on=['PHONE','STABR','LIBNAME'],how='outer')  
data = pd.merge(data,data_01,on=['PHONE','STABR','LIBNAME'],how='outer')  
data = pd.merge(data,data_02,on=['PHONE','STABR','LIBNAME'],how='outer')
data = pd.merge(data,data_03,on=['PHONE','STABR','LIBNAME'],how='outer') 
data = pd.merge(data,data_04,on=['PHONE','STABR','LIBNAME'],how='outer') 
data = pd.merge(data,data_05,on=['PHONE','STABR','LIBNAME'],how='outer') 
data = pd.merge(data,data_06,on=['PHONE','STABR','LIBNAME'],how='outer') 
data = pd.merge(data,data_07,on=['PHONE','STABR','LIBNAME'],how='outer') 


# In[41]:

data.head()


# In[42]:

data.info()


# In[43]:

data.to_csv('Big_1998_2007.csv')


# In[44]:

dif_98 = data["1999 LOCGVT"] - data["1998 LOCGVT"]


# In[45]:

dif_98


# In[46]:

filelist = {
    "data98", "data99","data00"
            
    
}


# In[47]:

i = 1995
u_cols = ('FSCSKEY', 'LOCGVT', 'LONGITUD','LATITUDE')
for file in filelist:
   name = 'data'+str(i)
   locals()[name] = pd.read_csv(file, encoding = "ISO-8859-1",usecols = ['LOCGVT','FSCSKEY'])
   i = i+1
data2016 = pd.read_csv(file, encoding = "ISO-8859-1",usecols = ['LOCGVT','LIBNAME','FSCSKEY','ADDRESS','CITY','STABR'])


# In[ ]:



