import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv("data/cleaned/cleaned_superstore.csv")

# Connect database
conn = sqlite3.connect("database/retail_analytics.db")

# Store into SQLite
df.to_sql("superstore", conn, if_exists="replace", index=False)

print("Data successfully loaded into SQLite!")

conn.close()