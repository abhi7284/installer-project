from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog
from panels.base_panel import BasePanel

class ChooseInstallDirectoryPanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__("Choose Installation Directory", "Select where you want to install the packages.", parent)

        self.install_directory = ""  # Variable to hold the selected directory
        layout = self.layout()  # Get the existing layout

        # Input field for directory path
        self.directory_input = QLineEdit(self)
        layout.addWidget(self.directory_input)

        # Button to choose the directory
        choose_button = QPushButton("Choose Directory", self)
        choose_button.clicked.connect(self.choose_directory)
        layout.addWidget(choose_button)

    def choose_directory(self):
        """Open a dialog to choose a directory and set it in the input field."""
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.install_directory = directory
            self.directory_input.setText(directory)  # Display the selected directory
