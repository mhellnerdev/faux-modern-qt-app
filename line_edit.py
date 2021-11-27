import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("./circlelabs")
        self.setGeometry(500, 500, 350, 350)
        self.UI()


    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("User ID")
        self.nameTextBox.move(60, 50)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText("Password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(60, 100)
        button = QPushButton("Save", self)
        button.move(85, 150)
        button.clicked.connect(self.getValues)
        self.show()

    def getValues(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle("UserID: " + name + " Password: " + password)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()