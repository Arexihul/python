import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,400,400)
        self.initUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Number 1: ")
        self.lbl_num1.move(50,30)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(120,30)
        self.txt_num1.resize(100,32)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Number 2: ")
        self.lbl_num2.move(50,80)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(120,80)
        self.txt_num2.resize(100,32)

        self.btn_addition = QtWidgets.QPushButton(self)
        self.btn_addition.setText(" + ")
        self.btn_addition.move(120,120)
        self.btn_addition.resize(30,30)
        self.btn_addition.clicked.connect(self.calculate)

        self.btn_subtraction = QtWidgets.QPushButton(self)
        self.btn_subtraction.setText(" - ")
        self.btn_subtraction.move(160,120)
        self.btn_subtraction.resize(30,30)
        self.btn_subtraction.clicked.connect(self.calculate)

        self.btn_multiplication = QtWidgets.QPushButton(self)
        self.btn_multiplication.setText(" x ")
        self.btn_multiplication.move(200,120)
        self.btn_multiplication.resize(30,30)
        self.btn_multiplication.clicked.connect(self.calculate)

        self.btn_division = QtWidgets.QPushButton(self)
        self.btn_division.setText(" ÷ ")
        self.btn_division.move(240,120)
        self.btn_division.resize(30,30)
        self.btn_division.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(120,160)

    def add(self):
        result = int(self.txt_num1.text()) + int(self.txt_num2.text())
        self.lbl_result.setText("Result: " + str(result))

    def sub(self):
        result = int(self.txt_num1.text()) - int(self.txt_num2.text())
        self.lbl_result.setText("Result: " + str(result))

    def mul(self):
        result = int(self.txt_num1.text()) * int(self.txt_num2.text())
        self.lbl_result.setText("Result: " + str(result))

    def div(self):
        result = int(self.txt_num1.text()) / int(self.txt_num2.text())
        self.lbl_result.setText("Result: " + str(result))

    def calculate(self):
        sender = self.sender().text()
        result = 0

        if sender == " + ":
            result = int(self.txt_num1.text()) + int(self.txt_num2.text())
        elif sender == " - ":
            result = int(self.txt_num1.text()) - int(self.txt_num2.text())
        elif sender == " x ":
            result = int(self.txt_num1.text()) * int(self.txt_num2.text())
        elif sender == " ÷ ":
            result = int(self.txt_num1.text()) / int(self.txt_num2.text())

        self.label_sonuc.setText("Result: " + str(result))
        

def window():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

window()

# command --> pyuic5 MainWindow.ui -o MainWindow.py