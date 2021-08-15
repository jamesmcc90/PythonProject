# MySQL

# Create a Function to define server connection details

from time import time
import mysql.connector
from numpy.lib.npyio import save
import pandas as pd
import time
from mysql.connector import Error, connection
from getpass import getpass

try:
    connection = mysql.connector.connect(
    host='localhost',
    user=input('Enter username: '), # root,
    password=getpass('Enter password: '), #64lislunnan,
    database='my_schema',
    auth_plugin='mysql_native_password',    
    buffered=True)

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
 
def saveSQL():
    mysql.connector.connect()
    query = "SELECT * FROM cars"   
    mycursor.execute(query)    
    connection.commit()
    df = pd.read_sql(query, connection)
    df.to_csv('C:\\Users\\James\\Desktop\\SQL_Export' + time.strftime("%Y%m%d") + '.csv')

sql()
saveSQL()