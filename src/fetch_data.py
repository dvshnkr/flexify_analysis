import os
from config import get_data_path

# Get the full path to the raw data file
data_dir = get_data_path()
print(data_dir)

# os walk
for dirpath, dirnames, filenames in os.walk(data_dir):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
