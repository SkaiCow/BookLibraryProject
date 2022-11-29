from tkinter import *
from tkinter import ttk
from FileManager import findRecordByIsbn

def placeSearchBar(app):
    def searchFor(data):
        print("we are looking now! : " + str(data))
        findRecordByIsbn(data)
    bottomF = Frame(app.root)
    bottomF.grid(column=0, row=1, columnspan=2, sticky=NSEW)
    bottomF.columnconfigure(0, weight=1)
    userInput = StringVar()
    ttk.Entry(bottomF, textvariable=userInput).grid(column=0,row=0, sticky=NSEW)
    ttk.Button(bottomF, text="Search", command=lambda: searchFor(userInput.get())).grid(column=1,row=0)