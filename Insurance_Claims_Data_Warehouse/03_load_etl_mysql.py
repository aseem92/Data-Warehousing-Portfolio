import os
import pandas as pd
from sqlalchemy import create_engine

# MySQL Connection
engine = create_engine(
    "mysql+pymysql://root:root123@127.0.0.1:3306/insurance_dw"
)

source_dir = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "etl_sources"
)

files = {
    "policy_holders.csv": "staging_policy_holder",
    "policies.csv": "staging_policy",
    "drivers.csv": "staging_driver",
    "claims.csv": "staging_claim"
}

for file_name, table_name in files.items():

    file_path = os.path.join(source_dir, file_name)

    print(f"Loading {file_name} into {table_name}")

    df = pd.read_csv(file_path)

    # Clear existing staging data
    with engine.begin() as conn:
        conn.exec_driver_sql(f"TRUNCATE TABLE {table_name}")

    # Insert CSV into MySQL
    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} rows")

print("✅ All staging tables loaded successfully!")

with open(
    r"C:\Users\aseem\Downloads\archive\transform.sql",
    "r",
    encoding="utf-8"
) as f:
    transform_sql = f.read()

with engine.begin() as conn:
    for statement in transform_sql.split(";"):
        if statement.strip():
            conn.exec_driver_sql(statement)

print("✅ Transform completed")