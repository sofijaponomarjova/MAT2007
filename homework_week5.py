#imports libraries

import numpy as np
import matplotlib.pyplot as plt 
import math


def main():
    path="/Users/admin/Desktop/MAT2007/solar_cycle_simulation.txt" #gets the path the pseudodata
    with open(path, "r") as file: #opens the file
        dataset=file.read() #saves data to a variable
    dataset=np.array(dataset.split(), dtype=float) #transforms data to an array
    subsamples=np.split(dataset, 10) #splits data in 10 subsamples
    sample_average=[] #creates list to store subsample averages
    sample_uncertainty=[] #creates list to store subsample average uncertanties 
    systematic_uncertainty=[]
    for sample in subsamples: #iterates over array of subsamples
        sample_average.append(np.average(sample)) #calculates average of each subsample and adds to list
        sample_uncertainty.append(np.std(sample)/math.sqrt(len(sample))) #calculates uncertainty of average for each subsample and adds to list
        systematic_uncertainty.append(np.average(sample)*0.1)
    k=np.arange(10) #makes a list of numbers from 0 to 9 (10 cycles there are)
    top_months=33+132*k #calculating the peak month of each cycle by formula I derived
    top_years=top_months/12 #transforms months into years
    total_time=np.arange(10*11*12) #creates list of indexes of months
    
    
    fig, axs = plt.subplots(1,3, figsize=(15, 7)) #creates 3 subplots
    fig.suptitle("Homework Exercises", fontweight='bold') #adds a title
    fig.subplots_adjust(left=0.05, right=0.98, wspace=0.3) #adjusts the alignement of subplots

    #Creation of first subplot
    axs[0].set_title("Solar Cycle as a Function of Time") 
    axs[0].set_ylabel("Number of Sunspots per Month")
    axs[0].set_xlabel("Time (Years)")
    axs[0].plot(total_time/12,dataset, color="#151E3F") #plots total time in years on x axis, plots number of sunspots per month on y axis
    axs[0].set_ylim(0, 150) #sets the y axis limit
    axs[0].grid() #plots the grid

    #Creation of second subplot
    axs[1].set_title("The Average Number of Sunspots per Month \n (With Statistical Uncertainty)") 
    axs[1].set_ylabel("Average Number of Sunspots per Month")
    axs[1].set_xlabel("Year of Cycle Top")
    axs[1].errorbar(top_years,sample_average, yerr=sample_uncertainty, fmt='o', color="#151E3F") #plots the peak years on x axis, plots the average amount of sunspots per cycle on y axis + adds statistical uncertainty
    axs[1].set_ylim(80, 120) #sets the y axis limit
    axs[1].grid() #plots the grid

    #Creation of third subplot
    axs[2].set_title("The Average Number of Sunspots per Month\n (With Both Uncertainties)") 
    axs[2].set_ylabel("Average Number of Sunspots per Month")
    axs[2].set_xlabel("Year of Cycle Top")
    axs[2].errorbar(top_years,sample_average, yerr=systematic_uncertainty, fmt='None', color="#5AD2F4", label="Systematic Uncertainty") #plots systematical uncertainty because (data point itself is set to none)
    axs[2].errorbar(top_years,sample_average, yerr=sample_uncertainty, fmt='o', color="#151E3F", label="Statistical Uncertainty") #plots the peak years on x axis, plots the average amount of sunspots per cycle on y axis + adds statistical uncertainty
    axs[2].set_ylim(80, 120) #sets the y axis limit
    axs[2].grid() #plots the grid
    axs[2].legend()
    
    #plots the final result
    plt.show()
 
main()