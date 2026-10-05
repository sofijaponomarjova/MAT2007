#Importing libraries
import numpy as np
import math
import statistics
import matplotlib.pyplot as plt

#formula to calculate the concentration at a time point
def formula(C0, k, t):
    return C0*(1/np.exp(k*t))

def main():
    #defining the variables required to calculate the concentration
    k=0.1
    time=60
    t=np.arange(0,time,1) #making a list of time points
    n_runs=100 #number of runs
    
    for i in range(n_runs): 
        filename="file"+str(i)+".txt" #creates a filename for each one of 100 files
        C0=np.random.normal(1, 0.1, 1) #draws the initial concentration for each of the simulations
        results=formula(C0, k, t) #simulates the concentration over all time points
        np.savetxt(filename, results) #saves the results in the text file
    average=[] #creates list for averages
    uncertainties=[] #creates list for uncertainties

    simulation_results=np.zeros((n_runs, time)) #creates an empty array (with 0) to store the data from simulations

    for i in range(n_runs):
        file="file"+str(i)+".txt" #iterates over the names of generated files
        with open(file, "r") as f: #opens the generated files
            data=f.readlines() #saves the data line by line into variable
            simulation_results[i,:]=data #replaces rows in the array of 0 with simulation data

    for j in simulation_results.T: #iterates over columns in result array
        average.append(statistics.mean(j)) #calculate average for column and appends it to list
        uncertainties.append(statistics.stdev(j)/math.sqrt(len(j))) #calculate uncertainties for column average and appends it to list

    #Plots the graph
    plt.title("The Concentration Decrease Over Time")
    plt.xlabel("Time [s]")
    plt.ylabel("Concentration [mol/L]")
    plt.errorbar(t, average, yerr=uncertainties, capsize=3, capthick=1, color="#7C90DB", label="mean ± SEM (n=100)")
    plt.grid(visible=True)
    plt.legend()
    plt.show()

main()
