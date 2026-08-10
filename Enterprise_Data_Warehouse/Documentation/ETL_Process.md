# ETL Process

## Overview

The ETL process transforms raw CSV files into an optimized analytical data warehouse.

---

## Extract

Data is generated using Python and exported as CSV files.

Datasets include:

- Customers
- Products
- Employees
- Branches
- Sales

---

## Transform

The transformation stage performs:

- Data cleansing
- Duplicate removal
- Surrogate key generation
- Date dimension creation
- Revenue calculation
- Cost calculation
- Profit calculation

---

## Load

The processed data is loaded into:

### Dimension Tables

- dim_customer
- dim_product
- dim_employee
- dim_branch
- dim_date

### Fact Table

- fact_sales

---

## ETL Flow

CSV Files

↓

Staging Tables

↓

Dimension Tables

↓

Fact Table

↓

Power BI

---

## Benefits

- Faster reporting
- Centralized analytics
- Consistent business metrics
- Optimized query performance
