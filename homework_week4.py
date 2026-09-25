#imports libraries

import math 
import numpy as np

def count_solar_activity(t, t0, c, a, p): #function to calculate sunspot numbers per time unit
    return a*math.sin(2*math.pi/p*(t-t0))+c #returns result

def task1():
    total_time=10*11*12 #time in months
    t0=0 #phase_shift
    c=np.random.normal(100, 10, total_time) #avg num of sun spots
    a=20 #amplitude of the cycle
    p=11*12 #period of the cycle in months
    filename="solar_cycle_simulation.txt" #file name for pseudodata
    pseudodata=[] #list to store pseudodata
    for t in range(total_time): #runs cycle for every month in simulation
        pseudodata.append(count_solar_activity(t, t0, c[t], a, p)) #adds generated data for each month to list
    np.savetxt(filename, pseudodata) #saves list to file
    print(f"Pseudodata is now saved on your computer in file '{filename}'!\nCheck it out!") #informs user that task is finished
    return filename #returns filename for future use

def task2(filename):
    with open (filename, "r") as file: #opens the file using the ame from first task
        dataset=file.read() #saves the data in a variable
    dataset=np.array(dataset.split(), dtype=float) #transforms data into an array 
    subsamples=np.split(dataset, 10) #splits data in 10 subsamples
    sample_average=[] #creates list to store subsample averages
    sample_uncertainty=[] #creates list to store subsample average uncertanties 
    for sample in subsamples: #iterates over array of subsamples
        sample_average.append(np.average(sample)) #calculates average of each subsample and adds to list
        sample_uncertainty.append(np.std(sample)) #calculates uncertainty of average for each subsample and adds to list
    avg_per_cycle=np.array([sample_average, sample_uncertainty]) #combines averages and uncertanties into 1 numpy array
    
    final_average=np.mean(avg_per_cycle[0]) #calculates the final average over all cycles using subsample methods
    final_uncertainty=np.std(avg_per_cycle[0]) #calculates the uncertainty for final average
    i=0 #index go count cycles
    print("Cycle  Average per cycle") #prints header for result output
    for a, u in zip(sample_average, sample_uncertainty): #iterates over lists of sample averages and uncertanties for averages per every subsample
        i+=1 #increases index
        print(i, a, "±", u) #prints the averages and unc for each subsample
    
    print(f"\nOn average there are {final_average} ± {final_uncertainty} solar spots per month in 11 year cycle!") #informs user about final average

#prints the titles and runs tasks for user
print("-- Task 1 --\n")
filename=task1()
print("-- Task 2 --\n")
task2(filename)
