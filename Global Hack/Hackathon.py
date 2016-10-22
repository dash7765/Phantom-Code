import csv
import matplotlib.pyplot as plt
import pylab as py
import numpy as np

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
'''    
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
ax0.axis([0,20,0,20])

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

ax7.hist(x_multi, n_bins, histtype='bar')
ax7.set_title('Chart 8')
ax7.set_xlabel('X Axis 8')
ax7.set_ylabel('Y Axis 8')

plt.tight_layout()
plt.show()
'''
DayOfWeekOfCall = [1,2,3]
DispatchesOnThisWeekday = [77, 32, 42]
LABELS = ["Monday", "Tuesday", "Wednesday"]
py.bar(DayOfWeekOfCall, DispatchesOnThisWeekday)
py.xticks(DayOfWeekOfCall, LABELS)
py.show()
