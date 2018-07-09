import pymysql

config = {
          'host':'172.19.195.175',#数据库所在主机IP
          'port':3306,#MySQL默认端口
          'user':'root',#mysql默认用户名
          'password':'123456',
          'db':'Orders',#数据库
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

'''
访问数据库，获取所有用户信息
返回：用户信息  （格式：[[{key:value},...], ...]）
'''
def getAllCustomers():
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

'''
访问数据库，获取所有产品信息
返回：产品信息  （格式：[[{key:value},...], ...]）
'''
def getAllProducts():
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

'''
访问数据库，获取用户欠款信息
输入：用户id
返回：欠款信息  （格式：[[{key:value}, ...]]）
'''
def getArrears(custid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM arrears WHERE custid = '%s'" % (custid)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

'''
访问数据库，获取产品库存信息
输入：产品id
返回：库存信息  （格式：[[{key:value}, ...]]）
'''
def getInventory(productid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT qty FROM inventory WHERE productid = '%s'" % (productid)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results  

'''
访问数据库，获取产品单位信息
输入：产品id
返回：单位信息  （格式：[[{key:value}, ...]]）
'''
def getProductUnit(productid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT unit FROM product WHERE productid = '%s'" % (productid)
    cursor.execute(sql)
    unit = cursor.fetchall()
    db.close()
    return unit

'''
访问数据库，插入订单信息
输入：用户id，产品id，订货数量，类型（D1,D2,D3）
'''
def InsertOrder(custid, productid, num, form):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO orders(custid, productid, num, form) VALUES (%s, %s, %s, %s)"
    data = (custid, productid, num, form)
    cursor.execute(sql, data)
    db.commit()
    db.close()

'''
访问数据库，删除订单信息
输入：用户id，产品id
'''
def DeleteOrder(custid, productid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "DELETE FROM orders WHERE custid = '%s' and productid = '%s'" % (custid, productid)
    cursor.execute(sql)
    db.commit()
    db.close()

'''
访问数据库，更新产品库存
输入：产品id，更改后的库存
'''
def UpdateInventory(productid, qty):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "UPDATE inventory SET qty = %s WHERE productid = %s" % (qty, productid)
    cursor.execute(sql)
    db.commit()
    db.close()
