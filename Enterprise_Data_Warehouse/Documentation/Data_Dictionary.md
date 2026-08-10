# Data Dictionary

## Dimension Tables

### dim_customer

| Column | Description |
|---------|-------------|
| customer_key | Surrogate Key |
| customer_id | Business Key |
| customer_name | Customer Name |
| city | Customer City |
| state | Customer State |
| segment | Customer Segment |

---

### dim_product

| Column | Description |
|---------|-------------|
| product_key | Surrogate Key |
| product_id | Product ID |
| product_name | Product Name |
| category | Product Category |
| brand | Product Brand |
| unit_cost | Unit Cost |

---

### dim_employee

| Column | Description |
|---------|-------------|
| employee_key | Surrogate Key |
| employee_id | Employee ID |
| employee_name | Employee Name |
| department | Department |
| branch | Assigned Branch |

---

### dim_branch

| Column | Description |
|---------|-------------|
| branch_key | Surrogate Key |
| branch_id | Branch ID |
| branch_name | Branch Name |
| city | Branch City |
| state | Branch State |

---

### dim_date

| Column | Description |
|---------|-------------|
| date_key | Date Key |
| full_date | Calendar Date |
| day | Day |
| month | Month |
| month_name | Month Name |
| quarter_no | Quarter |
| year | Year |
| week_no | Week Number |

---

## Fact Table

### fact_sales

| Column | Description |
|---------|-------------|
| sales_key | Surrogate Key |
| date_key | Date Dimension Key |
| customer_key | Customer Dimension Key |
| product_key | Product Dimension Key |
| employee_key | Employee Dimension Key |
| branch_key | Branch Dimension Key |
| quantity | Quantity Sold |
| sales_amount | Revenue |
| discount | Discount |
| cost_amount | Product Cost |
| profit | Profit |
