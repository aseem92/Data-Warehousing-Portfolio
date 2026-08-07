# Data Model

## Fact Table

### fact_claim

Stores insurance claim transactions.

Columns include

- claim_id
- policy_id
- claim_date
- claim_type
- amount
- status

---

## Dimension Tables

### dim_policy

Stores insurance policy information.

### dim_policy_holder

Stores customer information.

### dim_driver

Stores insured driver information.

---

## Staging Tables

- staging_policy
- staging_policy_holder
- staging_driver
- staging_claim

These tables temporarily store raw data before transformation.

---

## Model Type

Star Schema
