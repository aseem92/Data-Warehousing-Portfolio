import os
import sys
import hashlib
import mysql.connector

DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "insurance_dw"
DB_USER = "root"
DB_PASSWORD = "YOUR_PASSWORD"

SOURCE_DIR = os.path.join(
    os.path.expanduser("~"),
    "Desktop",
    "etl_sources"
)