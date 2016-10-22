#import Hackathon
#taken out... for some reason it stops the GUI from loading

import tkinter

def break_fix_gender():
    '''fixes the problem with importing'''
    import Hackathon
    Hackathon.gender_chart()
        
top = tkinter.Tk()
top.width = 600
top.height = 600
top.grid()
tkinter.Button(top, bg='orange',text='Gender Chart',
               command=break_fix_gender).grid(row=0,column=0)

top.mainloop()
