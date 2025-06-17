# PyQt5 QLabels

import sys # Syatem-specific parameters and functions (Iy provides access to some variables used or maintained by the imterpreter) 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon 
from PyQt5.QtGui import QFont # For font size
from PyQt5.QtCore import Qt # This is imported for alignments

class MainWindow(QMainWindow): # Class Inherits from QMainWindow 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Labels in Python")
        # self.setWindowGeometery(x, y, width, height)
        self.setGeometry(700, 300, 700, 500)
        self.setWindowIcon(QIcon("photo.jpg"))
        
        label = QLabel("Hello Anish", self)
        label.setFont(QFont("Arial", 20 ))
        label.setGeometry(0, 0, 700, 100)
        label.setStyleSheet("color: blue;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignButtom) # VERTICALLY BUTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        
        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER AND TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER AND BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER AND CENTER
        label.setAlignment(Qt.AlignCenter) # Center and Center
        
          
def main(): 
    app = QApplication(sys.argv) # sys is module and argv is module
    window = MainWindow() # default behaviour of the window is hidden
    window.show() # It blinks just for a fraction of second by this...
    sys.exit(app.exec_()) # It ensures to exit (Waits for user actions for the window)


if __name__ == "__main__":
    main()