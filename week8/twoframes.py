import tkinter

window = tkinter.Tk()
window.title("Button GUI app")
top = tkinter.Frame(window).pack()
bottom = tkinter.Frame(window).pack(side="bottom")
btn0 = tkinter.Button(top, text = "Hello!", fg = "red").pack()
btn1 = tkinter.Button(top, text = "How are you?", fg = "green").pack()
btn2 = tkinter.Button(bottom, text="Beautiful Day!", fg = "purple").pack(side="left")
btn3 = tkinter.Button(bottom, text="Bad Day!", fg = "blue").pack(side="right")
window.config(bg="#9e3206")
window.mainloop()