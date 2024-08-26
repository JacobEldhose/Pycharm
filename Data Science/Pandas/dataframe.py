import pandas as pd
import numpy as np

lst = [[101, 'jacob', 'e', 20, 'bigdata', 25000],
       [102, 'varun', 'k', 2, 'bigdata', 26000],
       [103, 'krishna', 'r', 24, 'datascience', 30000],
       [104, 'rethin', 't', 22, 'datascience', 35000],
       [105, 'eli', 'a', 23, 'bigdata', 25000],
       [106, 'don', 'a', 23, 'bigdata', 29000],
       [107, 'john', 'j', 20, 'datascience', 25000]]
df = pd.DataFrame(lst, columns=['id', 'fname', 'lname', 'age', 'prof', 'salary'])
print(df.head(3))
print(df.tail(2))
print(df.dtypes)

print(df.columns)
