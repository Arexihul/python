# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_radiobuttonForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxUlke = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUlke.setGeometry(QtCore.QRect(30, 20, 181, 241))
        self.groupBoxUlke.setObjectName("groupBoxUlke")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxUlke)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 111, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutUlke = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutUlke.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutUlke.setObjectName("gridLayoutUlke")
        self.radioAlmanya = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAlmanya.setObjectName("radioAlmanya")
        self.gridLayoutUlke.addWidget(self.radioAlmanya, 2, 0, 1, 1)
        self.radioTurkiye = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioTurkiye.setObjectName("radioTurkiye")
        self.gridLayoutUlke.addWidget(self.radioTurkiye, 0, 0, 1, 1)
        self.radioYunanistan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioYunanistan.setObjectName("radioYunanistan")
        self.gridLayoutUlke.addWidget(self.radioYunanistan, 3, 0, 1, 1)
        self.radioAzerbaycan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAzerbaycan.setObjectName("radioAzerbaycan")
        self.gridLayoutUlke.addWidget(self.radioAzerbaycan, 1, 0, 1, 1)
        self.lblUlke = QtWidgets.QLabel(self.groupBoxUlke)
        self.lblUlke.setGeometry(QtCore.QRect(0, 150, 171, 31))
        self.lblUlke.setText("")
        self.lblUlke.setObjectName("lblUlke")
        self.btnUlke = QtWidgets.QPushButton(self.groupBoxUlke)
        self.btnUlke.setGeometry(QtCore.QRect(10, 190, 91, 31))
        self.btnUlke.setObjectName("btnUlke")
        self.groupBoxEgitim = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEgitim.setGeometry(QtCore.QRect(240, 20, 181, 241))
        self.groupBoxEgitim.setObjectName("groupBoxEgitim")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxEgitim)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 111, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayoutEgitim = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayoutEgitim.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutEgitim.setObjectName("gridLayoutEgitim")
        self.radioLise = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioLise.setObjectName("radioLise")
        self.gridLayoutEgitim.addWidget(self.radioLise, 1, 0, 1, 1)
        self.radioLisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioLisans.setObjectName("radioLisans")
        self.gridLayoutEgitim.addWidget(self.radioLisans, 2, 0, 1, 1)
        self.radioYuksekLisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioYuksekLisans.setObjectName("radioYuksekLisans")
        self.gridLayoutEgitim.addWidget(self.radioYuksekLisans, 3, 0, 1, 1)
        self.radiolkokul = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radiolkokul.setObjectName("radiolkokul")
        self.gridLayoutEgitim.addWidget(self.radiolkokul, 0, 0, 1, 1)
        self.lblEgitim = QtWidgets.QLabel(self.groupBoxEgitim)
        self.lblEgitim.setGeometry(QtCore.QRect(0, 150, 171, 31))
        self.lblEgitim.setText("")
        self.lblEgitim.setObjectName("lblEgitim")
        self.btnEgitim = QtWidgets.QPushButton(self.groupBoxEgitim)
        self.btnEgitim.setGeometry(QtCore.QRect(10, 190, 91, 31))
        self.btnEgitim.setObjectName("btnEgitim")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxUlke.setTitle(_translate("MainWindow", "Ülke"))
        self.radioAlmanya.setText(_translate("MainWindow", "Almanya"))
        self.radioTurkiye.setText(_translate("MainWindow", "Türkiye"))
        self.radioYunanistan.setText(_translate("MainWindow", "Yunanistan"))
        self.radioAzerbaycan.setText(_translate("MainWindow", "Azerbaycan"))
        self.btnUlke.setText(_translate("MainWindow", "Ülke Seçimi"))
        self.groupBoxEgitim.setTitle(_translate("MainWindow", "Eğitim"))
        self.radioLise.setText(_translate("MainWindow", "Lise"))
        self.radioLisans.setText(_translate("MainWindow", "Lisans"))
        self.radioYuksekLisans.setText(_translate("MainWindow", "Yüksek Lisans"))
        self.radiolkokul.setText(_translate("MainWindow", "İlkokul"))
        self.btnEgitim.setText(_translate("MainWindow", "Eğitim Seçimi"))