import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("./circlelabs")
        self.setGeometry(50,50,650,650)
        self.UI()


    def UI(self):
        text1 = QLabel("./circlelabs", self)
        text2 = QLabel("developer operations", self)
        text1.move(100,50)
        text2.move(300,50)
        self.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()