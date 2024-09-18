from PySide6.QtWidgets import QWidget, QPushButton, QMessageBox, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt
from file_utils import load_file
from qsr_data_processing import merge_and_process_data
import os
import qsr_mail
import invqsr_mail
import armriqsr_mail 
import escqsr_mail # Import the invqsr module

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
        self.label = QLabel(f"welcome {os.getlogin()}")
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

        
        
        # New INVQSR Button
        self.invqsr_button = QPushButton("INVQSR", self)
        self.invqsr_button.setStyleSheet("""
            QPushButton {
                background-color: #FFC107;
                color: white;
                border-radius: 15px;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #ffca28;
            }
        """)
        layout.addWidget(self.invqsr_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.invqsr_button.clicked.connect(self.run_invqsr)

        # ESCQSR Button
        self.escqsr_button = QPushButton("ESCQSR", self)
        self.escqsr_button.setStyleSheet("""
            QPushButton {
                background-color: #FF5722;
                color: white;
                border-radius: 15px;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #e64a19;
            }
        """)
        layout.addWidget(self.escqsr_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.escqsr_button.clicked.connect(self.run_escqsr)

        # ARMRIQSR Button
        self.armriqsr_button = QPushButton("ARMRIQSR", self)
        self.armriqsr_button.setStyleSheet("""
            QPushButton {
                background-color: #9C27B0;
                color: white;
                border-radius: 15px;
                padding: 10px 20px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #7b1fa2;
            }
        """)
        layout.addWidget(self.armriqsr_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.armriqsr_button.clicked.connect(self.run_armriqsr)

        # Spacer to push items down to top-center
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer_bottom)
        self.label = QLabel("Created by Nikhil (sinnikhy)")
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Main window configuration
        self.setLayout(layout)
        self.setWindowTitle('QSR Tool')
        self.setGeometry(100, 100, 400, 400)  # Increased height to accommodate new buttons
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
        qsr_mail.qsr_mail_prep()


    def run_invqsr(self):
        try:
            invqsr_mail.invqsr_mail_prep()  # Call the invqsr_mail function from invqsr.py
           
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def run_escqsr(self):
        # Implement the functionality for ESCQSR here
        try:
            # Placeholder for ESCQSR functionality
            escqsr_mail.escqsr_mail_prep()  # Call the invqsr_mail function from invqsr.py
            # QMessageBox.information(self, "Info", "ESCQSR process completed.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

    def run_armriqsr(self):
        # Implement the functionality for ARMRIQSR here
        try:
            armriqsr_mail.armriqsr_mail_prep()  # Call the invqsr_mail function from invqsr.py
        
            # Placeholder for ARMRIQSR functionality
            # QMessageBox.information(self, "Info", "ARMRIQSR process completed.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")
