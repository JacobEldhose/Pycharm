import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\customer1.txt")
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']
#
# print(df.iloc[::])
#
# print(df.iloc[10:26,1:])

# x = df.iloc[:,0:4]
# y = df.iloc[:,5:]
# print(x)
# print('*'*100)
# print(y)

"""
filter 
loc
new_df = old_df.loc[old['col_name']condition]
"""

# df1 = df.loc[df['age']>50]
# print(df1)

# df1 = df.loc[df['location']=='india'] [['fname','lname','age','prof']]
# print(df1)
#
# print('*'*100)
#
# df2 = df.loc[df['prof']=='Doctor']
# print(df2)
#
# print('*'*100)
#
# df3 = df.loc[df['age']<30]
# print(df3)
#
# print('*'*100)
#
# df1 = (df.loc[(df['age']>50)&(df['location']=='india')]\
#             [['fname','lname','age']])
# print(df1)

# df['location'] = df['location'].fillna('india')
# print(df.isna().sum())

# df1 = df.loc[df['location']=='india'] \
#             .sort_values(by='age')\
#             [['fname','lname','age','prof']]
# print(df1)
# print('*'*100)
# df2 = df.sort_values(by='age',ascending=False)\
#           [['fname','lname','age','prof']].head(5)
# print(df2)
#
# print('*'*100)
#
# df3 = df.sort_values(by='age')\
#           [['fname','lname','age','prof']].head(3)
# print(df3)
# print('*'*100)
#
# df4 = df.loc[df['location']=='uk'] \
#             .sort_values(by='age')\
#             [['fname','lname','age']]
# print(df4)
# print('*'*100)
#
# df5 = df.loc[(df['age']<=60) & (df['age']>=40)] \
#             [['fname','lname','age']]
# print(df5)
# print('*'*100)
#
# df6 = df.loc[df['location']=='india'] \
#              .sort_values(by='age')\
#               [['fname','lname','age']].head(2)
# print(df6)
# print('*'*100)
# df7 = df.loc[(df['location']=='india')&(df['prof']=='Doctor')]\
#             [['fname','lname','age']]
# print(df7)
# print('*'*100)
#
# df8 = df.loc[df['prof']=='Pilot']\
#         .sort_values(by='age') \
#             [['fname','lname','age']].head(1)
# print(df8)
# print('*'*100)
#
# df9 = df.groupby('prof')['prof'].count()\
#          .sort_values(ascending=False)
# print(df9)

df10 = df.loc[df['location']=='india']\
          .groupby('prof') ['prof'].count()
print(df10)