from MySql import(
    getAllCustomer, getAllProduct, getArrears, getInventory
) 


def updataCustomer(ui):
    print(1)
    customerInfo = getAllCustomer()
    print(customerInfo)
    for row in customerInfo:
        ui.UpdateCustomers(row['custid'] + " : " + row['custname'])
        print(1)
