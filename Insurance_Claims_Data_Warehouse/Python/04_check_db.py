import os
import psycopg2

DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = int(os.getenv('DB_PORT', '5432'))
DB_NAME = os.getenv('DB_NAME', 'insurance')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'admin')

def q(cur, sql):
    cur.execute(sql)
    return cur.fetchall()

def main():
    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
    cur = conn.cursor()

    tables = [
        ('staging.policy_holder','staging'),
        ('staging.policy','staging'),
        ('staging.driver','staging'),
        ('staging.claim','staging'),
        ('dw.dim_policy_holder','dw'),
        ('dw.dim_policy','dw'),
        ('dw.dim_driver','dw'),
        ('dw.fact_claim','dw')
    ]

    print(f"Connected to {DB_HOST}:{DB_PORT}/{DB_NAME} as {DB_USER}\n")
    for tbl, schema in tables:
        try:
            cur.execute(f"SELECT count(*) FROM {tbl}")
            cnt = cur.fetchone()[0]
            print(f"{tbl}: {cnt} rows")
            if cnt>0:
                cur.execute(f"SELECT * FROM {tbl} LIMIT 1")
                print(' sample:', cur.fetchone())
        except Exception as e:
            print(f"{tbl}: ERROR - {e}")

    cur.close()
    conn.close()

if __name__=='__main__':
    main()
