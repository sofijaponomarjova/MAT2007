import math ##math library for formula
import csv #csv to work with files

def calculate_remaining_atoms(N0, lam, t):
    return N0*math.exp(-lam*t)
    


def write_to_file(file_name, data):
    with open(file_name, 'w', newline='') as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(["Time (s)", "Reamaining Atoms"])
            csvwriter.writerows(data)

def read_file(file):
     with open(file, 'r', newline='') as csvfile:
        csvreader=csv.reader(csvfile)
        all_data=list(csvreader)
        return all_data


def task1():
    N0=1000
    lam=0.1
    t=0
    data=[]
    file_name='radioactive_decay.csv'
    while t<=50:
        Nt=calculate_remaining_atoms(N0, lam, t)
        data.append([t, Nt])
        t+=1
    write_to_file(file_name, data)
    extracted_results=read_file(file_name)[1:]
    for row in extracted_results:
        row[0]=int(row[0])
        row[1]=float(row[1])
    print(extracted_results==data)

task1()