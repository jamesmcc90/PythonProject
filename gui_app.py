from time import time
import mysql.connector
from numpy.lib.npyio import save
import pandas as pd
import time
import tkinter as tkinter
from tkinter import *
import tkinter
import tkinter.messagebox

class Application(tkinter.Frame):

    baseWindow = tkinter.Tk()

    Label(baseWindow, text="Car ID", font=(12)).grid(row=0, column=0)
    inputID = tkinter.Entry(baseWindow)
    inputID.grid(row=0, column=1)

    Label(baseWindow, text="Car Colour", font=(12)).grid(row=1, column=0)
    inputColour = tkinter.Entry(baseWindow)
    inputColour.grid(row=1, column=1)

    Label(baseWindow, text="Car Make", font=(12)).grid(row=2, column=0)
    inputMake = tkinter.Entry(baseWindow)
    inputMake.grid(row=2, column=1)

    Label(baseWindow, text="Car Model", font=(12)).grid(row=3, column=0)
    inputModel = tkinter.Entry(baseWindow)
    inputModel.grid(row=3, column=1)
        
    baseWindow.title("My Python GUI Application")

    def hello ():
     tkinter.messagebox.showinfo("Message Box", "Hello there!")

    myButton = tkinter.Button(text="Click Me", command=hello).grid(row=5, column=0)

    baseWindow.geometry('600x600')
    baseWindow.mainloop()