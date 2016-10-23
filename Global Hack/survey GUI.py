import tkinter
from time import sleep

class Survey(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.grid()
        self.create()
    def create(self):
        tkinter.Label(self.root,text='Name').grid(row=0,column=0)
        self.nameText = tkinter.Text(self.root,width=30).grid(row=0,column=1)
def button():
    top.destroy()
    Survey()
top = tkinter.Tk()
top.grid()
tkinter.Button(top,text='Click here to start survey',command=button).grid()
top.mainloop()