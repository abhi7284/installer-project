import sys  # Ensure sys is imported to handle system arguments
from PyQt5.QtWidgets import QApplication, QMainWindow
from panel_manager import PanelManager  # Import the PanelManager

class InstallerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Installer")
        self.setGeometry(200, 200, 800, 600)

        # Create and manage UI panels using PanelManager
        self.panel_manager = PanelManager(self)
        self.setCentralWidget(self.panel_manager)  # Set the main widget

        self.show()  # Show the main window

def main():
    app = QApplication(sys.argv)  # Create the application instance
    installer_app = InstallerApp()  # Create the main installer window
    sys.exit(app.exec_())  # Start the event loop

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
