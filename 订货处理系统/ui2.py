# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import updateCustomers
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(817, 450)
        self.inputlist_bt = QtWidgets.QPushButton(Dialog)
        self.inputlist_bt.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.inputlist_bt.setObjectName("inputlist_bt")
        self.tree_show_bt = QtWidgets.QPushButton(Dialog)
        self.tree_show_bt.setGeometry(QtCore.QRect(110, 10, 93, 28))
        self.tree_show_bt.setObjectName("tree_show_bt")
        self.tree_run_bt = QtWidgets.QPushButton(Dialog)
        self.tree_run_bt.setGeometry(QtCore.QRect(210, 10, 93, 28))
        self.tree_run_bt.setObjectName("tree_run_bt")
        self.illustrate_bt = QtWidgets.QPushButton(Dialog)
        self.illustrate_bt.setGeometry(QtCore.QRect(310, 10, 93, 28))
        self.illustrate_bt.setObjectName("illustrate_bt")
        self.code_show_bt = QtWidgets.QPushButton(Dialog)
        self.code_show_bt.setGeometry(QtCore.QRect(410, 10, 93, 28))
        self.code_show_bt.setObjectName("code_show_bt")
        self.exit_bt = QtWidgets.QPushButton(Dialog)
        self.exit_bt.setGeometry(QtCore.QRect(510, 10, 93, 28))
        self.exit_bt.setObjectName("exit_bt")
        self.client_info_lb = QtWidgets.QLabel(Dialog)
        self.client_info_lb.setGeometry(QtCore.QRect(30, 50, 91, 16))
        self.client_info_lb.setObjectName("client_info_lb")
        self.client_cs_lb = QtWidgets.QLabel(Dialog)
        self.client_cs_lb.setGeometry(QtCore.QRect(40, 80, 72, 15))
        self.client_cs_lb.setObjectName("client_cs_lb")
        self.debt_lb = QtWidgets.QLabel(Dialog)
        self.debt_lb.setGeometry(QtCore.QRect(40, 110, 72, 15))
        self.debt_lb.setObjectName("debt_lb")
        self.debt_show_lb = QtWidgets.QLabel(Dialog)
        self.debt_show_lb.setGeometry(QtCore.QRect(140, 110, 72, 15))
        self.debt_show_lb.setObjectName("debt_show_lb")
        self.debt_time_lb = QtWidgets.QLabel(Dialog)
        self.debt_time_lb.setGeometry(QtCore.QRect(280, 110, 72, 15))
        self.debt_time_lb.setObjectName("debt_time_lb")
        self.good_info_lb = QtWidgets.QLabel(Dialog)
        self.good_info_lb.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.good_info_lb.setObjectName("good_info_lb")
        self.good_cs_lb = QtWidgets.QLabel(Dialog)
        self.good_cs_lb.setGeometry(QtCore.QRect(40, 180, 72, 15))
        self.good_cs_lb.setObjectName("good_cs_lb")
        self.good_num_lb = QtWidgets.QLabel(Dialog)
        self.good_num_lb.setGeometry(QtCore.QRect(40, 220, 72, 15))
        self.good_num_lb.setObjectName("good_num_lb")
        self.lib_num_lb = QtWidgets.QLabel(Dialog)
        self.lib_num_lb.setGeometry(QtCore.QRect(460, 180, 72, 15))
        self.lib_num_lb.setObjectName("lib_num_lb")
        self.good_time_lb = QtWidgets.QLabel(Dialog)
        self.good_time_lb.setGeometry(QtCore.QRect(460, 220, 72, 15))
        self.good_time_lb.setObjectName("good_time_lb")
        self.strategy_lb = QtWidgets.QLabel(Dialog)
        self.strategy_lb.setGeometry(QtCore.QRect(30, 260, 72, 15))
        self.strategy_lb.setObjectName("strategy_lb")
        self.client_cs_cb = QtWidgets.QComboBox(Dialog)
        self.client_cs_cb.setGeometry(QtCore.QRect(140, 80, 91, 22))
        self.client_cs_cb.setObjectName("client_cs_cb")
        self.good_cs_cb = QtWidgets.QComboBox(Dialog)
        self.good_cs_cb.setGeometry(QtCore.QRect(140, 180, 91, 22))
        self.good_cs_cb.setObjectName("good_cs_cb")
        self.lib_num_show_lb = QtWidgets.QLabel(Dialog)
        self.lib_num_show_lb.setGeometry(QtCore.QRect(560, 180, 72, 15))
        self.lib_num_show_lb.setObjectName("lib_num_show_lb")
        self.block_lb = QtWidgets.QLabel(Dialog)
        self.block_lb.setGeometry(QtCore.QRect(640, 180, 72, 15))
        self.block_lb.setObjectName("block_lb")
        self.good_time_cb = QtWidgets.QComboBox(Dialog)
        self.good_time_cb.setGeometry(QtCore.QRect(560, 220, 87, 22))
        self.good_time_cb.setObjectName("good_time_cb")
        self.good_num_edit = QtWidgets.QLineEdit(Dialog)
        self.good_num_edit.setGeometry(QtCore.QRect(140, 220, 91, 21))
        self.good_num_edit.setObjectName("good_num_edit")
        self.judge_pro_lb = QtWidgets.QLabel(Dialog)
        self.judge_pro_lb.setGeometry(QtCore.QRect(40, 290, 72, 15))
        self.judge_pro_lb.setObjectName("judge_pro_lb")
        self.judge_pro_tb = QtWidgets.QTextBrowser(Dialog)
        self.judge_pro_tb.setGeometry(QtCore.QRect(40, 320, 291, 91))
        self.judge_pro_tb.setObjectName("judge_pro_tb")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(400, 270, 20, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(10, 420, 791, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 270, 20, 161))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(10, 260, 16, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(10, 130, 791, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(120, 150, 681, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(10, 240, 791, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(120, 50, 681, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(90, 260, 711, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(790, 270, 20, 161))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(790, 160, 20, 91))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(790, 60, 20, 81))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(Dialog)
        self.line_13.setGeometry(QtCore.QRect(0, 160, 20, 91))
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(Dialog)
        self.line_14.setGeometry(QtCore.QRect(0, 60, 20, 81))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(Dialog)
        self.line_15.setGeometry(QtCore.QRect(10, 150, 16, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(Dialog)
        self.line_16.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.result_lb = QtWidgets.QLabel(Dialog)
        self.result_lb.setGeometry(QtCore.QRect(430, 290, 72, 15))
        self.result_lb.setObjectName("result_lb")
        self.result_show_lb = QtWidgets.QLabel(Dialog)
        self.result_show_lb.setGeometry(QtCore.QRect(430, 310, 201, 31))
        self.result_show_lb.setObjectName("result_show_lb")
        self.debt_time_show_lb = QtWidgets.QLabel(Dialog)
        self.debt_time_show_lb.setGeometry(QtCore.QRect(370, 110, 72, 15))
        self.debt_time_show_lb.setObjectName("debt_time_show_lb")


        self.inputlist_bt.clicked.connect(self.InputListClick)
       # self.tree_show_bt.clicked.connect(self.TreeShowClick)
        self.tree_run_bt.clicked.connect(self.TreeRunClick)
       # self.illustrate_bt.clicked.connect(self.IllustrateClick)
       # self.code_show_bt.clicked.connect(self.CodeShowClick)
        self.exit_bt.clicked.connect(Dialog.reject)

        # self.client_cs_cb.currentIndexChanged.connect(self.ClientChange)
        # self.good_cs_cb.currentIndexChanged.connect(self.GoodChange)
        # self.good_time_cb.currentIndexChanged.connect(self.TimeChange)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def InputListClick(self):
        self.client_info_lb.setStyleSheet("color:black")
        self.good_info_lb.setStyleSheet("color:black")
        self.strategy_lb.setStyleSheet("color:gray")
        updateCustomers(self)
        
        

    #def TreeShowClick(self):

        

    def TreeRunClick(self):
        self.client_info_lb.setStyleSheet("color:gray")
        self.good_info_lb.setStyleSheet("color:gray")
        self.strategy_lb.setStyleSheet("color:black")

    #def IllustrateClick(self):

    #def CodeShowClick(self):

    def UpdateCustomers(self,text):
        #self.client_cs_cb.
        self.client_cs_cb.addItem(text)

    #def ClientChange(self):
        

   # def GoodChange(self):

   # def TimeChange(self):

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.inputlist_bt.setText(_translate("Dialog", "输入订货单"))
        self.tree_show_bt.setText(_translate("Dialog", "显示判定树"))
        self.tree_run_bt.setText(_translate("Dialog", "运行判定树"))
        self.illustrate_bt.setText(_translate("Dialog", "程序说明"))
        self.code_show_bt.setText(_translate("Dialog", "显示源码"))
        self.exit_bt.setText(_translate("Dialog", "退出"))
        self.client_info_lb.setText(_translate("Dialog", "订货客户信息"))
        self.client_cs_lb.setText(_translate("Dialog", "选择客户："))
        self.debt_lb.setText(_translate("Dialog", "欠款金额："))
        self.debt_show_lb.setText(_translate("Dialog", ""))
        self.debt_time_lb.setText(_translate("Dialog", "欠款时间："))
        self.good_info_lb.setText(_translate("Dialog", "订货产品信息"))
        self.good_cs_lb.setText(_translate("Dialog", "选择产品："))
        self.good_num_lb.setText(_translate("Dialog", "订货数量："))
        self.lib_num_lb.setText(_translate("Dialog", "库存数量："))
        self.good_time_lb.setText(_translate("Dialog", "订货时间："))
        self.strategy_lb.setText(_translate("Dialog", "处置策略"))
        self.lib_num_show_lb.setText(_translate("Dialog", ""))
        self.block_lb.setText(_translate("Dialog", "块"))
        self.judge_pro_lb.setText(_translate("Dialog", "判定过程："))
        self.result_lb.setText(_translate("Dialog", "判定结果："))
        self.result_show_lb.setText(_translate("Dialog", ""))
        self.debt_time_show_lb.setText(_translate("Dialog", ""))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
