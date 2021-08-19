import tkinter as tk
from tkinter import *
from time import time
import mysql.connector
from numpy.lib.npyio import save
import pandas as pd
from mysql.connector import Error, connection
from getpass import getpass

root = tk.Tk()
root.geometry("800x640")

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

def sql():
    mysql.connector.connect()
    query = "INSERT INTO cars (Car_ID, Car_Colour, Car_Make, Car_Model) VALUES (%s, %s, %s, %s)"
    values = (carID, carColour, carMake, carModel)   
    mycursor.execute(query, values)
    connection.commit()

labelcarID = Label(root, text="Car ID").place(x = 40, y=20)
textcarID=tk.Text(root, height=3)
textcarID.pack()

labelcarID = Label(root, text="Car Colour").place(x = 40, y=60)
textcarColour=tk.Text(root, height=3)
textcarColour.pack()

textcarMake=tk.Text(root, height=3)
textcarMake.pack()

textcarModel=tk.Text(root, height=3)
textcarModel.pack()

btnRead=tk.Button(root, height=1, width=10, text="Read", command=sql)

btnRead.pack()

root.mainloop()