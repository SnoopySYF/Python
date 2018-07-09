import datetime
from MySql import(
    getAllCustomers, getAllProducts, getArrears, getInventory, getProductUnit, InsertOrder, DeleteOrder, UpdateInventory
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
    if(qty):
        return unit[0]['unit'], qty[0]['qty']
    else:
        return unit[0]['unit'], 0

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
    return date1-date2

'''
输入：订货数量， 库存， 是否欠款（根据这个后两项可选）， 订货时间， 欠款时间
返回：订单是否成立，判定过程，判定结果
'''
def Decision(order_num, store_num, ifowe, order_time = None ,owe_time = None):
    order = ""
    result = ""
    process = ""
    order_num = int(order_num)
    store_num = int(store_num)
    if(ifowe==False):
        if(order_num > store_num):
            order = "D2"
            process = "判定1：欠款时间为0天\n判定2：库存数量" + str(store_num) + " 小于 订货数量" + str(order_num)
            result = "先按库存发货进货再补发"
        else:
            order = "D1"
            process = "判定1：欠款时间为0天\n判定2：库存数量" + str(store_num) + " 大于等于 订货数量" + str(order_num)
            result = "立即发货"
    else:
        day_num = day_count(order_time ,owe_time).days  #欠款天数
        if(day_num <= 30):
            if(order_num <= store_num):
                order = "D1"
                process = "判定1：欠款时间为" + str(day_num) + "天\n判定2：库存数量" + str(store_num) + " 大于等于 订货数量" + str(order_num)
                result = "立即发货"
            else:
                order = "D2"
                process = "判定1：欠款时间为" + str(day_num) + "天\n判定2：库存数量" + str(store_num) + " 小于 订货数量" + str(order_num)
                result = "先按库存发货进货再补发"
        elif(30 < day_num < 100):
            if(order_num <= store_num):
                order = "D3"
                process = "判定1：欠款时间为" + str(day_num) + "天\n判定2：库存数量" + str(store_num) + " 大于等于 订货数量" + str(order_num)
                result = "先付款再发货"
            else:
                order = "D3"
                process = "判定1：欠款时间为" + str(day_num) + "天\n判定2：库存数量" + str(store_num) + " 小于 订货数量" + str(order_num)
                result = "不发货"
        elif(day_num >= 100):
            if(order_num <= store_num):
                order = "D3"
                process = "判定1：欠款时间为" + str(day_num) + "天"
                result = "通知先付款"
            else:
                order = "D3"
                process = "判定1：欠款时间为" + str(day_num) + "天"
                result = "通知先付款"
    return order, process, result

'''
创建订单
输入：客户id，产品id，订货数，库存数，类型（D1，D2，D3）
'''
def CreateOrder(custid, productid, order_num, store_num, form):
    order_num = int(order_num)
    store_num = int(store_num)
    if(form == "D1"):
        InsertOrder(custid, productid, order_num, form)
        UpdateInventory(productid, store_num - order_num)
    elif(form == "D2"):
        InsertOrder(custid, productid, order_num, form)
    elif(form == "D3"):
        InsertOrder(custid, productid, order_num, form)
        
