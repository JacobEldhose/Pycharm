import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\heart.csv")
print(df)
print('*'* 100)
print(df.shape)
print('*'* 100)
print(df.columns)
print('*'* 100)
print(df.dtypes)
print('*'* 100)
print(df.isna().sum())
print('*'* 100)
x = df.iloc[:,:-1]
print(x)
print('*'* 100)
y = df.iloc[:,-1:]
print(y)
print('*'* 100)
print(df.groupby('target')['target'].count().sort_values(ascending=False))
x = df['trestbps'].mean()
df['trestbps'].fillna(x,inplace=True)
x = df['restecg'].mode()[0]
df['restecg'].fillna(x,inplace=True)
x = df['thalach'].mean()
#df['restecg]=df['restecg].fillna(df['restecg].mode()[o])
df['thalach'].fillna(x,inplace=True)
x = df['ca'].mode()[0]
df['ca'].fillna(x,inplace=True)
x = df['thal'].mode()[0]
df['thal'].fillna(x,inplace=True)
print(df)

print(df.isna().sum())

print('*'* 100)
x = df['thalach'].mean()
for i in df.index:
    if df.loc[i,'thalach']>180:
        df.loc[i,'thalach'] = x
print(df)
df.to_csv("C:\\Users\\jacob\\Downloads\\heart_clean.csv",index=False)