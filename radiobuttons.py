import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

# instance the main window
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fox IT Tool")
        self.setGeometry(250,150,500,500)
        self.UI()

    # UI Widgets
    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/fox.png'))
        self.image.move(150,40)

        self.name = QLineEdit(self)
        self.name.move(150, 50 + 150)
        self.name.setPlaceholderText("UserID")
        self.password = QLineEdit(self)
        self.password.move(150, 100 + 150)
        self.password.setPlaceholderText("Password")
        self.domain = QRadioButton("Domain", self)
        self.domain.setChecked(True)
        self.local = QRadioButton("Local", self)
        self.domain.move(150, 170 + 150)
        self.local.move(280, 170 + 150)
        button = QPushButton("Login", self)
        #button.clicked.connect(self.getValues)
        button.move(180, 210 + 150)

        self.text = QLabel("© Fox Factory, Inc.", self)
        self.text.move(150, 460)

        self.show()




def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()