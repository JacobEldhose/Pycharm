import pandas as pd

df1 = pd.read_csv("C:\\Users\\jacob\\Downloads\\custom.txt")
df1.columns = ['id','name','age','loc','sal']

df2 = pd.read_csv("C:\\Users\\jacob\\Downloads\\order.txt")
df2.columns = ['orderid','timestamp',"id",'amount']

df3 = df1.merge(df2,on='id',how='inner')
print(df3[['name','age','loc','timestamp','amount']])
print('*'*100)
print(df3.loc[df3['sal']>=2500][['name','age','loc','sal','timestamp','amount']])
print('*'*100)
print(df3.sort_values(by='timestamp',ascending=False)[['name','age','sal','timestamp','amount']].head(1))
print('*'*100)
print(df3.sort_values(by='age',ascending=False)[['name','age','sal','timestamp','amount']].head(1))