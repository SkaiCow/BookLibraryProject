from tkinter import *
from tkinter import ttk



def placeSearchBar(app):
    def searchFor(data):
        if data == "":
            app.loadRecords()
            app.selectedRecord = None
            return
        if data.isnumeric():
            #this is a ISBN
            app.searchByIsbn(data)
        else:
            #this is a Title
            app.searchByTitle(data)
    bottomF = Frame(app.root)
    bottomF.grid(column=0, row=1, columnspan=2, sticky=NSEW)
    bottomF.columnconfigure(0, weight=1)
    userInput = StringVar()
    ttk.Entry(bottomF, textvariable=userInput).grid(column=0,row=0, sticky=NSEW)
    ttk.Button(bottomF, text="Search", command=lambda: searchFor(userInput.get())).grid(column=1,row=0)