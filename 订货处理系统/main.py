from MySql import(
    getAllCustomer, getAllProduct, getArrears, getInventory
) 
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui2 import Ui_Dialog

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_Dialog()
ui.setupUi(MainWindow)
ui.Add("21")
ui.Add("32")
MainWindow.show()
sys.exit(app.exec_())
