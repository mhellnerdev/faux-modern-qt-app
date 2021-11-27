import sys
from PyQt5.QtWidgets import *

# instance the main window
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("./circlelabs")
        self.setGeometry(250,150,500,500)
        self.UI()

    # UI Widgets
    def UI(self):
        self.label1 = QLabel("Do you know any programming languages?", self)
        self.label1.move(40, 60)
        self.combo = QComboBox(self)
        self.combo.move(150, 100)
        button = QPushButton("Save", self)
        button.move(150, 150)
        button.clicked.connect(self.getValue)
        self.combo.addItem("Yes")
        self.combo.addItem("No")
        self.combo.addItems(["C", "C#", "Javascript", "Python", "Ruby", "React", "GoLang"])
        list1 = ["Wolverine", "Sabertooth", "Deadpool"]

        # add list 1 to combobox options
        for name in list1:
            self.combo.addItem(name)

        # add numbers in range and add to combobox, pass converted to string already
        for number in range(18, 101):
            self.combo.addItem(str(number))

        self.show()

    #get value of combobox
    def getValue(self):
        value = self.combo.currentText()
        print(value)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ == '__main__':
    main()