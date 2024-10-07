from PyQt5.QtWidgets import QVBoxLayout, QLabel, QTextBrowser, QCheckBox
from PyQt5.QtCore import Qt
from panels.base_panel import BasePanel

class LicenseAgreementPanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__("License Agreement", "Please read and accept the license agreement.", parent)
        
        # Additional layout for License Agreement
        layout = self.layout()  # Get the existing layout
        
        # Text Browser to display license text
        self.license_browser = QTextBrowser(self)
        self.load_license_text()  # Load the content of license.txt file
        layout.addWidget(self.license_browser)

        # Checkbox for accepting the agreement
        self.accept_checkbox = QCheckBox("I accept the agreement", self)
        layout.addWidget(self.accept_checkbox)

        # Reference to the next button, which we will enable/disable
        self.next_button = None

    def load_license_text(self):
        """Loads the license text from a file and displays it in the QTextBrowser."""
        try:
            with open("installer/license/license.txt", "r") as file:
                license_text = file.read()
                self.license_browser.setText(license_text)
        except FileNotFoundError:
            self.license_browser.setText("License file not found. Please make sure 'license.txt' is available.")
