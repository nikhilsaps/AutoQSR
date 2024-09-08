import pandas as pd
import json

# Read CSV data into a DataFrame
df = pd.read_csv('merged_data.csv')

# Initialize an empty dictionary to store the JSON structure
json_data = {}

# Iterate through the rows of the DataFrame
for _, row in df.iterrows():
    type_ = row['Type']
    
    # Ensure the type key exists in the dictionary
    if type_ not in json_data:
        json_data[type_] = {}
    
    # Add the queue details under the specific type
    json_data[type_][row['Queue']] = {
        'Age': row['Age'],
        'Count': row['Count'],
        'Cluster': row['cluster'],
        'MP': row['MP']
    }

# Convert the dictionary to JSON
json_output = json.dumps(json_data, indent=4)

# Optionally, save the JSON to a file
with open('output.json', 'w') as f:
    f.write(json_output)

print("CSV has been converted to JSON format and saved as 'output.json'")
