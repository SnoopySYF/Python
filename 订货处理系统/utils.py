
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory
) 

def updateCustomers():
    customerInfo = getAllCustomers()
    return customerInfo

def updateProducts():
    productInfo = getAllProducts()
    return productInfo

def updateArrears(custid):
    arrears = getArrears(custid)
    if(arrears):
        return arrears[0]["amount"], arrears[0]["lastdate"]
    else:
        return 0, 0
