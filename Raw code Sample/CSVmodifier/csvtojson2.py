import pandas as pd
import json

# Load the CSV data
df = pd.read_csv('merged_data.csv')

# Initialize the result dictionary
result = {}

# Function to convert seconds to HH:MM format
def seconds_to_hhmm(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours:02}:{minutes:02}"

# Function to convert numpy types to native Python types
def convert_types(value):
    if isinstance(value, (pd.NA, float, int, str)):
        return value
    if hasattr(value, 'tolist'):
        return value.tolist()
    return str(value)

# Iterate over each unique 'Type' value
for t in df['Type'].unique():
    type_data = df[df['Type'] == t]
    type_dict = {}
    
    # Iterate over each unique 'MP' value
    for mp in df['MP'].unique():
        mp_data = type_data[type_data['MP'] == mp]
        
        if not mp_data.empty:
            mp_dict = {
                'count': int(mp_data['Count'].sum()),  # Convert to int
                'age': seconds_to_hhmm(int(mp_data['Age'].max())),  # Convert seconds to HH:MM
                'cluster': mp_data['cluster'].iloc[0]  # Assuming 'cluster' value is the same for each MP
            }
            type_dict[mp] = mp_dict
    
    result[t] = type_dict

# Output the result to a JSON file
with open('output.json', 'w') as f:
    json.dump(result, f, indent=4)
