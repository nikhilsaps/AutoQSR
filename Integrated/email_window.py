from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QLabel
from PySide6.QtCore import Qt
import webbrowser
import re

class EmailWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Label
        self.label = QLabel("Enter email addresses (comma or space-separated):")
        layout.addWidget(self.label)

        # Text box
        self.text_box = QLineEdit(self)
        layout.addWidget(self.text_box)

        # Buttons
        self.na_button = QPushButton("Move to NA", self)
        self.eu_button = QPushButton("Move to EU", self)
        self.fe_button = QPushButton("Move to FE", self)

        # Style buttons
        self.style_buttons([self.na_button, self.eu_button, self.fe_button])

        layout.addWidget(self.na_button)
        layout.addWidget(self.eu_button)
        layout.addWidget(self.fe_button)

        # Connect buttons to methods
        self.na_button.clicked.connect(lambda: self.open_outlook("NA"))
        self.eu_button.clicked.connect(lambda: self.open_outlook("EU"))
        self.fe_button.clicked.connect(lambda: self.open_outlook("FE"))

        # Main window configuration
        self.setLayout(layout)
        self.setWindowTitle('Generate Outlook Email')
        self.setGeometry(200, 200, 400, 300)
        self.setStyleSheet("background-color: #f9f9f9;")

    def style_buttons(self, buttons):
        for button in buttons:
            button.setStyleSheet("""
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

    def open_outlook(self, region):
        text = self.text_box.text().strip()

        if not text:
            QMessageBox.warning(self, "Input Error", "Please enter some email addresses.")
            return

        # Clean up the input: replace multiple spaces with a single space and then convert to comma-separated
        cleaned_text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
        emails = [email.strip() for email in cleaned_text.replace(' ', ',').split(',')]

        # Create the 'mailto' URL
        to_addresses = ",".join(f"{email}@amazon.com" for email in emails)
        cc_address = "ari-rtm@amazon.com"

        if region == "NA":
            subject = "Kindly flip to NA"
            body = (
                "Hi all,%0A%0A"
                "Please move to NA.%0A%0A"
                "Note: This mail is being monitored.%0A%0A"
                "Best regards,%0A"
                "sinnikhy@amazon.com"
            )
        elif region == "EU":
            subject = "Kindly flip to EU"
            body = (
                "Hi all,%0A%0A"
                "Please move to EU.%0A%0A"
                "Note: This mail is being monitored.%0A%0A"
                "Best regards,%0A"
                "sinnikhy@amazon.com"
            )
        elif region == "FE":
            subject = "Kindly flip to FE"
            body = (
                "Hi all,%0A%0A"
                "Please move to FE.%0A%0A"
                "Note: This mail is being monitored.%0A%0A"
                "Best regards,%0A"
                "sinnikhy@amazon.com"
            )
        else:
            QMessageBox.warning(self, "Region Error", "Invalid region selected.")
            return

        mailto_url = (
            f"mailto:{to_addresses}?cc={cc_address}&subject={subject}&body={body}"
        )

        # Open the default email client
        webbrowser.open(mailto_url)
