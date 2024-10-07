from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QFrame, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt

class PackageSelectionPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main layout for the Package Selection Panel
        layout = QVBoxLayout(self)

        # Top message
        message_label = QLabel("Please select packages you want to install", self)
        message_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(message_label)

        # Create a scroll area to hold the checkboxes
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Create a widget inside the scroll area to contain checkboxes
        package_widget = QWidget()
        package_layout = QVBoxLayout(package_widget)

        # Sample packages (can be dynamic based on actual needs)
        self.packages = {
            "Package 1": "This is the description for Package 1.",
            "Package 2": "This is the description for Package 2.",
            "Package 3": "This is the description for Package 3."
        }

        # Create checkboxes for each package
        self.checkboxes = []
        for package_name, package_description in self.packages.items():
            checkbox = QCheckBox(package_name, self)
            checkbox.package_description = package_description
            checkbox.stateChanged.connect(self.on_checkbox_toggled)
            package_layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

        # Add the package widget to the scroll area
        scroll_area.setWidget(package_widget)

        # Add the scroll area to the main layout (middle part)
        layout.addWidget(scroll_area)

        # Create a label for showing package description (bottom part)
        self.package_description_label = QLabel("Select a package to see its description.", self)
        self.package_description_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.package_description_label)

        # Set the layout for this panel
        self.setLayout(layout)

        # Reference to the next button, which we will enable/disable
        self.next_button = None

    def on_checkbox_toggled(self, state):
        """Handle checkbox toggle events to enable/disable the Next button and update description."""
        self.update_next_button_state()
        self.update_description()

    def update_next_button_state(self):
        """Enable the Next button only if at least one checkbox is checked."""
        if self.next_button:  # Ensure the Next button is assigned
            any_checked = any(checkbox.isChecked() for checkbox in self.checkboxes)
            self.next_button.setEnabled(any_checked)

    def update_description(self):
        """Update the package description label based on the selected package."""
        selected_checkboxes = [checkbox for checkbox in self.checkboxes if checkbox.isChecked()]
        
        if selected_checkboxes:
            # Show the description of the last selected package
            last_selected = selected_checkboxes[-1]
            self.package_description_label.setText(last_selected.package_description)
        else:
            # Reset the description if nothing is selected
            self.package_description_label.setText("Select a package to see its description.")
