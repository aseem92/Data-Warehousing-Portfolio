CREATE DATABASE enterprise_dw;
USE enterprise_dw;

CREATE TABLE stg_customers (
customer_id INT,
customer_name VARCHAR(100),
city VARCHAR(100),
state VARCHAR(100),
segment VARCHAR(50)
);

CREATE TABLE stg_products (
product_id INT,
product_name VARCHAR(100),
category VARCHAR(100),
brand VARCHAR(100),
unit_cost DECIMAL(10,2)
);

CREATE TABLE stg_employees (
employee_id INT,
employee_name VARCHAR(100),
department VARCHAR(100),
branch VARCHAR(100)
);

CREATE TABLE stg_branches (
branch_id INT,
branch_name VARCHAR(100),
city VARCHAR(100),
state VARCHAR(100)
);

CREATE TABLE stg_sales (
sales_id INT,
sales_date DATE,
customer_id INT,
product_id INT,
employee_id INT,
branch_id INT,
quantity INT,
unit_price DECIMAL(10,2),
discount DECIMAL(10,2)
);


CREATE TABLE dim_customer(

customer_key INT AUTO_INCREMENT PRIMARY KEY,

customer_id INT,

customer_name VARCHAR(100),

city VARCHAR(100),

state VARCHAR(100),

segment VARCHAR(50)

);

CREATE TABLE dim_product(

product_key INT AUTO_INCREMENT PRIMARY KEY,

product_id INT,

product_name VARCHAR(100),

category VARCHAR(100),

brand VARCHAR(100),

unit_cost DECIMAL(10,2)

);

CREATE TABLE dim_employee(

employee_key INT AUTO_INCREMENT PRIMARY KEY,

employee_id INT,

employee_name VARCHAR(100),

department VARCHAR(100),

branch VARCHAR(100)

);

CREATE TABLE dim_branch(

branch_key INT AUTO_INCREMENT PRIMARY KEY,

branch_id INT,

branch_name VARCHAR(100),

city VARCHAR(100),

state VARCHAR(100)

);

CREATE TABLE dim_date(

date_key INT PRIMARY KEY,

full_date DATE,

day INT,

month INT,

month_name VARCHAR(20),

quarter_no INT,

year INT,

week_no INT

);


CREATE TABLE fact_sales(

sales_key INT AUTO_INCREMENT PRIMARY KEY,

date_key INT,

customer_key INT,

product_key INT,

employee_key INT,

branch_key INT,

quantity INT,

sales_amount DECIMAL(12,2),

discount DECIMAL(10,2),

cost_amount DECIMAL(12,2),

profit DECIMAL(12,2),

FOREIGN KEY(date_key) REFERENCES dim_date(date_key),

FOREIGN KEY(customer_key) REFERENCES dim_customer(customer_key),

FOREIGN KEY(product_key) REFERENCES dim_product(product_key),

FOREIGN KEY(employee_key) REFERENCES dim_employee(employee_key),

FOREIGN KEY(branch_key) REFERENCES dim_branch(branch_key)

);


INSERT INTO dim_customer
(customer_id,customer_name,city,state,segment)

SELECT DISTINCT

customer_id,

customer_name,

city,

state,

segment

FROM stg_customers;



INSERT INTO dim_product
(product_id,product_name,category,brand,unit_cost)

SELECT DISTINCT

product_id,

product_name,

category,

brand,

unit_cost

FROM stg_products;



INSERT INTO dim_employee
(employee_id,employee_name,department,branch)

SELECT DISTINCT

employee_id,

employee_name,

department,

branch

FROM stg_employees;



INSERT INTO dim_branch
(branch_id,branch_name,city,state)

SELECT DISTINCT

branch_id,

branch_name,

city,

state

FROM stg_branches;


INSERT INTO dim_date

SELECT DISTINCT

DATE_FORMAT(sales_date,'%Y%m%d'),

sales_date,

DAY(sales_date),

MONTH(sales_date),

MONTHNAME(sales_date),

QUARTER(sales_date),

YEAR(sales_date),

WEEK(sales_date)

FROM stg_sales;


INSERT INTO fact_sales
(
date_key,
customer_key,
product_key,
employee_key,
branch_key,
quantity,
sales_amount,
discount,
cost_amount,
profit
)

SELECT

DATE_FORMAT(s.sales_date,'%Y%m%d'),

dc.customer_key,

dp.product_key,

de.employee_key,

db.branch_key,

s.quantity,

(s.quantity*s.unit_price),

s.discount,

(s.quantity*dp.unit_cost),

((s.quantity*s.unit_price)-s.discount-(s.quantity*dp.unit_cost))

FROM stg_sales s

JOIN dim_customer dc

ON s.customer_id=dc.customer_id

JOIN dim_product dp

ON s.product_id=dp.product_id

JOIN dim_employee de

ON s.employee_id=de.employee_id

JOIN dim_branch db

ON s.branch_id=db.branch_id;

-- Revenue

SELECT SUM(sales_amount)
FROM fact_sales;

-- Profit

SELECT SUM(profit)
FROM fact_sales;

-- Revenue By Branch

SELECT

b.branch_name,

SUM(f.sales_amount)

FROM fact_sales f

JOIN dim_branch b

ON f.branch_key=b.branch_key

GROUP BY b.branch_name;

-- Top Products

SELECT

p.product_name,

SUM(f.sales_amount) Revenue

FROM fact_sales f

JOIN dim_product p

ON f.product_key=p.product_key

GROUP BY p.product_name

ORDER BY Revenue DESC;

-- Top Customers

SELECT

c.customer_name,

SUM(f.sales_amount) Revenue

FROM fact_sales f

JOIN dim_customer c

ON f.customer_key=c.customer_key

GROUP BY c.customer_name

ORDER BY Revenue DESC;

-- Monthly Trend

SELECT

d.month_name,

SUM(f.sales_amount)

FROM fact_sales f

JOIN dim_date d

ON f.date_key=d.date_key

GROUP BY d.month_name;