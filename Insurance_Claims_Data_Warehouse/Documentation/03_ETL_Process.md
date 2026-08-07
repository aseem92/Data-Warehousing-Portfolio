# ETL Process

## Overview

The ETL pipeline automates loading raw insurance data into the analytical warehouse.

---

## Step 1

Generate Sample Data

Python Script

01_generate_sample_data.py

Output

CSV Files

---

## Step 2

Load CSV Files

Python Script

02_load_etl.py

Purpose

Load raw CSV files into staging tables.

---

## Step 3

Load into MySQL

Python Script

03_load_etl_mysql.py

Purpose

Populate Dimension and Fact tables.

---

## Step 4

Database Validation

Python Script

04_check_db.py

Purpose

Verify successful loading.

---

## ETL Workflow

CSV

↓

Staging

↓

Transformation

↓

Dimensions

↓

Fact Table

↓

Power BI
