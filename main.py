from tkinter import *
from tkinter import ttk
from SearchManager import *
from Actions import *
from FileManager import getAllRecords


"""recordBox = ttk.Frame(mainF, height=20)
recordBox.pack(fill="x")
ttk.Label(recordBox, text="ISBN").pack(side="left", anchor="w", expand=True, fill="both")
ttk.Label(recordBox, text="Author").pack(side="left", anchor="w", expand=True, fill="both")
ttk.Label(recordBox, text="Book Title").pack(side="left", anchor="w", expand=True, fill="both")
#record Box
recordBox = ttk.Frame(mainF, height=20)
recordBox.pack(fill="x")
ttk.Label(recordBox, text="0717802418").pack(side="left", anchor="w", expand=True, fill="both")
ttk.Label(recordBox, text="Karl Marx").pack(side="left", anchor="w", expand=True, fill="both")
ttk.Label(recordBox, text="The Communist Manifesto").pack(side="left", anchor="w", expand=True, fill="both")

#ttk.Style().configure("TFrame", background="#6d6875")
#ttk.Style().configure("TLabel", background="#6d6875", foreground="#e5989b")"""

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
        self.loadRecords()

        self.root.mainloop()
    def loadRecords(self):
        for item in self.mainF.winfo_children():
            item.destroy()
        recordBox = ttk.Frame(self.mainF, height=20)
        recordBox.pack(fill="x")
        ttk.Label(recordBox, text="ISBN").pack(side="left", anchor="w", expand=True, fill="both")
        ttk.Label(recordBox, text="Author").pack(side="left", anchor="w", expand=True, fill="both")
        ttk.Label(recordBox, text="Book Title").pack(side="left", anchor="w", expand=True, fill="both")
        for book in getAllRecords():
            recordBox = ttk.Frame(self.mainF, height=20)
            recordBox.pack(fill="x")
            ttk.Label(recordBox, text=book[0]).pack(side="left", anchor="w", expand=True, fill="both")
            ttk.Label(recordBox, text=book[1]).pack(side="left", anchor="w", expand=True, fill="both")
            ttk.Label(recordBox, text=book[2]).pack(side="left", anchor="w", expand=True, fill="both")


if __name__ == "__main__":
    app()
