
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory, getProductUnit
) 

def updateCustomers():
    customerInfo = getAllCustomers()
    return customerInfo

def updateProducts():
    productInfo = getAllProducts()
    return productInfo


'''
input: customer: custid : cusname
return: amount lastdate
error return: 0 0
'''
def getProductArrears(customer):
    cust = customer.split(" ")
    custid = cust[0]
    arrears = getArrears(custid)
    if(arrears):
        return arrears[0]['amount'], arrears[0]['lastdate']
    else:
        return 0, 0


'''
get product's unit and qty
input: productid
return: unit, qty
'''
def getProduct(product):
    prod = product.split(" ")
    productid = prod[0]
    unit = getProductUnit(productid)
    qty = getInventory(productid)
    return unit[0]['unit'], qty[0]['qty']
