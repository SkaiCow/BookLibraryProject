from tkinter import *
from tkinter import ttk

class SearchManager:
    def _init__(self, root):
        bottomF = ttk.Frame(root)
        bottomF.pack(side = "bottom", fill="x")
        ttk.Entry(bottomF, text="where am i").pack(side="left", expand=True, fill="both")
        ttk.Button(bottomF, text="Search").pack(side="right")

def searchFor(data):
    print("we are looking now! : " + str(data))

def placeSearchBar(root):
    bottomF = ttk.Frame(root)
    bottomF.pack(side = "bottom", fill="x")
    userInput = StringVar()
    ttk.Entry(bottomF, textvariable=userInput).pack(side="left", expand=True, fill="both")
    ttk.Button(bottomF, text="Search", command=lambda: searchFor(userInput.get())).pack(side="right")