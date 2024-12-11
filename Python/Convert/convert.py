import pandas as pd

df = pd.read_csv("D:\\Luminar\\results.unknown",header=None)
df.columns=['roll',"res"]
df.to_csv("D:\\Luminar\\results.csv")
