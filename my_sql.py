# MySQL

# Create a Function to define server connection details

import mysql.connector
from mysql.connector import Error, connection
from getpass import getpass

try:
    connection = mysql.connector.connect(
    host='localhost',
    user=input('Enter username: '), # root,
    password=getpass('Enter password: '), #64lislunnan,
    database='my_schema',
    auth_plugin='mysql_native_password')
    mycursor = connection.cursor()
    print(connection)
except Error as cError:
    print(cError)

carID = input("Enter Car ID: ")
carColour = input("Enter Car Colour: ")
carMake = input("Enter Car Make: ")
carModel = input("Enter Car Model: ")

def sql():
    mysql.connector.connect()
    query = "INSERT INTO cars (Car_ID, Car_Colour, Car_Make, Car_Model) VALUES (%s, %s, %s, %s)"
    values = (carID, carColour, carMake, carModel)   
    mycursor.execute(query, values)
    connection.commit()
    connection.close()

sql()