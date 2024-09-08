# file_utils.py
from PySide6.QtWidgets import QFileDialog

def load_file(file_type):
    """Load a CSV file using a file dialog and return the file path."""
    file_dialog = QFileDialog()
    if file_type == 'data':
        file_path, _ = file_dialog.getOpenFileName(
            caption="Select Data CSV File",
            filter="CSV files (*.csv)"
        )
    else:
        raise ValueError("Unknown file type specified.")
    
    return file_path
