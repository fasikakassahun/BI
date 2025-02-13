
# from telethon.sync import TelegramClient


# api_id =  20052466  
# api_hash = "1578ff5220e0775b364dd6f0f9941d04"  
# phone = "+251925913222"
# # Create the Telegram Client
# client = TelegramClient(phone, api_id, api_hash)

# async def scrape_telegram_data(channel_username):
#     print("Starting Telegram Client...") 
#     await client.start()
#     print("Connected to Telegram!") 
#     # Fetch and print messages
#     async for message in client.iter_messages(channel_username, limit=10):
#         print(message.text)  

# with client:
#     print("Running the script...")  
#     client.loop.run_until_complete(scrape_telegram_data("zawige"))  




# import pandas as pd
# from telethon.sync import TelegramClient


# api_id =  20052466  
# api_hash = "1578ff5220e0775b364dd6f0f9941d04"  
# phone = "+251925913222"

# # Connect to Telegram
# client = TelegramClient(phone, api_id, api_hash)

# # Create a list to store messages
# messages_list = []

# async def scrape_telegram_data(channel_username):
#     print("Connected to Telegram!")
#     async for message in client.iter_messages(channel_username, limit=1000):
#         if message.text:  
#             messages_list.append({"date": message.date, "message": message.text})

# with client:
#     client.loop.run_until_complete(scrape_telegram_data("zawige"))

# # Convert the list to a Pandas DataFrame
# df = pd.DataFrame(messages_list)

# # Print the first few rows
# print(df.head())






# import pandas as pd
# from telethon.sync import TelegramClient


# api_id =  20052466  
# api_hash = "1578ff5220e0775b364dd6f0f9941d04"  
# phone = "+251925913222"

# # Connect to Telegram
# client = TelegramClient(phone, api_id, api_hash)

# # Create a list to store messages
# messages_list = []

# async def scrape_telegram_data(channel_username):
#     print("Connected to Telegram!")
#     async for message in client.iter_messages(channel_username, limit=1000):
#         if message.text:  # Only store messages with text
#             messages_list.append({"date": message.date, "message": message.text})

# with client:
#     client.loop.run_until_complete(scrape_telegram_data("zawige"))

# # Convert the list to a Pandas DataFrame
# df = pd.DataFrame(messages_list)

# # Clean the data
# df.drop_duplicates(inplace=True)
# df.fillna("No Message", inplace=True)
# df["date"] = pd.to_datetime(df["date"])
# df.columns = df.columns.str.lower().str.replace(" ", "_")

# # Print cleaned data (optional)
# print(df.info())  
# print(df.head())

# # Save cleaned data to CSV
# df.to_csv("cleaned_telegram_data.csv", index=False)

# print("Data cleaning complete! Saved as 'cleaned_telegram_data.csv'.")







import pandas as pd
from telethon.sync import TelegramClient
from sqlalchemy import create_engine

api_id = 20052466  
api_hash = "1578ff5220e0775b364dd6f0f9941d04"  
phone = "+251925913222"

# Connect to Telegram
client = TelegramClient(phone, api_id, api_hash)

# Create a list to store messages
messages_list = []

async def scrape_telegram_data(channel_username):
    print("Connected to Telegram!")
    async for message in client.iter_messages(channel_username, limit=1000):
        if message.text:  # Only store messages with text
            messages_list.append({"date": message.date, "message": message.text})

with client:
    client.loop.run_until_complete(scrape_telegram_data("zawige"))


df = pd.DataFrame(messages_list)


df.drop_duplicates(inplace=True)
df.fillna("No Message", inplace=True)
df["date"] = pd.to_datetime(df["date"])
df.columns = df.columns.str.lower().str.replace(" ", "_")


print(df.info())  
print(df.head())


df.to_csv("cleaned_telegram_data.csv", index=False)

print("Data cleaning complete! Saved as 'cleaned_telegram_data.csv'.")


engine = create_engine("postgresql://postgres:abadit.kas1912@localhost:5432/ecommerce_db")

# Load data into the database
df.to_sql("telegram_messages", engine, if_exists="append", index=False)

print("Data successfully stored in PostgreSQL!")



from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL connection string 
engine = create_engine("postgresql://postgres:abadit.kas1912@localhost:5432/ecommerce_db")

try:
 
    if df.empty:
        print("❌ No data to insert into PostgreSQL. DataFrame is empty!")
    else:

        df.to_sql("telegram_messages", engine, if_exists="append", index=False)
        print("✅ Data successfully stored in PostgreSQL!")
except Exception as e:
    print("❌ Error inserting data:", e)

import pandas as pd
from telethon.sync import TelegramClient
from sqlalchemy import create_engine


api_id = 20052466  
api_hash = "1578ff5220e0775b364dd6f0f9941d04"  
phone = "+251925913222"

# ✅ Connect to Telegram
client = TelegramClient(phone, api_id, api_hash)

# ✅ Create a list to store messages
messages_list = []

async def scrape_telegram_data(channel_username):
    print("✅ Connected to Telegram!")
    async for message in client.iter_messages(channel_username, limit=1000):
        if message.text:  
            messages_list.append({"date": message.date, "message": message.text})

with client:
    client.loop.run_until_complete(scrape_telegram_data("zawige"))

# ✅ Convert the list to a Pandas DataFrame
df = pd.DataFrame(messages_list)

# ✅ Ensure `df` is not empty
if df.empty:
    print("❌ No data scraped! Exiting...")
    exit()

# ✅ Clean the data
df.drop_duplicates(inplace=True)
df.fillna("No Message", inplace=True)
df["date"] = pd.to_datetime(df["date"])
df.columns = df.columns.str.lower().str.replace(" ", "_")

# ✅ Print cleaned DataFrame
print(df.info())
print(df.head())

# ✅ Save cleaned data to CSV
df.to_csv("cleaned_telegram_data.csv", index=False)
print("✅ Data cleaning complete! Saved as 'cleaned_telegram_data.csv'.")

# ✅ PostgreSQL connection string 
engine = create_engine("postgresql://postgres:abadit.kas1912@localhost:5432/ecommerce_db")

try:
    # ✅ Insert data into PostgreSQL
    df.to_sql("telegram_messages", engine, if_exists="append", index=False)
    print("✅ Data successfully stored in PostgreSQL!")
except Exception as e:
    print("❌ Error inserting data:", e)

