from PyQt5.QtWidgets import QStackedWidget, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap

from panels.introduction import IntroductionPanel
from panels.license_agreement import LicenseAgreementPanel
from panels.package_selection import PackageSelectionPanel
from panels.summary import SummaryPanel
from panels.progress import ProgressPanel
from panels.complete import CompletePanel

class PanelManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create the main layout
        main_layout = QVBoxLayout(self)

        # Create a stacked widget for the panels
        self.stack = QStackedWidget(self)

        # Create and add default panels
        self.introduction_panel = IntroductionPanel(self.stack)
        self.license_agreement_panel = LicenseAgreementPanel(self.stack)
        self.package_selection_panel = PackageSelectionPanel(self.stack)
        self.summary_panel = SummaryPanel(self.stack)
        self.progress_panel = ProgressPanel(self.stack)
        self.complete_panel = CompletePanel(self.stack)

        # Add panels to the stack
        self.stack.addWidget(self.introduction_panel)
        self.stack.addWidget(self.license_agreement_panel)
        self.stack.addWidget(self.package_selection_panel)
        self.stack.addWidget(self.summary_panel)
        self.stack.addWidget(self.progress_panel)
        self.stack.addWidget(self.complete_panel)

        # Create navigation buttons
        self.next_button = QPushButton("Next", self)
        self.previous_button = QPushButton("Previous", self)

        # Connect buttons to methods
        self.next_button.clicked.connect(self.next_panel)
        self.previous_button.clicked.connect(self.previous_panel)

        # Create a layout for navigation buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)

        # Create a layout for the bottom icon
        icon_layout = QHBoxLayout()
        self.icon_label = QLabel(self)

        # Load icon with error checking
        icon_path = "installer/icons/icon.png"  # Adjust path as needed
        pixmap = QPixmap(icon_path)
        if pixmap.isNull():
            print("Error: Icon not found or unable to load.")
        
        # Resize the icon to 100x50 pixels
        self.icon_label.setPixmap(pixmap.scaled(100, 50, aspectRatioMode=1))  # Keep aspect ratio

        # Set the background of the icon label to be transparent
        self.icon_label.setStyleSheet("background: transparent;")

        icon_layout.addWidget(self.icon_label)
        icon_layout.addStretch(1)  # Push the icon to the left

        # Add components to the main layout
        main_layout.addWidget(self.stack)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(icon_layout)

        self.update_navigation_buttons(0)

    def next_panel(self):
        """Switch to the next panel."""
        current_index = self.stack.currentIndex()
        if current_index < self.stack.count() - 1:
            self.stack.setCurrentIndex(current_index + 1)
        self.update_navigation_buttons(current_index + 1)

    def previous_panel(self):
        """Switch to the previous panel."""
        current_index = self.stack.currentIndex()
        if current_index > 0:
            self.stack.setCurrentIndex(current_index - 1)
        self.update_navigation_buttons(current_index - 1)

    def update_navigation_buttons(self, index):
        """Enable or disable buttons based on the current panel index."""
        self.previous_button.setEnabled(index > 0)  # Disable "Previous" on first panel
        self.next_button.setEnabled(index < self.stack.count() - 1)  # Disable "Next" on last panel
