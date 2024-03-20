import tkinter

window = tkinter.Tk()
window.title("Button GUI")


def ClickAni():
    tkinter.Label(window, text="Such a nice innocent cute guy!").pack()
def ClickAlishba():
    tkinter.Label(window, text="Bad girl!").pack()

def ClickUsama():
    tkinter.Label(window, text="So straight, man!").pack()


tkinter.Button(window, text="SEE HOW ANI IS!", command=ClickAni).pack()
tkinter.Button(window, text="SEE HOW ALISHBA IS!", command=ClickAlishba).pack()
tkinter.Button(window, text="SEE HOW USAMA IS!", command=ClickUsama).pack()
window.mainloop()
