from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtCore import Qt

class SummaryPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main layout for the Summary Panel
        layout = QVBoxLayout(self)

        # Top message
        message_label = QLabel("Summary of your selections", self)
        message_label.setAlignment(Qt.AlignCenter)  # Center align the message
        layout.addWidget(message_label)

        # Text edit to display the selected packages
        self.summary_text = QTextEdit(self)
        self.summary_text.setReadOnly(True)  # Make it read-only so users can't modify it
        layout.addWidget(self.summary_text)

        # Set the layout
        self.setLayout(layout)

    def update_summary(self, selected_packages):
        """Updates the summary with the list of selected packages."""
        summary_text = "The following packages will be installed:\n\n"
        summary_text += "\n".join(selected_packages) if selected_packages else "No packages selected."
        self.summary_text.setText(summary_text)
