import tkinter
import csv

class Survey(object):
    '''this is for making the survey that Sierra wanted'''
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.grid()
        self.create()
        self.root.mainloop()
        
    def create(self):
        #questions credited to Sierra Rivas(no longer on team)
        tkinter.Label(self.root,text='First Name').grid(row=0,column=0)
        self.fNameText = tkinter.Entry(self.root,width=30).grid(row=0,column=1)
        
        tkinter.Label(self.root,text='Middle Name').grid(row=1,column=0)
        self.mNameText = tkinter.Entry(self.root,width=30).grid(row=1,column=1)
        
        tkinter.Label(self.root,text='Last Name').grid(row=2,column=0)
        self.lNameText = tkinter.Entry(self.root,width=30).grid(row=2,column=1)
        
        tkinter.Label(self.root,text='Age').grid(row=3,column=0)
        self.ageText = tkinter.Entry(self.root,width=30).grid(row=3,column=1)
        
        tkinter.Label(self.root,text='Race: (Asain, Native America, African\
        American, Hispanic, Caucasian)').grid(row=4,column=0)
        self.raceText = tkinter.Entry(self.root,width=30).grid(row=4,column=1)
        
        tkinter.Label(self.root,
                      text='"Gender: (Male, Female, Other)"').grid(row=5,
                                                                   column=0)
        self.genderText = tkinter.Entry(self.root,width=30).grid(row=5,column=1)
        tkinter.Button(self.root,text='Submit',
                       command=self.submit).grid(row=6,column=3)
    
    def submit(self):
        '''for submitting to a csv file'''
        pass
        '''with open('survey.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.fNameText.get(),self.mNameText.get(),
                             self.lNameText.get(),self.ageText.get(),
                             self.raceText.get(),self.genderText.get()])'''
def button():
    top.destroy()
    Survey()
top = tkinter.Tk()
top.grid()
tkinter.Button(top,text='Click here to start survey',command=button).grid()
top.mainloop()