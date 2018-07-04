from MySql import(
    getAllCustomer, getAllProduct, getArrears, getInventory
) 
from ui2 import Ui_Dialog

def updataCustomer(ui):
    customerInfo = getAllCustomer()
    for row in customerInfo:
        ui.Add(row['custid'] + " : " + row['custname'])
