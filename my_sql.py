# MySQL

# Create a Function to define server connection details

from logging import error
import mysql.connector
from mysql.connector import Error, connection, errorcode
from getpass import getpass

try:
    with mysql.connector.connect(
        host='localhost',
        user=input('Enter username: '), # root,
        password=getpass('Enter password: '), #64lislunnan,
        database='my_schema',
        auth_plugin='mysql_native_password'
    ) as connection:        
        mycursor = connection.cursor()
        print(connection)
except Error as cError:
    print(cError)

if (connection):
    carID = input("Enter Car ID: ")
    carColour = input("Enter Car Colour: ")
    carMake = input("Enter Car Make: ")
    carModel = input("Enter Car Model: ")
else:
    print("Sorry, access denied!")

# Create a function defining SQL insert
def sql():
    query = "INSERT INTO cars (Car_ID, Car_Colour, Car_Make, Car_Model) VALUES (%s, %s, %s, %s)"
    values = (carID, carColour, carMake, carModel)
    connection.connect()
    mycursor.execute(query, values)
    connection.commit()  # Make changes persistent to DB/Table

def rowExists():
    query = "SELECT EXISTS(SELECT * from cars WHERE (%s))"
    value = (carID)
    mycursor.execute(query, value)
    if False(rowExists):
        sql()
    else:
        print("Sorry, this ID exists")

connection.close()