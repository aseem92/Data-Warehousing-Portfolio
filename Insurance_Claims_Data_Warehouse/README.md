# 🛡 Insurance Claims Data Warehouse

## 📌 Project Overview

The Insurance Claims Data Warehouse is an end-to-end dimensional modeling project designed to transform operational insurance data into an analytical repository for business reporting and decision-making.

The project demonstrates the complete Data Warehousing lifecycle, including data modeling, ETL, dimensional design, and SQL-based analytical reporting.

---

# 🎯 Business Problem

Insurance companies generate large amounts of operational data from policies, customers, claims, and drivers. Transactional databases are optimized for daily operations but are inefficient for reporting and analytics.

The objective of this project is to build a Data Warehouse that enables business users to analyze:

- Claim trends
- Policy performance
- Customer insights
- Claim settlement analysis
- Business KPIs

---

# 🏗 Architecture

```
                Source Data (CSV)

                       │

                       ▼

               Staging Database

                       │

                       ▼

               Python ETL Process

                       │

                       ▼

            Data Warehouse (Star Schema)

                       │

                       ▼

             SQL Analytics & Reporting
```

---

# ⭐ Features

- End-to-End ETL Pipeline
- Dimensional Modeling
- Star Schema Design
- Fact & Dimension Tables
- SQL Analytical Queries
- Business KPI Reporting
- Clean Folder Organization

---

# 🛠 Tech Stack

- MySQL
- SQL
- Python
- Pandas
- Data Warehousing
- ETL
- Git
- GitHub

---

# 📂 Project Structure

```
Insurance_Claims_Data_Warehouse

│
├── Data
├── SQL
├── Python
├── ETL
├── Documentation
├── Diagrams
├── Screenshots
├── Presentation
└── README.md
```

---

# 📊 Star Schema

The warehouse follows a **Star Schema** architecture.

### Dimension Tables

- Policy Holder
- Policy
- Driver
- Date

### Fact Table

- Claims

---

# 🔄 ETL Workflow

1. Extract raw insurance data
2. Load data into staging tables
3. Clean and validate data
4. Transform into dimensional model
5. Load into fact and dimension tables
6. Perform analytical reporting

---

# 📈 Sample Business Questions

- Which policy type generates the highest number of claims?
- Which customers file the most claims?
- What is the average claim amount?
- Claim trends by month
- Driver-wise claim analysis

---

# 🎓 Skills Demonstrated

- Data Warehousing
- ETL Development
- SQL Development
- Python Automation
- Star Schema Design
- Data Modeling
- Business Intelligence
- Analytical Query Writing

---

# 🚀 Future Improvements

- Incremental ETL
- Slowly Changing Dimensions (SCD Type 2)
- Power BI Dashboard
- Data Quality Validation
- Cloud Data Warehouse Implementation

---

## 👨‍💻 Author

**Aseem Gulati**

Data Analyst | SQL | Python | ETL | Data Warehousing | Power BI
