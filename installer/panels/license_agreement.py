from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextBrowser, QCheckBox, QHBoxLayout
from PyQt5.QtCore import Qt

class LicenseAgreementPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main layout for the License Panel
        layout = QVBoxLayout(self)

        # Top message
        message_label = QLabel("Below is the license agreement", self)
        message_label.setAlignment(Qt.AlignCenter)  # Center align the message
        layout.addWidget(message_label)

        # Text Browser to display license text
        self.license_browser = QTextBrowser(self)
        self.load_license_text()  # Load the content of license.txt file
        layout.addWidget(self.license_browser)

        # Checkbox for accepting the agreement
        self.accept_checkbox = QCheckBox("I accept the agreement", self)
        self.accept_checkbox.stateChanged.connect(self.on_checkbox_toggled)
        layout.addWidget(self.accept_checkbox)

        # Set the layout
        self.setLayout(layout)

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

    def on_checkbox_toggled(self):
        """Enables the Next button only when the checkbox is checked."""
        if self.next_button:  # If the next button is assigned
            self.next_button.setEnabled(self.accept_checkbox.isChecked())

