# main.py
# Main script


# Imports
import sys

from PySide6 import QtWidgets

import src.gui as gui


# Definitions
def main():
    """Main"""
    
    # Create a Qt app
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and initialize windows
    gui.create_windows(app)
    
    # Show the main window    
    gui.main_window.show()

    # Start app and exit with code
    sys.exit(app.exec())

# Run
if __name__ == '__main__':
    main()