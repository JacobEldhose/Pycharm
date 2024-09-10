import pandas as pd
nst_dit1 = {
    'id': [1,2,3,4,5],
    'fname':['achu','kannan','sachin','rahul','suresh'],
    'lname':['k','r','s','r','s'],
    'age':[25,26,27,28,29]
}

nst_dit2 = {
    'id' : [4,5,6,7,8],
    'profession':['pilot','actor','doctor','engineer','civil engineer'],
    'salary':[30000,28000,70000,61000,43000],
    'location':['chennai','madurai','chennai','madurai','chennai']
}

df1 = pd.DataFrame(nst_dit1)

df2 = pd.DataFrame(nst_dit2)

# left outer join all data from left df and same values of left and right

df3 = df1.merge(df2, on='id', how='left')
print(df3)

# right outer join all data from right df and same values of left and right

df3 = df1.merge(df2, on='id',how='right')
print(df3)

df3 = df1.merge(df2, on='id',how='outer')
print(df3)