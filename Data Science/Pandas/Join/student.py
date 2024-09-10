import pandas as pd

df1 = pd.read_csv("C:\\Users\\jacob\\Downloads\\student.unknown")
df1.columns = ['name','rollno']

df2 = pd.read_csv("C:\\Users\\jacob\\Downloads\\results.unknown")
df2.columns = ['rollno','result']

df3 = df1.merge(df2,on='rollno',how='inner')
print(df3.loc[df3['result'] == 'pass'])