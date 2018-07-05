import pymysql

config = {
<<<<<<< HEAD
          'host':'172.19.195.175',#数据库所在主机IP
=======
          'host':'172.19.195.175',
>>>>>>> 538830a1dd3e4018468c5e24e8785a7e1c7f6c5b
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


if __name__ == "__main__":
    we = getAllCustomer()
    print(we)
