from tkinter import *
from tkinter import ttk
from FileManager import findRecordByIsbn

def placeSearchBar(app):
    def searchFor(data):
        print("we are looking now! : " + str(data))
        findRecordByIsbn(data)
    bottomF = ttk.Frame(app.root)
    bottomF.pack(side = "bottom", fill="x")
    userInput = StringVar()
    ttk.Entry(bottomF, textvariable=userInput).pack(side="left", expand=True, fill="both")
    ttk.Button(bottomF, text="Search", command=lambda: searchFor(userInput.get())).pack(side="right")