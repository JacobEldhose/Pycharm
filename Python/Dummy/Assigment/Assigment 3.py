import pandas as pd

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\movies_cleaned_pandas.csv")

df.columns = ['id','name','year','rating','duration']
# print(df)

# 1. Find row count
# print(df.shape)
# print('*'*100)
#
# # 2. Remove duplicates and find row count
# df1 = df.drop_duplicates()
# print(df1)
# print('*'*100)
#
# # 3. Sort data set by release year in des order
# print(df.sort_values(by='year',ascending=False))
# print('*'*100)
#
# # 4. Find rating mxm 5 movies name,year,rating
# print(df.sort_values(by='rating',ascending=False)[['name','year','rating']].head(5))
# print('*'*100)
#
# # 5. Find rating minimum 3 movies name,year,rtaing
# print(df.sort_values(by='rating')[['name','year','rating']].head(3))
# print('*'*100)
#
# # 6. Find Each year release movie count [count desc order]
# print(df.groupby('year')['year'].count().sort_values(ascending=False))
# print('*'*100)
#
# # 7. Each rating count [count desc order]
# print(df.loc[(df['year']==2008)&(df['rating']>3)])
# print('*'*100)
#
# # 8. 2008 and rating above 3 [collect]
# print((df.loc[(df['year']==2008)&(df['rating']>3)]).shape)
# print('*'*100)
#
# # 9. Find duration mxm 1 movies name,year,rating,duration
# print(df.sort_values(by='duration',ascending=False)[['name','year','rating','duration']].head(1))
# print('*'*100)
#
# # 10. Find rating mnm 1 movies name,year,rating,duration
# print(df.sort_values(by='duration')[['name','year','rating','duration']].head(1))
# print('*'*100)
# # 11. Rating above 4 and release year above 2005
#
# print(df.loc[(df['rating']>4)&(df['year']>=2005)])
# print('*'*100)
#
# print(df.loc[df['rating']==4.5])
# print('*'*100)
# print(df.loc[df['rating']==4.1])
# print('*'*100)
#
# # 12. 2008 movies count
# print(df.loc[df['year']==2008].shape)
# print('*'*100)
#
# # 13. 1975-2000 movies collect
# print(df.loc[(df['year']>=1975)&(df['year']<=2000)])
# print('*'*100)
# print((df.loc[(df['year']>=1975)&(df['year']<=2000)]).shape)
# print('*'*100)
#
# # 14. 1975-2000 and rating above 3.5 total row count
# print(df.loc[(df['year']>=1975)&(df['year']<=2000)&(df['rating']>3.5)])

print(df.groupby['rating']['rating'].count().sort_values)