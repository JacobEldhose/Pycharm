# Customer.txt

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\customer1.txt")
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'loc']

print(df.shape)

df.drop_duplicates()
print(df.shape)

df1 = df.sort_values(by= 'age') \
        [['fname','lname',"prof",'loc']].head(10)
print(df1)
print('*'*100)
df2 = df.sort_values(by= 'age',ascending=False) \
        [['fname','lname',"prof",'loc']].head(5)
print(df2)
print('*'*100)

df3 = df.groupby('loc') ['loc'].count()\
         .sort_values(ascending=False)
print(df3)
print('*'*100)

df4 = df.loc[df['loc']=='australia']
print(df4)
print('*'*100)

df5 = df.groupby('age') ['age'].count()\
         .sort_values(ascending=False)
print(df5)
print('*'*100)

df6 = df.groupby('prof') ['prof'].count()\
         .sort_values(ascending=False)
print(df6)

print('*'*100)
print('*'*100)

ind = df.loc[df['loc']=='india']
print(ind.shape)
print('*'*100)
in1 = ind.groupby('prof')['prof'].count()\
          .sort_values(ascending=False)
print(in1)
print('*'*100)
in2 = ind.sort_values(by= 'age',ascending=False) [['fname','lname','age','prof']].head(3)
print(in2)
print('*'*100)

in3 = ind.sort_values(by= 'age') [['fname','lname','age','prof']].head(3)
print(in3)
print('*'*100)

in4 = ind.loc[ind['age']>=40]
print(in4)
print('*'*100)

in5 = ind.loc[(ind['age']>=40) & (ind['age']<=60)]
print(in5)
print('*'*100)
print('*'*100)

us = df.loc[df['loc']=='us']
print(us.shape)
print('*'*100)

us1 = us.groupby('age') ['age'].count()
print(us1)
print('*'*100)

us2 = us.groupby('prof') ['prof'].count()\
         .sort_values(ascending=False)
print(us2)
print('*'*100)

us3 = us.loc[(us['prof']=='Civil engineer')&(us['age']>=30)]
print(us3)