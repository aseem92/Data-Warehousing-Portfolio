
import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker

# -----------------------------
# Configuration
# -----------------------------

fake = Faker()
random.seed(42)
np.random.seed(42)

# Project folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Data")

os.makedirs(DATA_DIR, exist_ok=True)

# Number of records
NUM_CUSTOMERS = 2000
NUM_PRODUCTS = 500
NUM_EMPLOYEES = 150
NUM_BRANCHES = 25
NUM_SALES = 50000

# -----------------------------
# Branch Data
# -----------------------------

branch_cities = [
    ("Delhi", "Delhi"),
    ("Mumbai", "Maharashtra"),
    ("Bangalore", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Chennai", "Tamil Nadu"),
    ("Pune", "Maharashtra"),
    ("Kolkata", "West Bengal"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"),
    ("Indore", "Madhya Pradesh"),
    ("Bhopal", "Madhya Pradesh"),
    ("Nagpur", "Maharashtra"),
    ("Chandigarh", "Chandigarh"),
    ("Surat", "Gujarat"),
    ("Raipur", "Chhattisgarh"),
    ("Jabalpur", "Madhya Pradesh"),
    ("Patna", "Bihar"),
    ("Kochi", "Kerala"),
    ("Bhubaneswar", "Odisha"),
    ("Noida", "Uttar Pradesh"),
    ("Gurgaon", "Haryana"),
    ("Visakhapatnam", "Andhra Pradesh"),
    ("Coimbatore", "Tamil Nadu"),
    ("Mysore", "Karnataka")
]

branches = []

for i, (city, state) in enumerate(branch_cities[:NUM_BRANCHES], start=1):
    branches.append({
        "branch_id": i,
        "branch_name": f"{city} Branch",
        "city": city,
        "state": state
    })

branches_df = pd.DataFrame(branches)

# -----------------------------
# Product Data
# -----------------------------

categories = {
    "Electronics": ["Laptop", "Smartphone", "Tablet", "Monitor", "Keyboard"],
    "Furniture": ["Office Chair", "Desk", "Cabinet", "Conference Table", "Bookshelf"],
    "Appliances": ["Refrigerator", "Microwave", "Washing Machine", "Air Conditioner", "Water Purifier"],
    "Office Supplies": ["Printer", "Notebook", "Pen Pack", "Paper Ream", "Whiteboard"],
    "Accessories": ["Headphones", "Mouse", "USB Drive", "Webcam", "Power Bank"]
}

brands = [
    "TechPro",
    "Nova",
    "Elite",
    "Prime",
    "Vision",
    "Apex",
    "SmartLine",
    "CoreX",
    "MaxOne",
    "Fusion"
]

products = []

product_id = 1

for category, items in categories.items():
    for item in items:
        for _ in range(20):
            products.append({
                "product_id": product_id,
                "product_name": f"{random.choice(brands)} {item}",
                "category": category,
                "brand": random.choice(brands),
                "unit_cost": round(random.uniform(500, 50000), 2)
            })
            product_id += 1

products_df = pd.DataFrame(products)

# -----------------------------
# Customer Data
# -----------------------------

segments = ["Retail", "Corporate", "Wholesale", "Government"]

customers = []

for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": i,
        "customer_name": fake.company(),
        "city": fake.city(),
        "state": fake.state(),
        "segment": random.choice(segments)
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# Employee Data
# -----------------------------

departments = [
    "Sales",
    "Marketing",
    "Finance",
    "Customer Support",
    "Operations"
]

employees = []

for i in range(1, NUM_EMPLOYEES + 1):
    employees.append({
        "employee_id": i,
        "employee_name": fake.name(),
        "department": random.choice(departments),
        "branch": random.choice(branches)["branch_name"]
    })

employees_df = pd.DataFrame(employees)

# -----------------------------
# Sales Data
# -----------------------------

sales = []

start_date = datetime(2024, 1, 1)

for i in range(1, NUM_SALES + 1):

    sale_date = start_date + timedelta(days=random.randint(0, 730))

    customer = random.randint(1, NUM_CUSTOMERS)

    product = random.randint(1, len(products_df))

    employee = random.randint(1, NUM_EMPLOYEES)

    branch = random.randint(1, NUM_BRANCHES)

    quantity = random.randint(1, 10)

    unit_price = round(random.uniform(1000, 60000), 2)

    discount = round(random.uniform(0, unit_price * 0.20), 2)

    sales.append({
        "sales_id": i,
        "sales_date": sale_date.date(),
        "customer_id": customer,
        "product_id": product,
        "employee_id": employee,
        "branch_id": branch,
        "quantity": quantity,
        "unit_price": unit_price,
        "discount": discount
    })

sales_df = pd.DataFrame(sales)

# -----------------------------
# Export CSV Files
# -----------------------------

branches_df.to_csv(
    os.path.join(DATA_DIR, "branches.csv"),
    index=False
)

customers_df.to_csv(
    os.path.join(DATA_DIR, "customers.csv"),
    index=False
)

products_df.to_csv(
    os.path.join(DATA_DIR, "products.csv"),
    index=False
)

employees_df.to_csv(
    os.path.join(DATA_DIR, "employees.csv"),
    index=False
)

sales_df.to_csv(
    os.path.join(DATA_DIR, "sales.csv"),
    index=False
)

print("=" * 50)
print("Enterprise Data Generated Successfully!")
print("=" * 50)
print(f"Customers : {len(customers_df)}")
print(f"Products  : {len(products_df)}")
print(f"Employees : {len(employees_df)}")
print(f"Branches  : {len(branches_df)}")
print(f"Sales     : {len(sales_df)}")
print(f"\nCSV files saved to:\n{DATA_DIR}")

if __name__ == "__main__":
    pass