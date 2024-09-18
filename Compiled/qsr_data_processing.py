import pandas as pd
import json
import os
from PySide6.QtWidgets import QMessageBox
import qsr_mail

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
            secs=seconds % 60
            return f"{hours:02}:{minutes:02}:{secs:02}"

        # Function to determine the status based on type and age
        def determine_status(type_value, age_seconds):
            if type_value in ['emails', 'armeq', 'maa', 'ltaeq', 'rcr', 'atoz']:
                if 64800 < age_seconds < 86400:
                    return "Need attention"
                elif age_seconds > 86400:
                    return "Missed"
            elif type_value in ['sgd', 'hrqsgd']:
                if 14400 < age_seconds < 36000:
                    return "Need attention"
                elif age_seconds > 36000:
                    return "missed"
            elif type_value in ['ri', 'hrqri','esc','armri']:
                if 28800 < age_seconds < 43200:
                    return "Need attention"
                elif age_seconds > 43200:
                    return "Missed"
            elif type_value in ['conc', 'hrqconc']:
                if 201600 < age_seconds < 259200:
                    return "Need attention"
                elif age_seconds > 259200:
                    return "Missed"
            elif type_value in ['acct', 'hrqacct']:
                if 345600 < age_seconds < 432000:
                    return "Need attention"
                elif age_seconds > 432000:
                    return "Missed"
            return "In control"

        # Iterate over each unique 'Type' value
        for t in merged_df['Type'].unique():
            type_data = merged_df[merged_df['Type'] == t]
            type_dict = {}

            # Iterate over each unique 'MP' value
            for mp in merged_df['MP'].unique():
                mp_data = type_data[type_data['MP'] == mp]
                
                if not mp_data.empty:
                    max_age_seconds = int(mp_data['Age'].max())
                    mp_dict = {
                        'count': int(mp_data['Count'].sum()),  # Convert to int
                        'age': seconds_to_hhmm(max_age_seconds),  # Convert seconds to HH:MM
                        'cluster': mp_data['cluster'].iloc[0],  # Assuming 'cluster' value is the same for each MP
                        'status': determine_status(t, max_age_seconds)  # Determine the status
                    }
                    type_dict[mp] = mp_dict

            result[t] = type_dict

        # Define the output file path
        output_file = 'output/output.json'
        
        # Remove the output file if it already exists
        if os.path.isfile(output_file):
            os.remove(output_file)

        # Output the result to a JSON file
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=4)
        
        QMessageBox.information(None, "Success", f"Output JSON file saved as {output_file}")
        qsr_mail.qsr_mail_prep()

    except Exception as e:
        QMessageBox.critical(None, "Error", f"An error occurred: {e}")

