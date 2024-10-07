from PyQt5.QtWidgets import QStackedWidget, QPushButton, QHBoxLayout, QWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys


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

        # Create a frame for the icon and navigation buttons
        bottom_frame = QFrame(self)
        bottom_layout = QHBoxLayout(bottom_frame)

        # Set margins for the icon and buttons
        bottom_layout.setContentsMargins(10, 0, 10, 0)  # 10px margin on both left and right

        # Create a label for the icon
        self.icon_label = QLabel(self)
        icon_path = "installer/icons/icon.png"  # Update with the actual path to your icon
        pixmap = QPixmap(icon_path)
        if not pixmap.isNull():
            self.icon_label.setPixmap(pixmap.scaled(100, 50, Qt.KeepAspectRatio))  # Resize to 100x50
        else:
            print("Icon not found or unable to load")

        # Set the background of the icon label to be transparent
        self.icon_label.setStyleSheet("background: transparent;")

        # Add the icon to the bottom layout (left side)
        bottom_layout.addWidget(self.icon_label)

        # Add spacing to push the buttons to the right side
        bottom_layout.addStretch(1)

        # Create navigation buttons (Next, Previous, and Done)
        self.previous_button = QPushButton("Previous", self)
        self.next_button = QPushButton("Next", self)
        self.done_button = QPushButton("Done", self)

        # Connect the buttons to their respective methods
        self.next_button.clicked.connect(self.next_panel)
        self.previous_button.clicked.connect(self.previous_panel)
        self.done_button.clicked.connect(self.exit_application)

        # Add the buttons to the right side of the layout
        bottom_layout.addWidget(self.previous_button)
        bottom_layout.addWidget(self.next_button)
        bottom_layout.addWidget(self.done_button)

        # Initially, hide the Done button
        self.done_button.setVisible(False)

        # Add the stacked widget (panels) and bottom frame (buttons + icon) to the main layout
        main_layout.addWidget(self.stack)
        main_layout.addWidget(bottom_frame)

        # Set the layout for the main widget
        self.setLayout(main_layout)

        # Initially, hide the Previous button (because it's the first panel)
        self.update_navigation_buttons(0)

    def next_panel(self):
        """Move to the next panel in the stack."""
        current_index = self.stack.currentIndex()
        if current_index < self.stack.count() - 1:  # If not on the last panel
            self.stack.setCurrentIndex(current_index + 1)
        self.update_navigation_buttons(current_index + 1)

    def previous_panel(self):
        """Move to the previous panel in the stack."""
        current_index = self.stack.currentIndex()
        if current_index > 0:  # If not on the first panel
            self.stack.setCurrentIndex(current_index - 1)
        self.update_navigation_buttons(current_index - 1)

    def update_navigation_buttons(self, index):
        """Update visibility of Next, Previous, and Done buttons based on the panel index."""
        # Hide Previous button if it's the first panel
        if index == 0:
            self.previous_button.setVisible(False)
        else:
            self.previous_button.setVisible(True)

        # Hide Next button and show Done button if it's the last panel
        if index == self.stack.count() - 1:
            self.next_button.setVisible(False)
            self.previous_button.setVisible(False)
            self.done_button.setVisible(True)
        else:
            self.next_button.setVisible(True)
            self.done_button.setVisible(False)

    def exit_application(self):
        """Exit the application when Done button is clicked."""
        sys.exit()