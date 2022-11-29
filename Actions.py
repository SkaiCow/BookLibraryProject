from tkinter import *
from tkinter import ttk
from FileManager import addRecord
def popAddWin(app):
    top= Toplevel(app.root)
    top.geometry("150x170")
    top.title("Add Book Window")
    def on_closing():
        print("cancel add record")
        top.destroy()
    top.protocol("WM_DELETE_WINDOW", on_closing)
    Label(top, text= "ISBN", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
    isbn = StringVar()
    Entry(top, textvariable=isbn).pack(anchor="w", padx=10)
    Label(top, text= "Author", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
    author = StringVar()
    Entry(top, textvariable=author).pack(anchor="w", padx=10)
    Label(top, text= "Book Title", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
    title = StringVar()
    Entry(top, textvariable=title).pack(anchor="w", padx=10)
    def sendRecord():
        print("sending data...")
        addRecord(isbn.get(), author.get(), title.get())
        app.loadRecords()
        top.destroy()
    Button(top, text="Add", command=sendRecord).pack(padx=10)


def placeActions(app):
    sideF = ttk.Frame(app.root)
    sideF.pack(side="right", fill="both")
    Label(sideF, text="Actions").pack(ipadx=12, ipady=4)
    ttk.Button(sideF, text="Add", command=lambda: popAddWin(app)).pack()
    ttk.Button(sideF, text="Delete").pack()