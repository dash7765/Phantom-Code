import csv
import matplotlib.pyplot as plt
import pylab as py
import numpy as np
import matplotlib
import xlrd

# Pulls values from Client Dataset.xlsx cells
def find_cell_client(column, row):
    book = xlrd.open_workbook("Client Dataset.xlsx") # Sets what file it will get the data from
    first_sheet = book.sheet_by_index(0) # Makes sure data is taken from the first sheet
    particular_cell_value = first_sheet.cell(column,row).value #gives value to a variable
    return particular_cell_value

# Pulls values from EmploymentEducation.xlsx cells
def find_cell_employment(column, row):
    book = xlrd.open_workbook("EmploymentEducation Dataset.xlsx")
    first_sheet = book.sheet_by_index(0)
    particular_cell_value = first_sheet.cell(column,row).value
    return particular_cell_value

# Pulls values from HealthAndDV.xlsx cells
def find_cell_health(column, row):
    book = xlrd.open_workbook("HealthAndDV Dataset.xlsx")
    first_sheet = book.sheet_by_index(0)
    particular_cell_value = first_sheet.cell(column,row).value
    return particular_cell_value

def call_data(data):
    out = []
    #list with valid dictionary
    with open(data) as f:
        reader = csv.reader(f)
        out.append(reader[0])
    with open(data, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
    return out
'''
#Removed because we called the data in graphs instead
def call_client():
    out = []
    with open('Sample Dataset - Client.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out
            
def call_disabilities():
    out = []
    with open('Sample Dataset - Disabilities.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out
            
def call_unemployment_education():
    out = []
    with open('Sample Dataset - EmploymentEducation.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out
            
def call_enrollment():
    out = []
    with open('Sample Dataset - Enrollment.csv', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out
            
def call_exit():
    out = []
    with open('Sample Dataset - Exit.csv', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out
            
def call_funder():
    out = []
    with open('Sample Dataset - Funder.csv', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out
            
def call_health_dv():
    out = []
    with open('Sample Dataset - HealthAndDV.csv', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out
            
def call_income_benefits():
    out = []
    with open('Sample Dataset - IncomeBenefits.csv', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out

def call_services():
    out = []
    with open('Sample Dataset - Services.csv', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            out.append(row)
        return out

#Failed Attempt To make histograms
# Matplotlib
n_bins = 10
x = np.random.randn(1000, 3)

fig, axes = plt.subplots(nrows=4, ncols=2)
ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7 = axes.flat

# Make a multiple-histogram of data-sets with different length.
x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]

ax0.hist(x_multi, n_bins, histtype='bar')
ax0.set_title('Chart 1')
ax0.set_xlabel('X Axis 1')
ax0.set_ylabel('Y Axis 1')

ax1.hist(x_multi, n_bins, histtype='bar')
ax1.set_title('Chart 2')
ax1.set_xlabel('X Axis 2')
ax1.set_ylabel('Y Axis 2')

ax2.hist(x_multi, n_bins, histtype='bar')
ax2.set_title('Chart 3')
ax2.set_xlabel('X Axis 3')
ax2.set_ylabel('Y Axis 3')

ax3.hist(x_multi, n_bins, histtype='bar')
ax3.set_title('Chart 4')
ax3.set_xlabel('X Axis 4')
ax3.set_ylabel('Y Axis 4')

ax4.hist(x_multi, n_bins, histtype='bar')
ax4.set_title('Chart 5')
ax4.set_xlabel('X Axis 5')
ax4.set_ylabel('Y Axis 5')

ax5.hist(x_multi, n_bins, histtype='bar')
ax5.set_title('Chart 6')
ax5.set_xlabel('X Axis 6')
ax5.set_ylabel('Y Axis 6')

ax6.hist(x_multi, n_bins, histtype='bar')
ax6.set_title('Chart 7')
ax6.set_xlabel('X Axis 7')
ax6.set_ylabel('Y Axis 7')

ax7labels=['jan','feb','mar','apr']
ax7.xticks(x, ax7labels)
ax7.hist(x_multi, n_bins, histtype='bar')
ax7.set_
ax7.set_title('Chart 8')
ax7.set_xlabel('X Axis 8')
ax7.set_ylabel('Y Axis 8')

plt.tight_layout()
plt.show()
'''
# Makes a chart compaing number of males and females
def gender_chart():
        fig = py.figure() # Makes the table
        x = [1, 2] # Set number of variables on x
        y = [find_cell_client(303,15), find_cell_client(305,15)] # Calls values from specific cells from Client Dataset.xlsx
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.bar(x, y, align='center') #Centers chart so data can be seen
        ax.set_title('Gender of Homeless') # Gives a title
        ax.set_ylabel('Number of People') # Labels the Y - Axis
        ax.set_xlabel('Gender') # Lables the X - Axis
        ax.set_xticks(x) # Allows to list strings on X - Axis
        ax.set_xticklabels(['Male', 'Female']) # Sets strings on X - Axis
        fig.show() # Shows the graph

# See gender_chart() for reference of code for any of the other charts    
def veteran_status_chart():
    fig = py.figure()
    x = [1, 2]
    y = [find_cell_client(303,17), find_cell_client(305,15)]
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x, y, align='center')
    ax.set_title('Homeless Veterans')
    ax.set_ylabel('Number of People')
    ax.set_xlabel('Veteran Status')
    ax.set_xticks(x)
    ax.set_xticklabels(['Veteran', 'Not Veteran'])
    fig.show()    
    
def race_chart():
    fig = py.figure()
    x = [1, 3, 5, 7, 9]
    y = [find_cell_client(303,9), find_cell_client(303,10), find_cell_client(303,11), find_cell_client(303,12), find_cell_client(303,13)]
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x, y, align='center')
    ax.set_title('Races of Homeless')
    ax.set_ylabel('Number of People')
    ax.set_xlabel('Race')
    ax.set_xticks(x)
    ax.set_xticklabels(['Native American', 'Asian American', 'African American', 'Native Hispanic', 'Caucasian'])
    fig.show()
    
def employment_chart():
        fig = py.figure()
        x = [1, 2, 3]
        y = [find_cell_employment(194,6), find_cell_employment(196,6), find_cell_employment(198,6)]
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.bar(x, y, align='center')
        ax.set_title('Employment of Homeless')
        ax.set_ylabel('Number of People')
        ax.set_xlabel('Employment Status')
        ax.set_xticks(x)
        ax.set_xticklabels(['Not Employed', 'Employed', 'Client Unsure'])
        fig.show()

def prior_residence_chart():
    
    fig = py.figure()
    x = [1, 2, 3]
    y = [179, 1, 117]
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.bar(x, y, align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(['Homeless Situation','Institutional Care', 'Transitional And Permenant Housing Situation'])
    fig.show()
    
def domestic_abuse_chart():
        fig = py.figure()
        x = [1, 2, 3]
        y = [find_cell_health(434,4), find_cell_health(432,4), find_cell_health(436,4)]
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.bar(x, y, align='center')
        ax.set_title('Domestic Abuse In Homeless')
        ax.set_ylabel('Number of People')
        ax.set_xlabel('Domestic Abuse Victim')
        ax.set_xticks(x)
        ax.set_xticklabels(['Yes','No', 'Doesn\'t Know'])
        fig.show()    
'''
Removed because code that used it was removed
Lined up the text on the bargraphs
def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
            '%d' % int(height),
            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)
        plt.show()'''
        