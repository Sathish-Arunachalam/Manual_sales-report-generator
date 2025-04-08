
import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Hsisath@1',
    database='my_sales_db'
)

# Query the data
query = "SELECT *, quantity * price_per_unit AS total_price FROM sales"
df = pd.read_sql(query, conn)

# Convert sale_date to datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Monthly total sales
df['month'] = df['sale_date'].dt.to_period('M')
monthly_sales = df.groupby('month')['total_price'].sum().reset_index()

# Top selling product
top_product = df.groupby('product_name')['quantity'].sum().idxmax()

# Total revenue
total_revenue = df['total_price'].sum()

# Save result to CSV
df.to_csv('Sales_Report.csv', index=False)

# Print summary
print("Total Revenue:", total_revenue)
print("Top Product:", top_product)
print("\nMonthly Sales:")
print(monthly_sales)

conn.close()
