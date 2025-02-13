# import pandas as pd

# # ✅ Load dataset
# df = pd.read_csv("kz.csv")  # Make sure 'kz.csv' is in the same folder as this script

# # ✅ Print first 5 rows
# print("📌 First 5 rows of the dataset:")
# print(df.head())

# # ✅ Print dataset structure
# print("\n📌 Dataset Info:")
# print(df.info())

# # ✅ Print total number of rows
# print(f"\n📌 Total rows: {df.shape[0]}")


 

import pandas as pd

try:

    df = pd.read_csv("kz.csv")  
    print("\n✅ CSV Loaded Successfully!")
    

    print(df.head())

except FileNotFoundError:
    print("❌ Error: The file 'kz.csv' was not found.")
    exit()
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    exit()


try:
    df.drop_duplicates(inplace=True)
    print("\n✅ Duplicates Removed Successfully!")
except Exception as e:
    print(f"❌ Error removing duplicates: {e}")


for column in df.columns:
    if df[column].dtype == 'float64' or df[column].dtype == 'int64':  
        df[column].fillna(0, inplace=True)  
    else:
        df[column].fillna("Unknown", inplace=True) 

print("\n✅ Missing Values Handled Correctly!")



try:
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        print("\n✅ Date Column Converted Successfully!")
except Exception as e:
    print(f"❌ Error converting date column: {e}")


try:
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    print("\n✅ Column Names Standardized!")
except Exception as e:
    print(f"❌ Error standardizing column names: {e}")

df.to_csv("cleaned_kz.csv", index=False)

print("\n✅ Data cleaning complete! Saved as 'cleaned_kz.csv'.")

# # ✅ Print final DataFrame
# print("\n📌 Final Cleaned Dataset:")
# print(df.head())

# from sqlalchemy import create_engine

# # ✅ PostgreSQL connection string (Replace with your details)
# db_url = "postgresql://postgres:abadit.kas1912@localhost:5432/ethiocommerce"
# # ✅ Create database connection
# engine = create_engine(db_url)

# print("\n✅ Connected to PostgreSQL successfully!")

import pandas as pd
from sqlalchemy import create_engine

# ✅ Load the cleaned dataset
try:
    df = pd.read_csv("cleaned_kz.csv")
    if df.empty:
        print("❌ Error: The dataset is empty. Ensure it has data before inserting into PostgreSQL.")
        exit()
    print("\n✅ Cleaned dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: 'cleaned_kz.csv' file not found.")
    exit()
except pd.errors.EmptyDataError:
    print("❌ Error: The file is empty!")
    exit()
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    exit()
db_url = "postgresql://postgres:abadit.kas1912@localhost:5432/ethiocommerce"
try:
    engine = create_engine(db_url)
    print("\n✅ Connected to PostgreSQL successfully!")
except Exception as e:
    print("❌ Database connection error:", e)
    exit()
try:
    df.to_sql("ecommerce_data", engine, if_exists="replace", index=False)
    print("\n✅ Data successfully stored in PostgreSQL!")
except Exception as e:
    print("❌ Error inserting data:", e)






