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

def getAllCustomers():
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

def getAllProducts():
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

def getArrears(custid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM arrears WHERE custid = '%s'" % (custid)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

def getInventory(productid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT qty FROM inventory WHERE productid = '%s'" % (productid)
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results  

def getProductUnit(productid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT unit FROM product WHERE productid = '%s'" % (productid)
    cursor.execute(sql)
    unit = cursor.fetchall()
    db.close()
    return unit

def InsertOrder(custid, productid, num, form):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO orders(custid, productid, num, form) VALUES (%s, %s, %s, %s)"
    data = (custid, productid, num, form)
    cursor.execute(sql, data)
    db.commit()
    db.close()

def DeleteOrder(custid, productid):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "DELETE FROM orders WHERE custid = '%s' and productid = '%s'" % (custid, productid)
    cursor.execute(sql)
    db.commit()
    db.close()

def UpdateInventory(productid, qty):
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "UPDATE inventory SET qty = %s WHERE productid = %s" % (qty, productid)
    cursor.execute(sql)
    db.commit()
    db.close()
