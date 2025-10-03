
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pw123',

)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE ELDERCO")

print("Done")