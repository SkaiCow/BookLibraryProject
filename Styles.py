from tkinter import *
from tkinter import ttk

def loadStyles(root):
    styles = ttk.Style(root)

    styles.configure('selected.TFrame', background="lightblue")
    styles.configure('selected.TLabel', background="lightblue")