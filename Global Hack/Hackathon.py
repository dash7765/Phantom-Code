import csv
import matplotlib.pyplot as plt
import pylab as py
import numpy as np


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
#Gender Chart

def gender_chart():
    Male = (20, 35, 10)

    ind = np.arange(3)  # number of variables on x
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, Male, width, color='b', yerr = 1)

    Female = (25, 32, 10)
    rects2 = ax.bar(ind + width, Female, width, color='y', yerr=1)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Gender')
    ax.set_xlabel('X Axis')
    ax.set_title('Gender')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(('Male', 'Female', 'Other'))

    ax.legend((rects1[0], rects2[0]), ('Male', 'Female'))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
            '%d' % int(height),
            ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)
        plt.show()
            