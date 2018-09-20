import mysql.connector
import json
import pymysql



mydb = mysql.connector.connect(
  host="",
  port="",
  user="",
  passwd="",
  database=""
)

mycursor = mydb.cursor()

def sqlAdd(name, address):
    mycursor = mydb.cursor()
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, address)
    mycursor.execute(sql, val)
    mydb.commit()

def sqlUpdateName(firstName, secondName):
    mycursor = mydb.cursor()
    sql = "UPDATE customers SET name = %s WHERE name = %s"
    val = (secondName, firstName)
    mycursor.execute(sql, val)
    mydb.commit()


def sqlUpdateAddress(firstAddress, secondAddress):
    mycursor = mydb.cursor()
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = (secondAddress, firstAddress)
    mycursor.execute(sql, val)
    mydb.commit()

def sqlDeleteName(name):
    mycursor = mydb.cursor()
    sql = "DELETE FROM customers WHERE name = %s"
    val = (name, )
    mycursor.execute(sql, val)
    mydb.commit()

def sqlDeleteAddress(address):
    mycursor = mydb.cursor()
    sql = "DELETE FROM customers WHERE address = %s"
    val = (address, )
    mycursor.execute(sql, val)
    mydb.commit()

def sqlSelectCustomers():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM customers")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def convertToJSON():

    connection = pymysql.connect(host='',
                                user='',
                                password='',
                                db='',
                                charset='',
                                cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customers")

    result = cursor.fetchall()
    print(json.dumps(result, indent=2))

    with open('test.json', 'w') as f:
        json.dump(result, f)

def convertFromJSON(JSONObj):
    jsondata = JSONObj
    pythonobj = json.loads(jsondata)
    return pythonobj


def main():
    json_data = '{"name": "Brian", "city": "Seattle"}'
    test = convertFromJSON(json_data)
    print(test["name"])

main()
