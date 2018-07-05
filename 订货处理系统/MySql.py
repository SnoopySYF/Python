
import pymysql

config = {
          'host':'172.19.195.175',
          'port':3306,#MySQL默认端口
          'user':'root',#mysql默认用户名
          'password':'123456',
          'db':'Orders',#数据库
          'charset':'utf8mb4',
          'cursorclass':pymysql.cursors.DictCursor,
          }

def getAllCustomer():
    db= pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

def getAllProduct():
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
