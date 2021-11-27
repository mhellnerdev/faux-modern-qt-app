import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("./circlelabs")
        self.setGeometry(50,50,650,650)
        self.UI()


    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("User ID")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Password")
        self.surname.setEchoMode(QLineEdit.Password)
        self.name.move(150, 50)
        self.surname.move(150, 100)
        self.remember = QCheckBox("Remember me", self)
        self.remember.move(160, 155)
        button = QPushButton("Submit", self)
        button.move(200, 200)
        # button = QPushButton("Submit", self)
        button.clicked.connect(self.submit)
        self.show()

    def submit(self):
        if (self.remember.isChecked()):
            print("name: " + self.name.text() + " \nPassword: " + self.surname.text() + " \nRemember me checked")
        else:
            print("name: " + self.name.text() + " \nPassword: " + self.surname.text() + " \nRemember me is not checked")

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()