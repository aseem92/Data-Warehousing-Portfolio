# System Architecture

## Overview

The solution follows a traditional Data Warehousing architecture consisting of Data Sources, ETL Layer, Data Warehouse, and Reporting Layer.

---

## Architecture Flow

CSV Files

↓

Python ETL Scripts

↓

MySQL Data Warehouse

↓

Power BI Dashboard

---

## Components

### Data Sources

- policy_holders.csv
- policies.csv
- drivers.csv
- claims.csv

### ETL Layer

Python scripts automate:

- Data generation
- Data loading
- Data validation
- Data transformation

### Data Warehouse

MySQL stores

- Staging Tables
- Dimension Tables
- Fact Table

### Reporting Layer

Power BI provides interactive dashboards for business users.

---

## Architecture Diagram

Insurance_warehouse_daigram.png
