import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/superstore.csv", encoding="latin1")

# Show basic info
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Save cleaned dataset
df.to_csv("data/cleaned/cleaned_superstore.csv", index=False)

print("\nData cleaning completed successfully.")