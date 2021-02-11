import pandas as pd

df = pd.read_csv('DATA/primeministers.csv', index_col="term")
print(df.head())
print(df.loc[20])
print(df.party)
print(df.loc[:,['lastname', 'party']])