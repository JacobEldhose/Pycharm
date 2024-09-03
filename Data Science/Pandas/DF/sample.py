import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\sample4.txt")
df.columns = ['id', 'fname', 'lname', 'age', 'phno', 'location']

# df1 = df.loc[df['age'] > 22][['fname', 'lname', 'age', 'phno']]
# print(df1)
# print('*' * 100)
#
# df2 = df.loc[df['age'] == 21][['fname', 'lname', 'age']]
# print(df2)
# print('*' * 100)
#
# df3 = df.loc[df['location'] == 'Chennai'][['fname', 'lname', 'age', 'phno']]
# print(df3)
# print('*' * 100)
#
# df4 = df.loc[(df['age'] > 23) & (df['location'] == 'Chennai')][['fname', 'lname', 'age']]
# print(df4)
# print('*' * 100)

df5 = df.groupby('location')['location'].count() \
        .sort_values()

print(df5)

print("*" * 100)

df6 = df.groupby('age')['age'].count()
print(df6)

print('*' * 100)
