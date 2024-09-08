import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv')

# Function to extract country code
def extract_country_code(queue):
    parts = queue.split('_')
    if len(parts) > 1 and parts[1] != 'trms':
        return parts[1]
    return ''

# Add the new column with country codes
df['mp'] = df['Queue'].apply(extract_country_code)

# Print the modified DataFrame to verify
print("Modified DataFrame with 'mp' column:")
print(df)

# Save the modified DataFrame to a new CSV file
df.to_csv('modified_data.csv', index=False)
print("\nModified DataFrame has been saved to 'modified_data.csv'")
