# PyQt5 Line Edit (Also known as text box)
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()
        
    def initUI(self):
        self.line_edit.setGeometry(10, 10, 275, 40)
        self.button.setGeometry(290, 10, 100, 40)
        self.line_edit.setStyleSheet("font-family: Arial;"
                                     "font-size: 25px;")
        self.button.setStyleSheet("font-family: Arial;"
                                     "font-size: 25px;"
                                     "background-color: skyblue;"
                                     "border-radius: 8px;")
        self.line_edit.setPlaceholderText("Enter your name: ")
        self.button.clicked.connect(self.submit)
        
    
    def submit(self):
        # print("You clicked the button.")
        text = self.line_edit.text()
        print(f"Hello {text}")
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())