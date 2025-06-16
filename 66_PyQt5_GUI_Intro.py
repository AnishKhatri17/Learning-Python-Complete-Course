# PyQt5 Introduction

# First we need to install PyQt5 to use and import it.
# in the terminal >> pip install PyQt5
# I successfully installed PyQt5 and also updated it.

import sys # Syatem-specific parameters and functions (Iy provides access to some variables used or maintained by the imterpreter) 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon # Importing to insert an icon

class MainWindow(QMainWindow): # Class Inherits from QMainWindow 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First GUI Program in Python")
        # self.setWindowGeometery(x, y, width, height)
        self.setGeometry(700, 300, 700, 500)
        self.setWindowIcon(QIcon("photo.jpg"))
        
        
def main(): 
    app = QApplication(sys.argv) # sys is module and argv is module
    window = MainWindow() # default behaviour of the window is hidden
    window.show() # It blinks just for a fraction of second by this...
    sys.exit(app.exec_()) # It ensures to exit (Waits for user actions for the window)


if __name__ == "__main__":
    main()