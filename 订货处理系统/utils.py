
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory
) 

def updateCustomers(ui):
    customerInfo = getAllCustomers()
    return customerInfo

def updateProduct():
    productInfo = getAllProducts()

def updateArrears(custid):
    arrears = getArrears(custid)
    if(arrears):
        return arrears[0]["amount"], arrears[0]["lastdate"]
    else:
        return 0, 0
