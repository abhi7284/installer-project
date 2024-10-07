from PyQt5.QtWidgets import QVBoxLayout, QLabel
from panels.base_panel import BasePanel

class SummaryPanel(BasePanel):
    def __init__(self, selected_packages, install_directory, parent=None):
        super().__init__("Summary", "Review your selections before proceeding.", parent)
        self.selected_packages = selected_packages
        self.install_directory = install_directory
        self.summary_label = QLabel(self)
        self.layout().addWidget(self.summary_label)  # Add summary label to the layout
        self.update_summary(selected_packages, install_directory)

    def update_summary(self, selected_packages, install_directory):
        """Update the summary display with the selected packages and directory."""
        self.selected_packages = selected_packages
        self.install_directory = install_directory
        package_list = ", ".join(self.selected_packages)
        summary_text = f"Selected Packages: {package_list}\nInstallation Directory: {self.install_directory}"
        self.summary_label.setText(summary_text)
