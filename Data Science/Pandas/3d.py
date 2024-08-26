import pandas as pd

dic = {'id': 101, 'fname': 'arun', 'lname': 'k', 'age': 27, 'prof': 'bigdata'}
s = pd.Series(dic, index=['lname', 'age', 'id', 'prof', 'fname'])
print(s)
