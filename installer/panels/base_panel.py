from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

class BasePanel(QWidget):
    def __init__(self, title, description, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        # Panel title
        title_label = QLabel(title, self)
        title_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        layout.addWidget(title_label)

        # Panel description
        description_label = QLabel(description, self)
        layout.addWidget(description_label)

        # Set the layout
        self.setLayout(layout)
