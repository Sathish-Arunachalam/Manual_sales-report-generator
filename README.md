# Manual_sales-report-generator
End-to-end Manual sales analysis using Python, MySQL, and pandas.

# 📊 Automated Sales Report Generator

A Python and SQL-based project that automates the generation of monthly sales reports using real-time data from a MySQL database. This project is designed to help businesses quickly view key sales insights without manual effort.

## 🚀 Features

- 📦 Extracts sales data from a MySQL database
- 🔍 Performs data cleaning and transformation using **pandas**
- 📈 Calculates:
  - Total Revenue
  - Top-selling Product
  - Monthly Sales Summary
- ⚡ Automates the entire process in one run using Python scripts

## 🛠️ Technologies Used

- **Python 3**
- **MySQL**
- **pandas**
- **mysql-connector-python**

## 🧩 Database Schema

### `sales_data` Table

| Column Name   | Data Type | Description              |
|---------------|-----------|--------------------------|
| order_id      | INT       | Unique order identifier  |
| product_name  | VARCHAR   | Name of the product      |
| quantity      | INT       | Units sold               |
| price         | FLOAT     | Price per unit           |
| order_date    | DATE      | Date of purchase         |

> Make sure this table exists in your MySQL database before running the script.

## 🔧 How to Run

1. Clone the repository or download the script.
2. Install required packages:

pip install pandas mysql-connector-python

3. Update your MySQL credentials and database name in the script:
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hsisath@1",
    database="my_sales_db"
)

Run the script:

python sales_report_generator.py

Output

Total Revenue: 3000.0
Top Product: Pencil

Monthly Sales:
     month  total_price
0  2023-11       2750.0
1  2023-12        250.0