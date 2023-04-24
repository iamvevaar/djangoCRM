import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

# prepare a cursor object

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE vevaar")

print("all Done")