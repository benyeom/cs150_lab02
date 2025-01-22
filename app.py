import pandas as pd

# s = pd.Series([42, 21, 7, 3.5])
# print(s)

df = pd.DataFrame({'age': 18,
                   'name': ['Alice', 'Bob', 'Carl'],
                   'cardio': [60, 70, 80]})
# print(df)
# print(df.loc[:, 'name'])
df.loc[1:, 'age'] = 16
print(df)

print("hello, world")