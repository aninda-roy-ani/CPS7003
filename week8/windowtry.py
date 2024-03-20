import tkinter

window = tkinter.Tk()
window.title("Button GUI app")
#label = tkinter.Label(window, text="Welcome to your very own GUI app!!").pack()
button_widget = tkinter.Button(window, text="Welcome with a button")
button_widget.pack()
window.config(bg="#9e3206")
window.mainloop()