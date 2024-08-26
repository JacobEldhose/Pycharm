import pandas as pd
import numpy as np

dic = {'id': [10, 11, 12, 13, 14],
       'fname': ['rahul', 'jake', 'vipin', 'anil', 'vimal'],
       'lname': ['k', 'p', 's', 'w', 'p'],
       'marks': [20, 30, 40, 50, 60]}
df = pd.DataFrame(dic)

print(df)
