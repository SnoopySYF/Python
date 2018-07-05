from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory
) 
<<<<<<< HEAD

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
=======


def updataCustomer(ui):
    print(1)
    customerInfo = getAllCustomer()
    print(customerInfo)
    for row in customerInfo:
        ui.UpdateCustomers(row['custid'] + " : " + row['custname'])
        print(1)
>>>>>>> 538830a1dd3e4018468c5e24e8785a7e1c7f6c5b
