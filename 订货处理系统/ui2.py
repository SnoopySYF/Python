# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from utils import(
    updateCustomers, updateProducts, getCustomerArrears, getProduct, Decision
)
import sys
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setWindowTitle("订单处理系统")
        Dialog.resize(817, 450)
        
        self.input_list_bt = QtWidgets.QPushButton(Dialog)
        self.input_list_bt.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.input_list_bt.setText("输入订货单")
        self.tree_show_bt = QtWidgets.QPushButton(Dialog)
        self.tree_show_bt.setGeometry(QtCore.QRect(110, 10, 93, 28))
        self.tree_show_bt.setText("显示判定树")
        self.tree_run_bt = QtWidgets.QPushButton(Dialog)
        self.tree_run_bt.setGeometry(QtCore.QRect(210, 10, 93, 28))
        self.tree_run_bt.setText("运行判定树")
        self.illustrate_bt = QtWidgets.QPushButton(Dialog)
        self.illustrate_bt.setGeometry(QtCore.QRect(310, 10, 93, 28))
        self.illustrate_bt.setText("程序说明") 
        self.code_show_bt = QtWidgets.QPushButton(Dialog)
        self.code_show_bt.setGeometry(QtCore.QRect(410, 10, 93, 28))
        self.code_show_bt.setText("显示源码")
        self.exit_bt = QtWidgets.QPushButton(Dialog)
        self.exit_bt.setGeometry(QtCore.QRect(510, 10, 93, 28))
        self.exit_bt.setText("退出")
        
        self.client_info_lb = QtWidgets.QLabel(Dialog)
        self.client_info_lb.setGeometry(QtCore.QRect(30, 50, 91, 16))
        self.client_info_lb.setText("订货客户信息")
        
        self.client_cs_lb = QtWidgets.QLabel(Dialog)
        self.client_cs_lb.setGeometry(QtCore.QRect(40, 80, 72, 15))
        self.client_cs_lb.setText("选择客户：")
        self.client_cs_cb = QtWidgets.QComboBox(Dialog)
        self.client_cs_cb.setGeometry(QtCore.QRect(140, 80, 201, 22))
        self.client_cs_cb.addItem("选择客户")
        
        self.debt_lb = QtWidgets.QLabel(Dialog)
        self.debt_lb.setGeometry(QtCore.QRect(40, 110, 72, 15))
        self.debt_lb.setText("欠款金额：")
        self.debt_show_lb = QtWidgets.QLabel(Dialog)
        self.debt_show_lb.setGeometry(QtCore.QRect(140, 110, 72, 15))
        
        self.debt_time_lb = QtWidgets.QLabel(Dialog)
        self.debt_time_lb.setGeometry(QtCore.QRect(280, 110, 72, 15))
        self.debt_time_lb.setText("欠款时间")
        self.debt_time_show_lb = QtWidgets.QLabel(Dialog)
        self.debt_time_show_lb.setGeometry(QtCore.QRect(370, 110, 82, 15))
        
        self.line_1t1 = QtWidgets.QFrame(Dialog)
        self.line_1t1.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.line_1t1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1t1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1t2 = QtWidgets.QFrame(Dialog)
        self.line_1t2.setGeometry(QtCore.QRect(120, 50, 681, 20))
        self.line_1t2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1t2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1b = QtWidgets.QFrame(Dialog)
        self.line_1b.setGeometry(QtCore.QRect(10, 130, 791, 16))
        self.line_1b.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_1b.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1l = QtWidgets.QFrame(Dialog)
        self.line_1l.setGeometry(QtCore.QRect(0, 60, 20, 81))
        self.line_1l.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1l.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1r = QtWidgets.QFrame(Dialog)
        self.line_1r.setGeometry(QtCore.QRect(790, 60, 20, 81))
        self.line_1r.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1r.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.product_info_lb = QtWidgets.QLabel(Dialog)
        self.product_info_lb.setGeometry(QtCore.QRect(30, 150, 91, 16))
        self.product_info_lb.setText("订货产品信息")
        
        self.product_cs_lb = QtWidgets.QLabel(Dialog)
        self.product_cs_lb.setGeometry(QtCore.QRect(40, 180, 72, 15))
        self.product_cs_lb.setText("选择产品：")
        self.product_cs_cb = QtWidgets.QComboBox(Dialog)
        self.product_cs_cb.setGeometry(QtCore.QRect(140, 180, 161, 22))
        self.product_cs_cb.addItem("选择产品")
        
        self.lib_num_lb = QtWidgets.QLabel(Dialog)
        self.lib_num_lb.setGeometry(QtCore.QRect(460, 180, 72, 15))
        self.lib_num_lb.setText("库存数量")
        self.lib_num_show_lb = QtWidgets.QLabel(Dialog)
        self.lib_num_show_lb.setGeometry(QtCore.QRect(560, 180, 72, 15))
        self.lib_unit_lb = QtWidgets.QLabel(Dialog)
        self.lib_unit_lb.setGeometry(QtCore.QRect(640, 180, 72, 15))
        
        self.order_num_lb = QtWidgets.QLabel(Dialog)
        self.order_num_lb.setGeometry(QtCore.QRect(40, 220, 72, 15))
        self.order_num_lb.setText("订货数量：")
        self.order_num_edit = QtWidgets.QLineEdit(Dialog)
        self.order_num_edit.setGeometry(QtCore.QRect(140, 220, 91, 21))
        
        self.order_time_lb = QtWidgets.QLabel(Dialog)
        self.order_time_lb.setGeometry(QtCore.QRect(460, 220, 72, 15))
        self.order_time_lb.setText("订货时间：")
        self.good_time_cb = QtWidgets.QComboBox(Dialog)
        self.good_time_cb.setGeometry(QtCore.QRect(560, 220, 87, 22))
        
        self.line_2t1 = QtWidgets.QFrame(Dialog)
        self.line_2t1.setGeometry(QtCore.QRect(10, 150, 16, 16))
        self.line_2t1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2t1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2t2 = QtWidgets.QFrame(Dialog)
        self.line_2t2.setGeometry(QtCore.QRect(120, 150, 681, 20))
        self.line_2t2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2t2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2b = QtWidgets.QFrame(Dialog)
        self.line_2b.setGeometry(QtCore.QRect(10, 240, 791, 16))
        self.line_2b.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2b.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2l = QtWidgets.QFrame(Dialog)
        self.line_2l.setGeometry(QtCore.QRect(0, 160, 20, 91))
        self.line_2l.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2l.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2r = QtWidgets.QFrame(Dialog)
        self.line_2r.setGeometry(QtCore.QRect(790, 160, 20, 91))
        self.line_2r.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2r.setFrameShadow(QtWidgets.QFrame.Sunken)
        
        self.strategy_lb = QtWidgets.QLabel(Dialog)
        self.strategy_lb.setGeometry(QtCore.QRect(30, 260, 72, 15))
        self.strategy_lb.setText("处置策略")
        
        self.judge_pro_lb = QtWidgets.QLabel(Dialog)
        self.judge_pro_lb.setGeometry(QtCore.QRect(40, 290, 72, 15))
        self.judge_pro_lb.setText("判定过程")
        self.judge_pro_tb = QtWidgets.QTextBrowser(Dialog)
        self.judge_pro_tb.setGeometry(QtCore.QRect(40, 320, 291, 91))
        
        self.result_lb = QtWidgets.QLabel(Dialog)
        self.result_lb.setGeometry(QtCore.QRect(430, 290, 72, 15))
        self.result_lb.setText("判定结果")
        self.result_show_lb = QtWidgets.QLabel(Dialog)
        self.result_show_lb.setGeometry(QtCore.QRect(430, 310, 201, 31))
        
        self.line_3t1 = QtWidgets.QFrame(Dialog)
        self.line_3t1.setGeometry(QtCore.QRect(10, 260, 16, 16))
        self.line_3t1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3t1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3t2 = QtWidgets.QFrame(Dialog)
        self.line_3t2.setGeometry(QtCore.QRect(90, 260, 711, 20))
        self.line_3t2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3t2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3b = QtWidgets.QFrame(Dialog)
        self.line_3b.setGeometry(QtCore.QRect(10, 420, 791, 20))
        self.line_3b.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3b.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3l = QtWidgets.QFrame(Dialog)
        self.line_3l.setGeometry(QtCore.QRect(0, 270, 20, 161))
        self.line_3l.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3l.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3r = QtWidgets.QFrame(Dialog)
        self.line_3r.setGeometry(QtCore.QRect(790, 270, 20, 161))
        self.line_3r.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3r.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3m = QtWidgets.QFrame(Dialog)
        self.line_3m.setGeometry(QtCore.QRect(400, 270, 20, 161))
        self.line_3m.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3m.setFrameShadow(QtWidgets.QFrame.Sunken)


        self.input_list_bt.clicked.connect(self.InputListClick)
       # self.tree_show_bt.clicked.connect(self.TreeShowClick)
        self.tree_run_bt.clicked.connect(self.TreeRunClick)
       # self.illustrate_bt.clicked.connect(self.IllustrateClick)
       # self.code_show_bt.clicked.connect(self.CodeShowClick)
        self.exit_bt.clicked.connect(Dialog.reject)

        self.client_cs_cb.currentTextChanged.connect(self.ClientChange)
        self.product_cs_cb.currentTextChanged.connect(self.ProductChange)
       # self.good_time_cb.currentIndexChanged.connect(self.TimeChange)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def InputListClick(self):
        self.client_info_lb.setStyleSheet("color:black")
        self.product_info_lb.setStyleSheet("color:black")
        self.strategy_lb.setStyleSheet("color:gray")

        self.client_cs_cb.currentTextChanged.disconnect(self.ClientChange)
        self.product_cs_cb.currentTextChanged.disconnect(self.ProductChange)
        client_num = self.client_cs_cb.count()
        for i in range(1,client_num):
            self.client_cs_cb.removeItem(1)
        product_num = self.order_cs_cb.count()
        for j in range(1,product_num):
            self.order_cs_cb.removeItem(1)
        self.client_cs_cb.currentTextChanged.connect(self.ClientChange)
        self.product_cs_cb.currentTextChanged.connect(self.GoodChange)
        print(1)
        customers = updateCustomers()
        print(0)
        for custom in customers:
            self.UpdateCustomers(custom['custid'] + " : " + custom['custname'])
        products = updateProducts()
        for product in products:
            self.UpdateProducts(product['productid'] + " : " + product['productname'])
        

    #def TreeShowClick(self):

        

    def TreeRunClick(self):
        self.client_info_lb.setStyleSheet("color:gray")
        self.product_info_lb.setStyleSheet("color:gray")
        self.strategy_lb.setStyleSheet("color:black")
        debt = self.debt_show_lb.text()
        debt_time = self.debt_time_show_lb.text()
        product_num = self.order_num_edit.text()
        lib_num = self.lib_num_show_lb.text()
        good_time = "2014-6-11"
        if debt == "无欠款":
            order, process, result = Decision(product_num, lib_num, False)
        else:
            order, process, result = Decision(product_num, lib_num, True, good_time, debt_time)
        self.judge_pro_tb.setText(process)
        self.result_show_lb.setText(result)

    #def IllustrateClick(self):

    #def CodeShowClick(self):

    def UpdateCustomers(self,text):
        self.client_cs_cb.addItem(text)

    def UpdateProducts(self,text):
        self.product_cs_cb.addItem(text)

    def ClientChange(self):
        client = self.client_cs_cb.currentText()
        print(client)
        debt, debt_time = getCustomerArrears(client)
        print(debt)
        print(debt_time)
        if debt == 0:
            self.debt_show_lb.setText("无欠款")
            self.debt_time_show_lb.setText("")
        else:
            self.debt_show_lb.setText(str(debt))
            self.debt_time_show_lb.setText(debt_time)

    def ProductChange(self):
        good = self.good_cs_cb.currentText()
        good_type, good_num = getProduct(good)
        print(good_type)
        print(good_num)
        self.good_type_lb.setText(good_type)
        self.lib_num_show_lb.setText(str(good_num))

   # def TimeChange(self):


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
