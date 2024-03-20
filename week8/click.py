import tkinter

window = tkinter.Tk()
window.title("Button GUI")

def ClickButton():
    tkinter.Label(window,text="You have clicked the button!").pack()

tkinter.Button(window, text="Click the button!", command=ClickButton).pack()
window.mainloop()