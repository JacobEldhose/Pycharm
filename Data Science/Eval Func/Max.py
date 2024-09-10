import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\customer1.txt")
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']

print(df.groupby('prof')['age'].max())