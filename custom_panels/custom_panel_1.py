from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class CustomPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        
        # Create a label to display a custom message
        self.custom_label = QLabel("This is a custom panel!", self)
        layout.addWidget(self.custom_label)

    def update_message(self, new_message):
        """Method to update the label on this custom panel."""
        self.custom_label.setText(new_message)
