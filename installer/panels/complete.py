from PyQt5.QtWidgets import QVBoxLayout, QLabel
from panels.base_panel import BasePanel

class CompletePanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__("Installation Complete", "The installation has been successfully completed.", parent)
        # Add any additional completion display widgets here
        self.complete_label = QLabel("Thank you for installing!", self)
        self.layout().addWidget(self.complete_label)
