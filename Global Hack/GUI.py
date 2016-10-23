#import Hackathon
#taken out... for some reason it stops the GUI from loading

import tkinter

def button_gender():
    '''fixes the problem with importing'''
    import Hackathon
    Hackathon.gender_chart()

def button_veteran_status():
    '''fixes the problem with importing'''
    import Hackathon
    Hackathon.veteran_status_chart()

def button_race():
    '''fixes the problem with importing'''
    import Hackathon
    Hackathon.race_chart()

def button_employment():
    '''fixes the problem with importing'''
    import Hackathon
    Hackathon.employment_chart()
    
def button_prior_residence():
    '''fixes the problem with importing'''
    import Hackathon
    Hackathon.prior_residence_chart()
    
def button_domestic_abuse():
    '''fixes the problem with importing'''
    import Hackathon
    Hackathon.domestic_abuse_chart()
    
    
top = tkinter.Tk()
top.width = 600
top.height = 600
top.grid()
tkinter.Button(top, bg='orange',text='Gender Chart',
               command=button_gender).grid()
tkinter.Button(top, bg='orange',text='Veteran Status Chart',
               command=button_veteran_status).grid()
tkinter.Button(top, bg='orange',text='Race Chart',
               command=button_race).grid()
tkinter.Button(top, bg='orange',text='Employment Chart',
               command=button_employment).grid()
tkinter.Button(top, bg='orange',text='Prior Residence Chart',
               command=button_prior_residence).grid()
tkinter.Button(top, bg='orange',text='Domestic Abuse Chart',
               command=button_domestic_abuse).grid()

top.mainloop()
