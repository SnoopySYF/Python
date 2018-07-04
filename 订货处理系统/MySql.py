
import pymysql

def getAllCustomer():
    db = pymysql.connect("localhost", "root", "123456", "Orders")
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results

def getAllProduct():
    db = pymysql.connect("localhost", "root", "123456", "Orders")
    cursor = db.cursor()
    sql = "SELECT * FROM product"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return results