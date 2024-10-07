from PyQt5.QtWidgets import QVBoxLayout, QLabel, QCheckBox, QHBoxLayout, QWidget, QTextBrowser
from PyQt5.QtCore import Qt
from panels.base_panel import BasePanel

class PackageSelectionPanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__("Package Selection", "Select the packages you want to install.", parent)

        self.packages = ["Package A", "Package B", "Package C"]  # Example packages
        self.selected_packages = []  # List of selected packages
        self.package_checkboxes = []  # Store checkbox references

        layout = self.layout()  # Get the existing layout

        # Create a layout for the package checkboxes
        package_layout = QVBoxLayout()
        for package in self.packages:
            checkbox = QCheckBox(package, self)
            checkbox.stateChanged.connect(self.on_checkbox_toggled)
            self.package_checkboxes.append(checkbox)
            package_layout.addWidget(checkbox)

        # Add package checkboxes to the main layout
        layout.addLayout(package_layout)

        # Package description area
        self.description_browser = QTextBrowser(self)
        layout.addWidget(self.description_browser)

    def on_checkbox_toggled(self):
        """Update selected packages and display the description of the selected package."""
        self.selected_packages = [checkbox.text() for checkbox in self.package_checkboxes if checkbox.isChecked()]
        if self.selected_packages:
            self.description_browser.setText(f"Selected Package: {self.selected_packages[-1]}")
        else:
            self.description_browser.setText("No package selected.")

