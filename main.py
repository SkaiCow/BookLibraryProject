from tkinter import *
from tkinter import ttk
from SearchManager import *
from Actions import *


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
        placeActions(self.root)
        mainF = ttk.Frame(self.root, borderwidth=2, width=200, height=100, relief='sunken')
        mainF.pack(fill="both", expand=True)
        recordBox = ttk.Frame(mainF, height=20)
        recordBox.pack(fill="x")
        ttk.Label(recordBox, text="ISBN").pack(side="left", anchor="w", expand=True, fill="both")
        ttk.Label(recordBox, text="Author").pack(side="left", anchor="w", expand=True, fill="both")
        ttk.Label(recordBox, text="Book Title").pack(side="left", anchor="w", expand=True, fill="both")

        self.root.mainloop()

if __name__ == "__main__":
    app()
