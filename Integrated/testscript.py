import os
import pandas as pd
import time
import subprocess
import dummy
# Path to your Downloads folder
downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')

# Path to the script you want to execute if a valid CSV is found
script_to_execute = '\dummy.py'

def find_latest_csv():
    latest_file = None
    latest_time = 0
    
    # Iterate over files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(downloads_folder, filename)
            file_mod_time = os.path.getmtime(file_path)

            if file_mod_time > latest_time:
                latest_time = file_mod_time
                latest_file = file_path

    return latest_file

def check_csv_file(file_path):
    try:
        # Read the first row of the CSV file
        df = pd.read_csv(file_path, nrows=0)
        if list(df.columns) == ['Queue', 'Count', 'Age']:
            return True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False

while True:
    latest_csv = find_latest_csv()
    
    if latest_csv and check_csv_file(latest_csv):
        
        print(f"Found valid CSV file: {latest_csv}")
        dummy.teste()
    
    # Wait for one hour
    time.sleep(100)
