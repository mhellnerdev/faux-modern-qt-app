import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("./circlelabs")
        self.setGeometry(50,50,650,650)
        self.UI()


    def UI(self):
        self.text = QLabel("./circlelabs", self)
        enterButton = QPushButton("Enter",self)
        exitButton = QPushButton("Exit",self)
        self.text.move(150, 50)
        enterButton.move(100, 80)
        exitButton.move(300, 80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.text.setText("You Clicked Enter")
        self.text.resize(200, 20)
    def exitFunc(self):
        self.text.setText("You Clicked Exit")
        self.text.resize(200, 20)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()