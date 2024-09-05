import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

def load_file(file_type):
    """Load a CSV file using a file dialog and return the file path."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    if file_type == 'data':
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")], title="Select Data CSV File")
    else:
        raise ValueError("Unknown file type.")
    return file_path

def merge_data(data_file, type_dict_file, output_file):
    """Merge data from data_file and type_dict_file and save to output_file."""
    # Load TypeDict data
    type_dict_df = pd.read_csv(type_dict_file)
    
    # Load Data data
    data_df = pd.read_csv(data_file)
    
    # Merge Data with TypeDict based on the 'queue' column
    merged_df = pd.merge(data_df, type_dict_df, on='Queue', how='left')
    
    # Check if the output file already exists and delete it if it does
    if os.path.isfile(output_file):
        os.remove(output_file)
    
    # Save the merged DataFrame to the output CSV file
    merged_df.to_csv(output_file, index=False)
    messagebox.showinfo("Success", f"File saved as {output_file}")

def main():
    # Determine the path to the typedict.csv file in the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    type_dict_file = os.path.join(script_dir, 'typedict.csv')

    if not os.path.isfile(type_dict_file):
        messagebox.showerror("Error", f"{type_dict_file} not found.")
        return

    # Load the Data CSV file
    data_file = load_file('data')
    if not data_file:
        messagebox.showerror("Error", "Data file not selected.")
        return

    # Define the output file path
    output_file = os.path.join(script_dir, "merged_data.csv")

    # Merge the data and save to output file
    merge_data(data_file, type_dict_file, output_file)

if __name__ == "__main__":
    # Create a Tkinter window
    root = tk.Tk()
    root.title("CSV Merger")
    root.geometry("300x150")

    # Add a button to start the process
    button = tk.Button(root, text="Load and Merge CSV Files", command=main)
    button.pack(expand=True)

    root.mainloop()
