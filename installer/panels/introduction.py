from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class IntroductionPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create a layout for the panel
        layout = QVBoxLayout(self)

        # Create a label for the background image
        self.background_label = QLabel(self)
        pixmap = QPixmap("path_to_your_image/background.jpg")  # Update with the actual path to your image
        self.background_label.setPixmap(pixmap)
        self.background_label.setScaledContents(True)  # Scale the image to fit the label
        self.background_label.setGeometry(self.rect())  # Set it to fill the panel

        # Create a label for the introduction message
        self.intro_label = QLabel("Welcome to the Installer!\n\n"
                                   "This installer will guide you through the installation process.\n"
                                   "Please follow the instructions carefully.", self)
        self.intro_label.setAlignment(Qt.AlignCenter)  # Center the text
        self.intro_label.setStyleSheet("color: white; font-size: 18px;")  # Change text color and size for visibility

        # Add the introduction label on top of the background label
        layout.addWidget(self.background_label)
        layout.addWidget(self.intro_label)

        self.setLayout(layout)  # Set the layout for the panel

        # Adjust the layout to ensure the background is behind the label
        layout.setContentsMargins(0, 0, 0, 0)  # No margins
        layout.setSpacing(0)  # No spacing
