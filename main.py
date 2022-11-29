from tkinter import *
from tkinter import ttk
from SearchManager import *
from Actions import *
from FileManager import getAllRecords
from Styles import loadStyles

class app:
    def __init__(self):
        #app data
        self.selectedRecord = {}

        self.root = Tk()
        self.root.geometry("600x400")
        self.root.title('Book Library')
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

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
    def loadRecords(self):
        self.clearRecords()
        def selectRecord(event):
                if self.selectedRecord != {}:
                    self.selectedRecord["frame"].configure(style="TFrame")
                    for l in self.selectedRecord["frame"].winfo_children():
                        l.configure(style="TLabel")
                frame = event.widget
                frame.configure(style="selected.TFrame")
                bookData = []
                for l in frame.winfo_children():
                    bookData.append(l.cget("text"))
                    l.configure(style="selected.TLabel")
                self.selectedRecord = {"frame":frame, "data": bookData}
        for book in getAllRecords():
            recordBox = ttk.Frame(self.recordContainer, height=20)
            recordBox.pack(fill="x")
            recordBox.bind("<Button-1>", selectRecord)
            recordBox.columnconfigure(0, weight=1, uniform="fred")
            recordBox.columnconfigure(1, weight=1, uniform="fred")
            recordBox.columnconfigure(2, weight=1, uniform="fred")
            ttk.Label(recordBox, text=book[0]).grid(column=0, row=0, sticky=W)
            ttk.Label(recordBox, text=book[1]).grid(column=1, row=0, sticky=W)
            ttk.Label(recordBox, text=book[2]).grid(column=2, row=0, sticky=W)
    def clearRecords(self):
        for item in self.recordContainer.winfo_children():
            item.destroy()


if __name__ == "__main__":
    app()
