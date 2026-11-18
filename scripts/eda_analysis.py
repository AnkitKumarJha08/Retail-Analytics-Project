import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/cleaned/cleaned_superstore.csv")

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])

# =========================
# Monthly Sales Trend
# =========================

monthly_sales = df.groupby(
    df['Order Date'].dt.to_period('M')
)['Sales'].sum()

plt.figure(figsize=(12,6))

monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

# =========================
# Category-wise Sales
# =========================

category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))

category_sales.plot(kind='bar')

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()

# =========================
# Region-wise Profit
# =========================

region_profit = df.groupby('Region')['Profit'].sum()

plt.figure(figsize=(8,5))

region_profit.plot(kind='bar')

plt.title("Region-wise Profit")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.show()

# =========================
# Top 10 Products
# =========================

top_products = df.groupby('Product Name')['Sales'].sum() \
                 .sort_values(ascending=False) \
                 .head(10)

plt.figure(figsize=(12,6))

top_products.plot(kind='bar')

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()

print("\nEDA Analysis Completed Successfully")