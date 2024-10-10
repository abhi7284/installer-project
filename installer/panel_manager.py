from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from panels.introduction import IntroductionPanel
from panels.license_agreement import LicenseAgreementPanel
from panels.package_selection import PackageSelectionPanel
from panels.choose_install_directory import ChooseInstallDirectoryPanel
from panels.summary import SummaryPanel
from panels.progress import ProgressPanel
from panels.complete import CompletePanel
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QFrame, QLabel, QSpacerItem, QSizePolicy, QVBoxLayout

import sys

class PanelManager(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(400, 300)
        # Create the main layout
        main_layout = QVBoxLayout(self)

        # Create a stacked widget for the panels
        self.stack = QStackedWidget(self)

        # Create and add default panels
        self.introduction_panel = IntroductionPanel(self.stack)
        self.license_agreement_panel = LicenseAgreementPanel(self.stack)
        self.package_selection_panel = PackageSelectionPanel(self.stack)
        self.choose_install_directory_panel = ChooseInstallDirectoryPanel(self.stack)
        self.summary_panel = SummaryPanel([], "", self.stack)  # Initially empty
        self.progress_panel = ProgressPanel(self.stack)
        self.complete_panel = CompletePanel(self.stack)

        # Add panels to the stack
        self.stack.addWidget(self.introduction_panel)
        self.stack.addWidget(self.license_agreement_panel)
        self.stack.addWidget(self.package_selection_panel)
        self.stack.addWidget(self.choose_install_directory_panel)
        self.stack.addWidget(self.summary_panel)
        self.stack.addWidget(self.progress_panel)
        self.stack.addWidget(self.complete_panel)

        # Create a frame for the navigation buttons
        bottom_frame = QFrame(self)
        bottom_layout = QHBoxLayout(bottom_frame)

        # Create navigation buttons (Next, Previous, and Done)
        self.previous_button = QPushButton("Previous", self)
        self.next_button = QPushButton("Next", self)
        self.done_button = QPushButton("Done", self)
        self.previous_button.setFixedSize(100, 25) 
        self.next_button.setFixedSize(100, 25) 
        self.done_button.setFixedSize(100, 25) 

        # Connect the buttons to their respective methods
        self.next_button.clicked.connect(self.next_panel)
        self.previous_button.clicked.connect(self.previous_panel)
        self.done_button.clicked.connect(self.exit_application)

        # Add the buttons to the layout
        bottom_layout.addWidget(self.previous_button)
        bottom_layout.addWidget(self.next_button)
        bottom_layout.addWidget(self.done_button)

        # Initially, hide the Done button
        self.done_button.setVisible(False)

        # Add the stacked widget and bottom frame to the main layout
        main_layout.addWidget(self.stack)
        main_layout.addWidget(bottom_frame)

        # Set the layout for the main widget
        self.setLayout(main_layout)

        # Initially, hide the Previous button (because it's the first panel)
        self.update_navigation_buttons(0)

    def next_panel(self):
        """Move to the next panel in the stack."""
        current_index = self.stack.currentIndex()
        if current_index == 1:  # License Agreement panel
            if not self.license_agreement_panel.accept_checkbox.isChecked():
                self.next_button.setStyleSheet("background-color: lightblue; color: white;")
                return  # Don't proceed if checkbox is not checked

        if current_index < self.stack.count() - 1:  # If not on the last panel
            self.stack.setCurrentIndex(current_index + 1)
        self.update_navigation_buttons(current_index + 1)

        # Update the Summary panel with selected data
        if current_index == 3:  # Moving to Summary Panel
            selected_packages = self.package_selection_panel.selected_packages
            install_directory = self.choose_install_directory_panel.install_directory
            self.summary_panel.update_summary(selected_packages, install_directory)

    def previous_panel(self):
        """Move to the previous panel in the stack."""
        current_index = self.stack.currentIndex()
        if current_index > 0:  # If not on the first panel
            self.stack.setCurrentIndex(current_index - 1)
        self.update_navigation_buttons(current_index - 1)

    def update_navigation_buttons(self, index):
        """Update visibility of Next, Previous, and Done buttons based on the panel index."""
        # Hide Previous button if it's the first panel
        self.previous_button.setVisible(index > 0)

        # Hide Next button and show Done button if it's the last panel
        if index == self.stack.count() - 1:
            self.next_button.setVisible(False)
            self.done_button.setVisible(True)
        else:
            self.next_button.setVisible(True)
            self.done_button.setVisible(False)

    def exit_application(self):
        """Exit the application when Done button is clicked."""
        sys.exit()
