import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\customer1.txt", sep=',', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']

df1 = df[['fname', 'lname', 'age', 'prof']].head(50)
print(df1)
print("*" * 100)

df2 = df[['fname', 'lname', 'age']].head(20)
print(df2)
print('*' * 100)

print(df.isna().sum())
print("*"*100)

df3 = df.fillna('India')
print(df3)

print(df3.isna().sum())
