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

path = "images/Copy of Intern Ranges 2024 - US Summary.csv"
df2 = pd.read_csv(path)
print(df2)