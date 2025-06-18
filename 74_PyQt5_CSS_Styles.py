# PyQt5 setStyleSheet()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setGeometry(700, 300, 500, 500)
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        hbox = QHBoxLayout()
        
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        
        central_widget.setLayout(hbox)
        
        # applying css to specific widgets rather than all, we need to set object name, Here's how ...
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")  
        
        
        # """""" triple quotes is used to write long strings in an organized way
        self.setStyleSheet      ("""
                                  QPushButton{
                                      font-size: 40px;
                                      font-family: Arial;
                                      padding: 15px 75px;
                                      margin: 25px;
                                      border: 3px solid;
                                      border-radius: 15px;
                                  } 
                                  QPushButton#button1{
                                      background-color: red;
                                  }
                                  QPushButton#button2{
                                      background-color: green;
                                  }
                                  QPushButton#button3{
                                      background-color: blue;  
                                  }
                                     
                                  QPushButton#button1:hover{
                                      color: white;
                                  }
                                  QPushButton#button2:hover{
                                      color: white;
                                  }
                                  QPushButton#button3:hover{
                                      color: white; 
                                  }
                                   """)
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
    
# This is kind of like boiler plate code for Python PyQt5 code
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super()._init_()
#         self.setGeometry(700, 300, 500, 500)
#         self.initUI()
        
#     def initUI(self):
#         pass
    
    
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())