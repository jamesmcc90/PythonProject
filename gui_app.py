from time import time
import mysql.connector
from numpy.lib.npyio import save
import pandas as pd
import time
import tkinter as tkinter
from tkinter import *
import tkinter
import tkinter.messagebox

baseWindow = tkinter.Tk()
baseWindow.title("My Python GUI Application")
baseWindow.iconbitmap('C:\\Users\\James\\Downloads\\Cornmanthe3rd-Plex-Other-python.ico')
baseWindow.geometry('400x300')

Label(baseWindow, text="Car ID", font=(12)).grid(row=0, column=0)
inputID = tkinter.Entry(baseWindow)
inputID.grid(row=0, column=1)

'''
def number():
    try:
        int(inputID.get())
    except ValueError:
        errorLabel.config(baseWindow, text='That is text!', font=(12)).grid(row=10, column=0)
'''

errorLabel = Label(baseWindow, text="")
Label(baseWindow, text="Car Colour", font=(12)).grid(row=2, column=0)
inputColour = tkinter.Entry(baseWindow)
inputColour.grid(row=2, column=1)

Label(baseWindow, text="Car Make", font=(12)).grid(row=3, column=0)
inputMake = tkinter.Entry(baseWindow)
inputMake.grid(row=3, column=1)

Label(baseWindow, text="Car Model", font=(12)).grid(row=4, column=0)
inputModel = tkinter.Entry(baseWindow)
inputModel.grid(row=4, column=1)

def hello ():
    tkinter.messagebox.showinfo("Message Box", "Hello there!")

myButton = tkinter.Button(text="Click Me", command=quit).grid(row=6, column=0)
baseWindow.mainloop()