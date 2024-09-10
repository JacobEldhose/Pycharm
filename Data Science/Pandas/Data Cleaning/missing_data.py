import pandas as pd

df = pd.read_csv("C:\\Users\\jacob\\Downloads\\missing_data.csv")
print(df.isna().sum())
# mean median  mode - object
# df['Calories'].fillna(inplace=True,method=
#                       )
#
# x = df['Calories'].mode()[0]
# df['Calories'].fillna(x,inplace=True)
# y = df['Date'].mode()[0]
# df['Date'].fillna(y,inplace=True)
# print(df)


# dropna to remove the row with missing values


df.dropna(subset='Calories', inplace=True,ignore_index=True)
print(df)