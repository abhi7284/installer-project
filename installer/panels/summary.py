from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class SummaryPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        # Create a label to display the introduction message
        self.intro_label = QLabel("Summary Panel", self)
        layout.addWidget(self.intro_label)

    def update_message(self, new_message):
        """Method to update the label on this panel."""
        self.intro_label.setText(new_message)
