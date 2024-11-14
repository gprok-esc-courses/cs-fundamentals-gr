
from tkinter import Tk, Label, Entry, Button

def button_clicked():
    txt = entry.get()
    label.configure(text=txt)

window = Tk()

label = Label(window, text='-')
label.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=1, column=0)

button = Button(window, text='Click Me', command=button_clicked)
button.grid(row=2, column=0)

window.mainloop()
