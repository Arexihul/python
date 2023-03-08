import sys
from PyQt5 import QtWidgets
from _dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnCalculate.clicked.connect(self.calculate)


    def calculate(self):
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        print(start, end)

        print("Days in month {0}".format(start.daysInMonth()))
        print("Days in year {0}".format(start.daysInYear()))

        print(f"Total days: {start.daysTo(end)}")

        now = QDate.currentDate()
        
        print(f"Total days from now: {start.daysTo(now)}")


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
