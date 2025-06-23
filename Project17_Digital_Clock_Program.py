# Python PyQt5 Digital Clock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt # Qt is for alignment
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget): # we will inherit from the base class QWidgets
    def __init__(self): #creating a constructor of the window
        super().__init__()
        # self.time_label = QLabel("12:00:00", self) # placeholder time
        self.time_label = QLabel(self)  
        self.timer = QTimer(self)
        self.initUI()
        
    # in the initUI() method we will design the layouts of the digital clock
    def initUI(self):
        self.setWindowTitle("Digital Clock Program")
        self.setGeometry(600, 400, 300, 100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        # center aligned horizontally
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")
        
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]  # index of operator 0 This will retrieve the first element of the font family because we are working with a list.
        my_font = QFont(font_family, 150) # 150 is the font size
        self.time_label.setFont(my_font)
        
        # To get the clock update every second
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
    
    
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") # A is anteridium and P means post meridian
        self.time_label.setText(current_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show() # until this the window only displays momentarily just for few time for that we use the below function sys.exit(app.exec_())
    sys.exit(app.exec_()) # It is a method it handles the execution and also handles events such as mouse click, key presses or other user inputs
    