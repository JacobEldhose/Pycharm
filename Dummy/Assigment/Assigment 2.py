import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\txn.txt")
df.columns = ['orderid','purchasedate','customerid','amount','product','category','city','state','payment']
print(df.shape)

print('*'*100)

print(df['purchasedate']>='1-1-')