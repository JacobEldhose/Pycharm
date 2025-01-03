import pandas as pd
a=[[101,'dona','geotge',33],[102,'dona','george',33]]
df=pd.DataFrame(a,columns=['id','fname','lname','age'])
print(df)
# a=df.shape
# print(a)
# a=df.size
# print(a)
# a=df.ndim
# print(a)
# a=df.columns
# print(a)
# a=df.dtypes
# print(a)
# a=df.head()
# print(a)
a={'id':['101','102','103','103'],'fname':['dona','dennis','kiosk','kiosk'],'age':[33,44,22,22]}
df=pd.DataFrame(a)
print(df)
a=df.shape
print(a)
a=df.size
print(a)
a=df.columns
print(a)
a=df.dtypes
print(a)
a=df.head()
print(a)
# duplicate rows are removed with the help of drop_duplicates() ,not duplicate values.,only duplcate rows
# drop_duplicates
df1=df.drop_duplicates()
print(df)
# drop()  columns(specify axis=1 ),rows (index are specified)
df1=df.drop(0)
print(df1)
df1=df.drop(['age','fname'],axis=1)
print(df1)

# reading from a file
df2=pd.read_csv('/home/user/Downloads/sample4.txt',sep=',',header=None)

print(df2)
df2.columns=['roll_no','fname','lname','age','no','loc']
print(df2)
# new column
df2['prof'] = ['ds','ds','ds','ds','ds','ds','ds','ds']
print(df2)
# to collect required columns
print(df2[['roll_no','fname','lname']])
#     first 3 fname,lname,age,loc   in one line
df3=df2[['roll_no','fname','lname','age','loc']].head(3)
print(df3)
# describe()-to describe about each columns===describe numerical values
print(df2.describe())
# top describes most repeated value
print(df2.describe(include='O'))
# if both needs to be described
print(df2.describe(include='all'))
# find the sum of misssing values
print(df2.isna().sum())
# fill the missing data
print(df2.fillna('24'))


#customer1.txt

df=pd.read_csv('/home/user/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','profession','loc']
print(df)
print('*'*100)
print(df.isna().sum())
print(df.fillna('india'))
print('*'*100)
# Hierarchy
# loc->sort ->colname->head/tail

#2. india work fname,lname,age,prof
df1=df.loc[df['loc']=='india'][['fname','lname','age','profession','loc']]
print(df1)
print('*'*100)
#3. Age mxm 5 employee fname,lname,age,prof
df1=df.sort_values(by='age',ascending=False)[['fname','lname','age','profession']] .head()
print(df1)
# 6. Age range 40 to 60 fname,lname,age,prof
df1=df.loc[(df['age']>=40) & (df['age']<=60)][['fname','lname','age','profession']]


df=pd.read_csv('/home/user/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','profession','loc']
print(df)
# 5. Each location count [count desc order]
df1=df.groupby('loc')['loc'].count().sort_values(ascending=False)
print(df1)
# 6. Full data
df1=df.loc[df['loc']=='australia']
print(df1)

# 9. India work
df1=df.loc[df['loc']=='india']
print(df1)
# A. Row count
df2=df1.shape[0]
print(df2)
# E. age above 40 full data
df2=df1.loc[df['age']>40].sort_values(by='age',ascending=False)
print(df2)

# F. age range 30 to 40 [profession count]
print('*'*100)
df2=df1.loc[(df['age']>=30)&(df['age']<=40)].groupby('profession')['profession'].count()
print(df2)



df=pd.read_csv('/home/user/Downloads/txn.txt',sep=',',header=None)
df.columns=['id','purchase_date','cust_no','amount','category','product','city','state','payment']
print(df)
# 2. jan month oid,cusno,category,product,state

df1=df.loc[(df['purchase_date']>="01-01-2011")&(df['purchase_date']<="01-31-2011")]\
       .sort_values('purchase_date')[['id','purchase_date','cust_no','category','product','city','state']]
print(df1)
# 8 Each category total amount
df1=df.groupby('category')['amount'].sum()
print(df1)
# 9 Each category maximum amount
df1=df.groupby('category')['amount'].max()
print(df1)
# 10 Each category avg amount
df1=df.groupby('category')['amount'].mean()
print(df1)
#customer5.txt
import pandas as pd
df=pd.read_csv('/home/user/Downloads/customer5.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc','salary']
print(df)
# 2.each prof min age[age desc]
df1=df.groupby('prof')['age'].min().sort_values(ascending=False)
print(df1)
# 5.each age group average salary
print("5\n")
df1=df.groupby('age')['salary'].mean()
print(df1)
df=pd.read_csv('/home/user/Downloads/customer1.txt',sep=',',header=None)
# 4000001,Kristina,Chung,55,Pilot,india
df.columns=['id','fname','lname','age','profession','loc']
print(df)
# Head and tails functions can only access from first or last columns .cannot access inbetween  columns
    # iloc may be used to access inbetween columns,rows====accesed with the help of index
#     if 5th element required.then,
print(df.iloc[:4,:1])
x=df.iloc[:,:-1]
print(x)
y=df.iloc[:,-1]
print(y)

# data_cleaning
#Missing values,wrong format
import pandas as pd
df=pd.read_csv('/home/user/Downloads/missing_data.csv',sep=',')
print(df)
print(df.isna().sum())
# print(df.fillna('240'))
# still df has missing values hence we use keyword called "inplprint(df)ace"
# df.fillna('240',inplace=True)
# print(df)

# x=df['Calories'].mean()
# df['Calories'].fillna(x,inplace=True)
# print(df)
# x=df['Date'].mode()[0]
#
# df['Date'].fillna(x,inplace=True)
# print(df)

# dropna() can also be used to drop the rows which has missing values in it but index will not be continous
# print(df.dropna())
# print(df.dropna(axis=1))  whole column is removed
# print(df.dropna(subset='Calories',inplace=True))
# print(df)
# print(df.dropna(ignore_index=True))

# 4 types of joining

# 1.inner joining
# 2.left outer joining
# 3.right outer joining
# 4.full outer joining

# inner joining

# 2dataframe can be joined by using common fields in 2 dataframes
#2 dataframes are combined  if the common field is having matching values
# nested dic:id,fname,lname,loc
dic1={'id':['1','2','3','4','5'],
      'fname':['rajeev','jay','jessy','kerli','genny'],
      'lname':['e','k','r','a','h'],
      'age':['25','26','27','30','34']}
dic2={'id':['4','5','6','7','8'],'prof':['bigdata','python','IT','IT','IT'],'salary':['25000','25000','25000','25000','25000'],'loc':['andra','jammu','kerala','delhi','up']}
df1=pd.DataFrame(dic1)
print(df1)
df2=pd.DataFrame(dic2)
print(df2)
df3=pd.merge(df1,df2,on='id',how='inner')
print(df3)
df3=pd.merge(df1,df2,on='id',how='left')
print(df3)
df3=pd.merge(df1,df2,on='id',how='right')
print(df3)
df3=pd.merge(df1,df2,on='id',how='outer')
print(df3)

import pandas as pd
df1=pd.read_csv("/home/user/Downloads/student",sep=',',header=None)
df2=pd.read_csv("/home/user/Downloads/results",sep=',',header=None)
df1.columns=['name','roll_no']
df2.columns=['roll_no','result']
df3=pd.merge(df1,df2,on='roll_no',how='inner')
print(df3)
# pass==name,roll_no,result
print(df3.loc[df3['result']=='pass'] [['name','roll_no','result']])


df=pd.read_csv('/home/user/Downloads/missing_data.csv',sep=',')
print(df)
df.loc[7,'Duration']=45
print(df)
x=df['Calories'].mean()
print(x)
for i in df.index:
    if df.loc[i,'Calories'] >350:
        df.loc[i,'Calories']=x
print(df)


#######################################
# interview qns:
# difference between linspace and arange
# difference between reshape and flatten
# interview qn:perform dot product(2d)
#sort,ceil,round
#########################################