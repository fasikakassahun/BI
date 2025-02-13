import pandas as pd

# Load the dataset (Make sure the CSV file is in the same folder as this script)
df = pd.read_csv("kz.csv")

# Print first 5 rows
print(df.head())

# Print dataset information
print(df.info())

# Print the number of rows
print(f"Total rows: {df.shape[0]}")
