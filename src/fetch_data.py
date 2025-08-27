import os
import sqlite3
import pandas as pd
from config import get_data_path

# Get the full path to the raw data file
data_file = get_data_path("raw", "flexify.sqlite")

# Connect to a database file named 'example.db'
with sqlite3.connect(data_file) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table in tables:
        print(f"Printing head of the `{table[0]}` table:")
        df = pd.read_sql_query(f"SELECT * FROM {table[0]}", conn)
        print(df.head())
        print("\n\n")
