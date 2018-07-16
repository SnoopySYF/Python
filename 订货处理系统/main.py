#!/usr/bin/env python
#-*- coding:utf-8 -*-
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory, getProductUnit
) 
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from ui2 import Ui_Dialog
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

