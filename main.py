from tkinter import *
from tkinter import ttk
from SearchManager import *
from Actions import *
from FileManager import getAllRecords

class app:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x400")
        self.root.title('Book Library')

        placeSearchBar(self)
        placeActions(self)
        self.mainF = ttk.Frame(self.root, borderwidth=2, width=200, height=100, relief='sunken')
        self.mainF.pack(fill="both", expand=True)
        recordBox = ttk.Frame(self.mainF, height=20)
        recordBox.pack(fill="x")
        ttk.Label(recordBox, text="ISBN").pack(side="left", anchor="w", expand=True, fill="both")
        ttk.Label(recordBox, text="Author").pack(side="left", anchor="w", expand=True, fill="both")
        ttk.Label(recordBox, text="Book Title").pack(side="left", anchor="w", expand=True, fill="both")
        self.recordContainer = ttk.Frame(self.mainF)
        self.recordContainer.pack(expand=True, fill="both")
        self.loadRecords()

        self.root.mainloop()
    def loadRecords(self):
        self.clearRecords()
        for book in getAllRecords():
            recordBox = ttk.Frame(self.recordContainer, height=20)
            recordBox.pack(fill="x")
            ttk.Label(recordBox, text=book[0], justify="left", background="blue").pack(side="left", expand=True)
            ttk.Label(recordBox, text=book[1], justify="left", background="red").pack(side="left", expand=True)
            ttk.Label(recordBox, text=book[2], justify="left", background="green").pack(side="left", expand=True)
    def clearRecords(self):
        for item in self.recordContainer.winfo_children():
            item.destroy()


if __name__ == "__main__":
    app()
