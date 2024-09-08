from PySide6.QtWidgets import QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from file_utils import load_file
from qsr_data_processing import merge_and_process_data
from email_window import EmailWindow  # Import the new EmailWindow class
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Spacer to push items to the top
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_top)

        # Label
        self.label = QLabel("Select the QSR and Prepare Email")
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Curved Button
        self.curved_button = QPushButton("QSR Prep")
        self.curved_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 15px;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.curved_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.curved_button.clicked.connect(self.on_button_click)

        # Email Window Button
        self.email_button = QPushButton("Quick Move", self)
        self.email_button.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 15px;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        layout.addWidget(self.email_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.email_button.clicked.connect(self.open_email_window)

        # Spacer to push items down to top-center
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_bottom)
        self.label = QLabel("Created by Nikhil (sinnikhy)")
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Main window configuration
        self.setLayout(layout)
        self.setWindowTitle('WFM Tool')
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #f9f9f9;")

    def on_button_click(self):
        # Existing functionality
        script_dir = os.path.dirname(os.path.abspath(__file__))
        type_dict_file = os.path.join(script_dir, 'assets/typedict.csv')

        if not os.path.isfile(type_dict_file):
            QMessageBox.critical(self, "Error", f"TypeDict file not found: {type_dict_file}")
            return

        # Load the Data CSV file
        data_file = load_file('data')
        if not data_file:
            QMessageBox.critical(self, "Error", "Data file not selected.")
            return

        # Merge and process the data, and save to output JSON
        merge_and_process_data(data_file, type_dict_file)

    def open_email_window(self):
        self.email_window = EmailWindow()
        self.email_window.show()
