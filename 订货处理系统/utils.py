import datetime
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
def getCustomerArrears(customer):
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

def day_count(order_time ,owe_time):#计算欠款天数 订货时间 欠款时间
    temp=order_time.split('-')
    order_year=int(temp[0])
    order_month=int(temp[1])
    order_day=int(temp[2])
    temp = owe_time.split('-')
    owe_year = int(temp[0])
    owe_month = int(temp[1])
    owe_day = int(temp[2])
    date1=datetime.datetime(order_year,order_month,order_day)
    date2 = datetime.datetime(owe_year, owe_month, owe_day)
    print(date1-date2)
    return date1-date2

'''
输入：订货数量， 库存， 是否欠款（根据这个后两项可选）， 订货时间， 欠款时间
返回：判定结果
'''
def provide(order_num, store_num, ifowe, order_time = None ,owe_time = None):
    if(ifowe==False):
        if(order_num>store_num):
            return "先按库存发货进货再补发"
        else:
            return "立即发货"
    else:
        day_num = day_count(order_time ,owe_time).days  #欠款天数
        if(day_num <= 30):
            if(order_num <= store_num):
                return "立即发货"
            else:
                return "先按库存发货进货再补发"
        elif(30 < day_num < 100):
            if(order_num <= store_num):
                return "先付款再发货"
            else:
                return "不发货"
        elif(day_num >= 100):
            if(order_num <= store_num):
                return "通知先付款"
            else:
                return "通知先付款"

