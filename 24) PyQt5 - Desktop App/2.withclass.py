import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("First App")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("icon.png"))
        self.setToolTip("mytooltip")
        self.initUI()   

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Your name: ")
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Your surname: ")
        self.lbl_surname.move(50,70)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,150)
        self.lbl_result.move(150,150)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150,30)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150,70)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(150,110)

        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_result.setText(f"Name: {self.txt_name.text()}\nSurname: {self.txt_surname.text()}")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
