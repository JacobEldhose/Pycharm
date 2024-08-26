import pandas as pd

s1 = pd.Series([4, 6, 7, 8, 9, 1])
s2 = pd.Series([5, 1, 4, 2, 1, 5, 6])

s3 = s1.add(s2)
print(s3)

s4 = s1.mul(s2)
print(s4)

s5 = s1.div(s2)
print(s5)

s6 = s1._append(s2,ignore_index=True)
print(s6)