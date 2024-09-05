import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os

def load_file(file_type):
    """Load a CSV file using a file dialog and return the file path."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    if file_type == 'data':
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")],
            title="Select Data CSV File"
        )
    else:
        raise ValueError("Unknown file type specified.")
    
    return file_path

def merge_and_process_data(data_file, type_dict_file):
    """Merge data from data_file with type_dict_file and process the merged data."""
    try:
        # Load TypeDict data
        type_dict_df = pd.read_csv(type_dict_file)
        if 'Queue' not in type_dict_df.columns:
            raise ValueError("TypeDict file must contain 'Queue' column.")

        # Load Data data
        data_df = pd.read_csv(data_file)
        if 'Queue' not in data_df.columns:
            raise ValueError("Data file must contain 'Queue' column.")
        
        # Merge Data with TypeDict based on the 'Queue' column
        merged_df = pd.merge(data_df, type_dict_df, on='Queue', how='left')
        
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
        for t in merged_df['Type'].unique():
            type_data = merged_df[merged_df['Type'] == t]
            type_dict = {}

            # Iterate over each unique 'MP' value
            for mp in merged_df['MP'].unique():
                mp_data = type_data[type_data['MP'] == mp]
                
                if not mp_data.empty:
                    mp_dict = {
                        'count': int(mp_data['Count'].sum()),  # Convert to int
                        'age': seconds_to_hhmm(int(mp_data['Age'].max())),  # Convert seconds to HH:MM
                        'cluster': mp_data['cluster'].iloc[0]  # Assuming 'cluster' value is the same for each MP
                    }
                    type_dict[mp] = mp_dict

            result[t] = type_dict

        # Define the output file path
        output_file = 'output.json'
        
        # Remove the output file if it already exists
        if os.path.isfile(output_file):
            os.remove(output_file)

        # Output the result to a JSON file
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=4)
        
        messagebox.showinfo("Success", f"Output JSON file saved as {output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    """Main function to handle the merging and processing process."""
    # Determine the path to the typedict.csv file in the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    type_dict_file = os.path.join(script_dir, 'typedict.csv')

    if not os.path.isfile(type_dict_file):
        messagebox.showerror("Error", f"TypeDict file not found: {type_dict_file}")
        return

    # Load the Data CSV file
    data_file = load_file('data')
    if not data_file:
        messagebox.showerror("Error", "Data file not selected.")
        return

    # Merge and process the data, and save to output JSON
    merge_and_process_data(data_file, type_dict_file)

if __name__ == "__main__":
    # Create a Tkinter window
    root = tk.Tk()
    root.title("how dare you open me ")
    root.geometry("300x150")

    # Add a button to start the process
    button = tk.Button(root, text="I dare you to press me", command=main)
    button.pack(expand=True)

    root.mainloop()
