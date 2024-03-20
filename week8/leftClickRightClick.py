import tkinter

window = tkinter.Tk()
window.title("Come on! Click away!")


def left_click(event):
    tkinter.Label(window, text="You clicked the left one!").pack()


def middle_click(event):
    tkinter.Label(window, text="You clicked the middle one!").pack()


def right_click(event):
    tkinter.Label(window, text="You clicked the right one!").pack()


window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)

window.mainloop()
