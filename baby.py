import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import groupby

B_names=pd.read_csv('yob2000.txt',names=['Baby Name','Gender','Total count'])
new=B_names.sort_values(by='Total count',ascending=False)
new=new.head(20)

B_names_2=pd.read_csv('yob2016.txt',names=['Baby Name','Gender','Total count'])
new_2=B_names_2.sort_values(by='Total count',ascending=False)
new_2=new_2.head(20)

c = pd.merge(new, new_2, on='Baby Name', how='outer', suffixes=(' 2016', ' 2000'))
c.plot(x='Baby Name', kind='bar')
plt.title('Top 20 baby counts from 2000 and 2016')
plt.show()


group=B_names_2.groupby(B_names_2['Baby Name'].str[-1:])['Total count'].sum()
group.plot(x='Baby Name',kind='bar')
plt.title('Count by last character')
plt.show()













