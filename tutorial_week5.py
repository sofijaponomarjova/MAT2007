#!!!!!!! At the bottom of the file REMOVE # FROM THE TASK YOU WANT TO RUN !!!!!!!!!!!

#imports necessary libraries

import numpy as np
import matplotlib.pyplot as plt 
import math

#first task

def task1():
    sample_population=10000 #defines sample size for all isotopes
    lifetime=[1,5,10] #list of diff lifetimes
    colors=["#23395B", "#406E8E", "#CBF7ED"] #list of colors for each isotope
    labels=["Isotope 1 (Lifetime: 1 year)", "Isotope 2 (Lifetime: 5 years)", "Isotope 3 (Lifetime: 10 years)"] #labels for legend
    bin_size=np.arange(0, 41) #creates a list of nombers from 0 to 40, will be used as bin edges = 0-1, 1-2, 2-3, 3-4, 4-5 etc.
    plt.title("Decay Rate of Radioactive Isotopes With Different Lifetimes") 
    plt.ylabel("Decays per Year")
    plt.xlabel("Time (years)")
    for index, value in enumerate(lifetime): #iterates over 3 diff lifetimes and saves the index and value (lifetime) in separate variables 
        t=np.random.exponential(value, sample_population) #generate the data for specific isotope
        plt.hist(t, color=colors[index], bins=bin_size, alpha=0.6, label=labels[index]) #plots the histogram, with unique colors and label, transparency (so every isotope is visible) and bin sizes are the same for each isotope
    plt.legend()
    plt.show()

def coulombs_law(q1, q2, vac_perm, r): #function to calculate coulombs law
    F=(abs(1/(4*math.pi*vac_perm)*(q1*q2/r**2))) 
        
    return F


def task2():

    plt.title("Coulomb Force on Electron vs Distance\n (Positron, Lead Nucleus, Oxygen Nucleus)")
    plt.xlabel("Distance (m)")
    plt.ylabel("Electron Force (N)")

    #the values for equation
    electron=1.602/10**19
    vacuum_perm=8.854/10**12
    oxygen=8*electron
    lead_nucleus=82*electron
    positron=electron
    distance=np.logspace(-9, 0, 1000)

    #calculates the coulombs law for each particle
    Fp=coulombs_law(electron, positron, vacuum_perm, distance)
    Fln=coulombs_law(electron, lead_nucleus, vacuum_perm, distance)
    Fo=coulombs_law(electron, oxygen, vacuum_perm, distance)

    #plotting each particle on the same canvas
    plt.loglog(distance, Fp, label="Positron")
    plt.loglog(distance, Fln, label=("Lead Nucleus"))
    plt.loglog(distance, Fo, label=("Oxygen Nucleus"))

    #adding grid & legend
    plt.grid(which="major", alpha=0.5)
    plt.legend()
    
    #showing the graph
    plt.show()


def task3():
    
    data1=np.random.normal(10, 2, 1000) #generating data for first sample
    data2=np.random.normal(20, 7, 1000) #generating data for second sample
    edges=np.arange(-10, 51, 1) #generating the edges for bins (60 bins)
    labels=["μ=10, σ=2", "μ=20, σ=7"] #list of labels for legend
    
    plt.title("Two Histograms with Different Gaussian Distributions")
    plt.xlabel("Values")
    plt.ylabel("Count of Values")
    
    #plotting both histograms in different colours & transparency so they are visible
    plt.hist(data1, bins=edges, color="#8C2F39", alpha=0.6, label=labels[0])
    plt.hist(data2, bins=edges, color="#FCB9B2", alpha=0.6, label=labels[1])
    plt.legend()
    plt.show()


#!!!!!!! REMOVE # FROM THE TASK YOU WANT TO RUN !!!!!!!!!!!

task1()
task2()
task3()
