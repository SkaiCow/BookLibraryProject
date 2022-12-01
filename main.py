from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image as PILImage
from SearchManager import *
from Actions import *
from FileManager import *
from Styles import loadStyles

class app:
    def __init__(self):
        #app data
        self.selectedRecord = None
        self.AVAIL = []
        self.indexIsbnList = loadIsbnIndexFile()
        self.indexTitleList = loadTitleIndexFile()
        self.editImages = []

        self.root = Tk()
        self.root.geometry("600x400")
        self.root.title('Book Library')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        def on_closing():
            crushRecordFile(self)
            writeToIndexfile(self.indexIsbnList, self.indexTitleList)
            self.root.destroy()
        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        loadStyles(self.root)

        placeSearchBar(self)
        placeActions(self)
        
        #main Frame
        self.mainF = ttk.Frame(self.root, borderwidth=2, relief='sunken')
        self.mainF.grid(column=0, row=0, sticky=NSEW)
        self.mainF.columnconfigure(0, weight=1)
        self.mainF.rowconfigure(1, weight=1)

        #table col titles
        recordBox = Frame(self.mainF, height=20)
        recordBox.grid(row=0, sticky=EW)
        recordBox.columnconfigure(0, weight=1)
        recordBox.columnconfigure(1, weight=1)
        recordBox.columnconfigure(2, weight=1)
        ttk.Label(recordBox, text="ISBN").grid(column=0, row=0)
        ttk.Label(recordBox, text="Author").grid(column=1, row=0)
        ttk.Label(recordBox, text="Book Title").grid(column=2, row=0)

        self.recordContainer = Frame(self.mainF)
        self.recordContainer.grid(column=0, row=1, sticky=NSEW)
        self.loadRecords()

        self.root.mainloop()
    def loadRecords(self, filterlist = None):
        self.clearRecords()
        def selectRecord(event):
                if self.selectedRecord != None:
                    self.selectedRecord["frame"].configure(style="TFrame")
                    l = self.selectedRecord["frame"].winfo_children()
                    l[0].configure(style="TLabel")
                    l[1].configure(style="TLabel")
                    l[2].configure(style="TLabel")
                frame = event.widget
                frame.configure(style="selected.TFrame")
                l = frame.winfo_children()
                l[0].configure(style="selected.TLabel")
                l[1].configure(style="selected.TLabel")
                l[2].configure(style="selected.TLabel")
                self.selectedRecord = {"frame":frame, "data": [l[0].cget("text"),l[1].cget("text"),l[2].cget("text")]}
        def editRecord(event):
            frame = event.widget
            recordBox = frame.master.winfo_children()
            self.editRecordPopUp(recordBox[0].cget("text"))
            #print([recordBox[0].cget("text"),recordBox[1].cget("text"),recordBox[2].cget("text")])
        if filterlist == None:
            filterlist = getAllRecords(self)
        for book in filterlist:
            recordBox = ttk.Frame(self.recordContainer, height=20)
            recordBox.pack(fill="x")
            recordBox.bind("<Button-1>", selectRecord)
            recordBox.columnconfigure(0, weight=1, uniform="fred")
            recordBox.columnconfigure(1, weight=1, uniform="fred")
            recordBox.columnconfigure(2, weight=1, uniform="fred")
            ttk.Label(recordBox, text=book[0]).grid(column=0, row=0, sticky=W)
            ttk.Label(recordBox, text=book[1]).grid(column=1, row=0, sticky=W)
            ttk.Label(recordBox, text=book[2]).grid(column=2, row=0, sticky=W)
            editPicture = PILImage.open("./images/edit.png")
            editPicture = editPicture.resize((15,15))
            editPicture = ImageTk.PhotoImage(editPicture)
            self.editImages.append({"image":editPicture, "record":recordBox})
            editButton = Label(recordBox, image=self.editImages[-1]["image"])
            editButton.grid(column=3, row=0)
            editButton.bind("<Button-1>", editRecord)
    def clearRecords(self):
        for item in self.recordContainer.winfo_children():
            item.destroy()
    def searchByIsbn(self, key):
        self.selectedRecord = None
        results = findRecordByIsbn(self, key)
        if results is not None:
            self.loadRecords([results])
        else:
            print("No Record Found")

    def searchByTitle(self, key):
        self.selectedRecord = None
        results = findRecordByTitle(self, key)
        if results is not None:
            self.loadRecords([results])
        else:
            print("No Record Found")
    def editRecordPopUp(self, isbn):
        top= Toplevel(self.root)
        top.geometry("150x170")
        top.title("Edit Book Window")
        def on_closing():
            print("cancel edit record")
            top.destroy()
        top.protocol("WM_DELETE_WINDOW", on_closing)
        oldRecord = findRecordByIsbn(self, isbn)
        for x in self.indexIsbnList:
            if x[0] == isbn:
                indexOfRecord = x[1]
        Label(top, text= "ISBN", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
        isbn = StringVar(value=oldRecord[0])
        Entry(top, textvariable=isbn).pack(anchor="w", padx=10)
        Label(top, text= "Author", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
        author = StringVar(value=oldRecord[1])
        Entry(top, textvariable=author).pack(anchor="w", padx=10)
        Label(top, text= "Book Title", font=('Mistral 12 bold')).pack(anchor="w", padx=10)
        title = StringVar(value=oldRecord[2])
        Entry(top, textvariable=title).pack(anchor="w", padx=10)
        def sendRecord():
            editRecordFile(app, isbn.get(), author.get(), title.get(), int(indexOfRecord))
            self.loadRecords()
            top.destroy()
        Button(top, text="Done", command=sendRecord).pack(padx=10)
        


if __name__ == "__main__":
    app()
