import pandas as pd
 
df = pd.read_csv("Countries.csv")

print("First 5 rows of the dataset:")
print(df.head())

print("Last 5 rows of the dataset:")
print(df.tail())

print("Shape of the dataset:")
print(df.shape)

print("Column names:")
print(df.columns)

print("Dataset information:")
print(df.info())

print("Summary statistics:")
print(df.describe())

print("Data types:")
print(df.dtypes)

print("Missing values:")
print(df.isnull().sum())

print("Unique values:")
print(df.nunique())

print("Random 5 rows:")
print(df.sample(5))

print("Value counts:")
print(df["ColumnName"].value_counts())
