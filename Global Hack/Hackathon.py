import csv
import matplotlib.pyplot as plt

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
    
# Matplotlib

fig = plt.figure()

x = 200 + 25*plt.randn(1000)
y = 150 + 25*plt.randn(1000)
n, bins, patches = plt.hist([x, y])

plot_url = py.plot_mpl(fig, filename='docs/mpl-histogram')