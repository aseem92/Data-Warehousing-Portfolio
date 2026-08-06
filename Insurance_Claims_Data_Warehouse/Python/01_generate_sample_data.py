import csv
import os
import random
from datetime import datetime, timedelta

# Config
USER_DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")
OUT_DIR = os.path.join(USER_DESKTOP, "etl_sources")
os.makedirs(OUT_DIR, exist_ok=True)

NUM_POLICY_HOLDERS = 200
NUM_POLICIES = 200
NUM_DRIVERS = 300
NUM_CLAIMS = 400

first_names = ["John","Jane","Michael","Michelle","Robert","Linda","David","Susan","James","Patricia","William","Barbara","Richard","Elizabeth"]
last_names = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez"]
policy_types = ["Auto","Home","Life","Commercial"]
claim_types = ["Collision","Theft","Liability","Fire","Weather"]
claim_status = ["Open","Closed","Denied","Settled"]

def rand_name():
    return random.choice(first_names), random.choice(last_names)

def write_policy_holders(path):
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["policy_holder_id","first_name","last_name","dob","address","phone","email"]) 
        for i in range(1, NUM_POLICY_HOLDERS+1):
            fn, ln = rand_name()
            dob = (datetime.today() - timedelta(days=random.randint(25*365,80*365))).date().isoformat()
            address = f"{random.randint(100,9999)} {random.choice(['Main St','Oak Ave','Pine Rd','Maple Blvd'])}, City"
            phone = f"+1-202-{random.randint(200,999):03d}-{random.randint(1000,9999):04d}"
            email = f"{fn.lower()}.{ln.lower()}{i}@example.com"
            writer.writerow([i,fn,ln,dob,address,phone,email])

def write_policies(path):
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["policy_id","policy_number","policy_holder_id","effective_date","expiration_date","policy_type","premium_amount"]) 
        for i in range(1, NUM_POLICIES+1):
            policy_number = f"P-{20260000 + i}"
            holder = random.randint(1, NUM_POLICY_HOLDERS)
            eff = (datetime.today() - timedelta(days=random.randint(0,365))).date()
            exp = (eff + timedelta(days=365)).isoformat()
            eff = eff.isoformat()
            ptype = random.choice(policy_types)
            premium = round(random.uniform(200.0, 5000.0),2)
            writer.writerow([i,policy_number,holder,eff,exp,ptype,premium])

def write_drivers(path):
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["driver_id","policy_id","first_name","last_name","dob","license_number","relationship"]) 
        for i in range(1, NUM_DRIVERS+1):
            policy = random.randint(1, NUM_POLICIES)
            fn, ln = rand_name()
            dob = (datetime.today() - timedelta(days=random.randint(18*365,75*365))).date().isoformat()
            lic = f"D{random.randint(1000000,9999999)}"
            rel = random.choice(["Self","Spouse","Child","Other"]) 
            writer.writerow([i,policy,fn,ln,dob,lic,rel])

def write_claims(path):
    with open(path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["claim_id","policy_id","claim_date","claim_type","amount","status","description"]) 
        for i in range(1, NUM_CLAIMS+1):
            policy = random.randint(1, NUM_POLICIES)
            claim_date = (datetime.today() - timedelta(days=random.randint(0,900))).date().isoformat()
            ctype = random.choice(claim_types)
            amount = round(random.uniform(250.0, 50000.0),2)
            status = random.choice(claim_status)
            desc = f"{ctype} claim for policy {policy}"
            writer.writerow([i,policy,claim_date,ctype,amount,status,desc])

def main():
    print("Writing sample CSVs to", OUT_DIR)
    write_policy_holders(os.path.join(OUT_DIR, "policy_holders.csv"))
    write_policies(os.path.join(OUT_DIR, "policies.csv"))
    write_drivers(os.path.join(OUT_DIR, "drivers.csv"))
    write_claims(os.path.join(OUT_DIR, "claims.csv"))
    print("Done.")

if __name__ == '__main__':
    main()