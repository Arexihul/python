import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QLine
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QLabel, QLineEdit, QMainWindow, QProgressBar, QPushButton, QRadioButton, QSlider, QTableView, QTableWidget, QToolTip
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First App")
    win.setGeometry(200,200,500,500)
    win.setWindowIcon(QIcon("icon.png"))
    win.setToolTip("mytooltip")
    
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Your name: ")
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Your surname: ")
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)

    def clicked(self):
        print("Button clicked. Name: " + txt_name.text() + " Surname: " + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Save")
    btn_save.move(150,110)

    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())


window()

# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar