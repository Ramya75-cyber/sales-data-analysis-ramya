import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data_sample.csv", encoding='latin1')

# Clean (optional)
df = df.dropna()

# Convert date
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

# 1. Sales by Product
product_sales = df.groupby("PRODUCTLINE")["SALES"].sum()
product_sales.plot(kind='bar')
plt.title("Sales by Product Line")
plt.show()

# 2. Monthly Sales Trend
monthly = df.groupby(df["ORDERDATE"].dt.month)["SALES"].sum()
monthly.plot()
plt.title("Monthly Sales Trend")
plt.show()

# 3. Top Countries
country = df.groupby("COUNTRY")["SALES"].sum().head(10)
country.plot(kind='bar')
plt.title("Top Countries by Sales")
plt.show()

# 4. Order Status
status = df["STATUS"].value_counts()
status.plot(kind='pie', autopct='%1.1f%%')
plt.title("Order Status Distribution")
plt.show()