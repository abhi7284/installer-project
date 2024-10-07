from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog

class ChooseInstallDirectoryPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create layout for the panel
        layout = QVBoxLayout(self)

        # Add label
        label = QLabel("Please choose the installation directory:", self)
        layout.addWidget(label)

        # Add text input to display selected directory
        self.dir_input = QLineEdit(self)
        self.dir_input.setPlaceholderText("Installation directory path...")
        layout.addWidget(self.dir_input)

        # Add 'Choose Directory' button
        self.choose_dir_button = QPushButton("Choose Directory", self)
        self.choose_dir_button.clicked.connect(self.open_directory_dialog)
        layout.addWidget(self.choose_dir_button)

        # Set the layout
        self.setLayout(layout)

    def open_directory_dialog(self):
        """Opens a dialog to select the installation directory."""
        selected_dir = QFileDialog.getExistingDirectory(self, "Select Installation Directory")
        if selected_dir:  # If a directory is selected
            self.dir_input.setText(selected_dir)
