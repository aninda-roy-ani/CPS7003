import tkinter
from tkinter import *
window = tkinter.Tk()
window.title("Choose Database")
Check_1 = IntVar()
Check_2 = IntVar()
tkinter.Checkbutton(window, text="Relational database", variable=Check_1, onvalue=0, offvalue=1).grid(row=0)
tkinter.Checkbutton(window, text="No-SQL database", variable=Check_2, onvalue=0, offvalue=1).grid(row=1)
window.mainloop()