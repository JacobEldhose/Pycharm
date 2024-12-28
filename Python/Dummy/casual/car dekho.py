import pandas as pd
import numpy as np
import re

pd.set_option('display.max_columns',None)

df = pd.read_csv("D:\\Luminar\\Car dekho (1).csv")
print(df.isna().sum())
print(df.dtypes)
df['mileage'] = df['mileage'].str.extract(r'(\d+)', expand=False).astype(float)
df['engine'] = df['engine'].str.extract(r'(\d+)', expand=False).astype(float)
df['max_power'] = df['max_power'].str.extract(r'(\d+)', expand=False).astype(float)
df['torque'] = df['torque'].str.extract(r'(\d+)', expand=False).astype(float)
df.drop_duplicates()
x = df['mileage'].mean()
df['mileage'].fillna(x,inplace=True)
x = df['engine'].mean()
df['engine'].fillna(x,inplace=True)
x = df['max_power'].mean()
df['max_power'].fillna(x,inplace=True)
x = df['torque'].mean()
df['torque'].fillna(x,inplace=True)
df['seats'].fillna(df['seats'].mode()[0],inplace=True)
print(df.isna().sum())

df.to_csv("D:\\Luminar\\Car dekho cleaned.csv")