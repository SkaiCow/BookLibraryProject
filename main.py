from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("600x400")
root.title('Book Library')

#build window
#bottomBar
bottomF = ttk.Frame(root)
bottomF.pack(side = "bottom", fill="x")
ttk.Entry(bottomF, text="where am i").pack(side="left", expand=True, fill="both")
ttk.Button(bottomF, text="Search").pack(side="right")

#sideBar
sideF = ttk.Frame(root)
sideF.pack(side="right", fill="both")
Label(sideF, text="Actions").pack(ipadx=12, ipady=4)
ttk.Button(sideF, text="Add").pack()
ttk.Button(sideF, text="Delete").pack()

#main Frame
mainF = ttk.Frame(root, borderwidth=2, width=200, height=100, relief='sunken')
mainF.pack(fill="both", expand=True)

recordBox = ttk.Frame(mainF, height=20)
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
#ttk.Style().configure("TLabel", background="#6d6875", foreground="#e5989b")




root.mainloop()
