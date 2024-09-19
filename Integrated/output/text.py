import json

def sum_counts(json_data):
    result = {}
    
    for key in json_data.keys():
        total_count = sum(region['count'] for region in json_data[key].values())
        result[key] = total_count
        
    return result

# Load JSON data from a file
with open('output.json', 'r') as file:
    json_data = json.load(file)

result = sum_counts(json_data)
print(result)
