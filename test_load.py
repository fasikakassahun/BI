import pandas as pd

try:
    df = pd.read_csv("cleaned_kz.csv")
    print("\n✅ File loaded successfully!")
    print(df.head())  # Show first 5 rows
except FileNotFoundError:
    print("❌ Error: 'cleaned_kz.csv' file not found.")
except pd.errors.EmptyDataError:
    print("❌ Error: The file is empty!")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
