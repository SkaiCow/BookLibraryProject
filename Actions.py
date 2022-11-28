from tkinter import *
from tkinter import ttk

def popAddWin(win):
    top= Toplevel(win)
    top.geometry("150x170")
    top.title("Add Book Window")
    Label(top, text= "ISBN", font=('Mistral 12 bold')).pack(anchor="w", padx=10)

    Entry(top).pack(anchor="w", padx=10)
    Label(top, text= "Author", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
    Entry(top).pack(anchor="w", padx=10)
    Label(top, text= "Book Title", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
    Entry(top).pack(anchor="w", padx=10)
    def addRecord():
        #add data to file. this will probably go else where
        print("sending data...")
        top.destroy()
    Button(top, text="Add", command=addRecord).pack(padx=10)


def placeActions(root):
    sideF = ttk.Frame(root)
    sideF.pack(side="right", fill="both")
    Label(sideF, text="Actions").pack(ipadx=12, ipady=4)
    ttk.Button(sideF, text="Add", command=lambda: popAddWin(root)).pack()
    ttk.Button(sideF, text="Delete").pack()