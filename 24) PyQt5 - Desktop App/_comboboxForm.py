# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_comboboxForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(441, 231)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbSehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbSehirler.setGeometry(QtCore.QRect(30, 30, 151, 41))
        self.cbSehirler.setObjectName("cbSehirler")
        self.lblResult = QtWidgets.QLabel(self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(210, 20, 201, 71))
        self.lblResult.setText("")
        self.lblResult.setObjectName("lblResult")
        self.btnGetItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetItems.setGeometry(QtCore.QRect(50, 130, 91, 31))
        self.btnGetItems.setObjectName("btnGetItems")
        self.btnLoadItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadItems.setGeometry(QtCore.QRect(180, 130, 81, 31))
        self.btnLoadItems.setObjectName("btnLoadItems")
        self.btnClearItems = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearItems.setGeometry(QtCore.QRect(290, 130, 81, 31))
        self.btnClearItems.setObjectName("btnClearItems")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 441, 21))
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
        self.btnGetItems.setText(_translate("MainWindow", "Get Item"))
        self.btnLoadItems.setText(_translate("MainWindow", "Load Items"))
        self.btnClearItems.setText(_translate("MainWindow", "Clear Items"))
