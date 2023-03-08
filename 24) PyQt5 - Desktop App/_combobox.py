import sys
from PyQt5 import QtWidgets
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.cbSehirler

        combo.addItem("Ankara")
        combo.addItem("İstanbul")
        combo.addItem("Kocaeli")
        # combo.addItems(["Adana", "İzmir","Rize"])

        self.ui.btnLoadItems.clicked.connect(self.loadItems)
        self.ui.btnGetItems.clicked.connect(self.getItems)
        self.ui.btnClearItems.clicked.connect(self.clearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)

    def loadItems(self):
        sehirler = ["Adana","İzmir","Rize"]

        self.ui.cbSehirler.addItems(sehirler)

    def getItems(self):
        print(self.ui.cbSehirler.currentText())
        print(self.ui.cbSehirler.currentIndex())

        count = self.ui.cbSehirler.count()
        for index in range(count):
            print(self.ui.cbSehirler.itemText(index))  # itemText() girilen index numarasındaki itemin textini getirir.

    def clearItems(self):
        self.ui.cbSehirler.clear()

    def selectedChangedIndex(self, index):
        print(index)

    def selectedChangedText(self, text):
        print(text)

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
