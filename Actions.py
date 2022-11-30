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
        addRecord(app, isbn.get(), author.get(), title.get())
        app.loadRecords()
        top.destroy()
    Button(top, text="Add", command=sendRecord).pack(padx=10)

def seachListByIsbn(list, key):
    i = 0
    for x in list:
        if x[0] == key:
            return i
        i += 1
    return -1

def deleteRecord(app):
    if app.selectedRecord != {}:
        recordIndex = app.indexIsbnList[seachListByIsbn(app.indexIsbnList, app.selectedRecord["data"][0])][1]
        app.AVAIL.append(recordIndex)
        app.indexIsbnList.remove([app.selectedRecord["data"][0],recordIndex])
        app.indexTitleList.remove([app.selectedRecord["data"][2],recordIndex])
        fl = open("./data/BookRecords.txt", "r+")
        fl.seek(51 * int(recordIndex))
        fl.write('{r:{c}<{n}}'.format(r=recordIndex, n=50, c='-'))
        fl.close()
        app.loadRecords()
        app.selectedRecord = {}
    else:
        print("no selected record")

def placeActions(app):
    sideF = ttk.Frame(app.root)
    sideF.grid(column=1, row=0, sticky=N)
    Label(sideF, text="Actions").grid(row=0, ipadx=12, ipady=4)
    ttk.Button(sideF, text="Add", command=lambda: popAddWin(app)).grid(row=1)
    ttk.Button(sideF, text="Delete", command=lambda: deleteRecord(app)).grid(row=2)