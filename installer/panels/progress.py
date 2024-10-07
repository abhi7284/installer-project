from PyQt5.QtWidgets import QVBoxLayout, QLabel
from panels.base_panel import BasePanel

class ProgressPanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__("Progress", "Installation in progress...", parent)
        # Add any additional progress display widgets here
        self.progress_label = QLabel("Installation is currently ongoing...", self)
        self.layout().addWidget(self.progress_label)
