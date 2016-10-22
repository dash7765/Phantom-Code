import csv

def call_client():
    with open('Sample Dataset - Client.csv', newline='') as f:
        for row in csv.reader(f):
            print(row)
            
def call_disabilities():
    with open('Sample Dataset - Disabilities.csv', newline='') as f:
        for row in csv.reader(f):
            print(row)
            
def call_unemployment_education():
    with open('Sample Dataset - EmploymentEducation.csv', newline='') as f:
        for row in csv.reader(f):
            print(row)
            
def call_enrollment():
    with open('Sample Dataset - Enrollment.csv', newline = '') as f:
        for row in csv.reader(f):
            print(row)
            
def call_exit():
    with open('Sample Dataset - Exit.csv', newline = '') as f:
        for row in csv.reader(f):
            print(row)
            
def call_funder():
    with open('Sample Dataset - Funder.csv', newline = '') as f:
        for row in csv.reader(f):
            print(row)
            
def call_health_dv():
    with open('Sample Dataset - HealthAndDV.csv', newline = '') as f:
        for row in csv.reader(f):
            print(row)
            
def call_income_benefits():
    with open('Sample Dataset - IncomeBenefits.csv', newline = '') as f:
        for row in csv.reader(f):
            print(row)

def call_services():
    with open('Sample Dataset - Services.csv', newline = '') as f:
        for row in csv.reader(f):
            print(row)