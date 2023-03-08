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
        print("Hata:", err)
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
        print("Hata:", err)
    finally:
        connection.close()
        print("database connection ended")


liste = []
while True:
    name = input("Product Name: ")
    price = input("Product Price: ")
    imageUrl = input("Product İmage Url: ")
    description = input("Product Description: ")

    liste.append((name,price,imageUrl,description))

    result = input("Would you like to add more products? (y/n)")
    if result == "n":
        print("Your inputs are transferring to the database...")
        print(liste)
        insertProducts(liste)
        break
    elif result == "y":
        continue
    else:
        print("Please enter 'y' for yes and 'n' for no")
        result = input("Would you like to add more products? (y/n)")
    if result == "n":
        print("Your inputs are transferring to the database...")
        print(liste)
        insertProducts(liste)
        break
    elif result == "y":
        continue
    else:
        print("Please enter 'y' for yes and 'n' for no")

