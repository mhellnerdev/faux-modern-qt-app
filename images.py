import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("./circlelabs")
        self.setGeometry(50,50,500,300)
        self.UI()


    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/fox.png'))
        self.image.move(150,50)
        removeButton = QPushButton("Remove", self)
        removeButton.move(100, 220)
        removeButton.clicked.connect(self.removeImg)
        showButton = QPushButton("Show", self)
        showButton.move(260, 220)
        showButton.clicked.connect(self.showImg)
        self.show()

    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()