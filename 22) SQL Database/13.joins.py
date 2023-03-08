import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(host="localhost", user="root", password="12u8g6v5", database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = (name,price,imageUrl,description)

    cursor.execute(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} products added")
        print(f"Last product id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        connection.close()
        print("database connection ended")

# insertProduct("huawei",4500,"14.jpg","good")

def insertProducts(yourList):
    connection = mysql.connector.connect(host="localhost", user="root", password="12u8g6v5", database="node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)"
    values = yourList

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} products added")
        print(f"Last product id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        connection.close()
        print("database connection ended")

def getProducts():
    connection = mysql.connector.connect(host="localhost", user = "root", password="12u8g6v5", database="node-app")
    cursor = connection.cursor()

    sql = "Select * from products"
    sql = "Select * from categories"
    sql = "Select * from products inner join categories on categories.id = products.categoryid"
    sql = "Select products.name,products.price,categories.name from products inner join categories on categories.id = products.categoryid"
    sql = "Select p.name,p.price,c.name from products as p inner join categories as c on c.id = p.categoryid where c.name='telefon'"


    cursor.execute(sql)

    try:
        result = cursor.fetchall()    
        for product in result:
            print(product)
    except mysql.connector.Error as err:
        print('error:', err)
    finally:
        connection.close()
        print('database connection ended')


getProducts()
