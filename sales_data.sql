CREATE DATABASE my_sales_db;
USE my_sales_db;


CREATE TABLE sales (
    id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price_per_unit FLOAT,
    sale_date DATE
);

INSERT INTO sales VALUES
(1, 'Shampoo', 'Beauty', 10, 150.0, '2023-11-10'),
(2, 'Notebook', 'Stationery', 5, 40.0, '2023-11-11'),
(3, 'Shampoo', 'Beauty', 7, 150.0, '2023-11-15'),
(4, 'Pencil', 'Stationery', 20, 5.0, '2023-12-01'),
(5, 'Pen', 'Stationery', 15, 10.0, '2023-12-02');

select * from Sales