import sys
from PyQt5.QtWidgets import QApplication
from panel_manager import PanelManager

def main():
    app = QApplication(sys.argv)
    panel_manager = PanelManager()  # Create the main panel manager
    panel_manager.show()  # Show the main panel manager
    sys.exit(app.exec_())  # Start the application event loop

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
