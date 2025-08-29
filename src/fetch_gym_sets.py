import os
import sqlite3
import pandas as pd
from config import get_data_path
from pathlib import Path

# Get the full path to the raw data file
raw_data_path = get_data_path("raw")
raw_data_file = raw_data_path / "flexify.sqlite"

# Connect to a database file named 'example.db'
with sqlite3.connect(raw_data_file) as conn:
    df = pd.read_sql_query("SELECT * FROM gym_sets", conn)

gym_sets_path = get_data_path("fetched") / "gym_sets.csv"
gym_sets_path.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(gym_sets_path, index=False)
