# MySQL

# Create a Function to define server connection details

import mysql.connector
#customerName = input("Enter Customer Name: ")
#customerAddress = input("Enter Customer Address: ")

carID = input("Enter Car ID: ")
carColour = input("Enter Car Colour: ")
carMake = input("Enter Car Make: ")
carModel = input("Enter Car Model: ")

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='64lislunnan',
    database='my_schema',
    auth_plugin='mysql_native_password'
)

mycursor = connection.cursor()

# Create a function defining SQL insert
def sql():
    query = "INSERT INTO cars (Car_ID, Car_Colour, Car_Make, Car_Model) VALUES (%s, %s, %s, %s)"
    values = (carID, carColour, carMake, carModel)
    mycursor.execute(query, values)

sql()
connection.commit()  # Make changes persistent to DB/Table

for x in mycursor:
    print(x)