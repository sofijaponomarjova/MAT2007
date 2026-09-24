#importing necessary libraries and functions

import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

def task1():
    try:
        mean=5 #defines the mean
        t_interval=1000 #defines the time interval
        photons=np.random.poisson(mean, t_interval) #generates the pseudo dataset by randomly drawing from poisson distribution
        with open("detected_photons.txt", "w") as file: #opens (creates if not present the file)
            for i in photons: #iterates over created array
                file.write(f"{i}\n") #writes the generated photon count in a file in one column
            return True #indicates that the program finished successfully
    except:
        print("Something went wrong!") #warns user that there was a problem
        return None #exits the function

def task2():
    try:
        with open("detected_photons.txt", "r") as file: #opens the file from task 1
            data=file.read() #saves the data into a string
        photons=np.array(data.split(), dtype=int) #creates an array from the string (splits the string when a space is detected)
        subsamples=np.split(photons, 10) #splits the og array into 10 subsamples
        with open ("photons_subsamples.txt", "w") as file2: #opens/creates a new file for subsamples
            for i in subsamples: #iterates over the subsample array
                file2.write(f"{i}\n") #saves each subsample in a new line of the new file
        return subsamples #returns the array of subsamples to reuse it in other tasks
    except:
        print("Something went wrong!") #if there's an error warns the user
        return None #exits the function
    
def task3(subsamples):
    subsamples_avg=[] #creates an empty list for averages
    for i in subsamples: #iterates ove the subsample array
        subsamples_avg.append(np.average(i)) #calculates average for every subsample and saves it in list
    final_mean=np.average(subsamples_avg) #calculates the final mean
    uncertainty=np.std(subsamples_avg) #calculates the uncertainty/standard deviation
    print(f"There is on average {final_mean} ± {uncertainty} photons detected!\n") #prints the result for user

def task4(subsamples):
    skewness=[] #empty list for skewness
    kurt=[] #empty list for kurtosis
    for i in subsamples: #iterates over the array of subsamples
        skewness.append(skew(i)) #calculates skewness for each subsample
        kurt.append(kurtosis(i)) #calculate kurtosis for each subsample
    final_skew=np.average(skewness) #calculates the final skewness
    unc_skew=np.std(skewness) #caculates std/uncertainty for skewness
    final_kurt=np.average(kurt) #calculates the final kurtosis
    unc_kurt=np.std(kurt) #calculates the std/uncertainty for kurtosis
    print(f"The skewness is {final_skew} ± {unc_skew}\n") #prints the result
    print(f"The kurtosis is {final_kurt} ± {unc_kurt}\n") #prints the result
    

print("-- Task 1 --\n") #beautiful design
result=task1() #calls task1 and saves the result
if result is not None: #checks if function run correctly
    print("Task completed!\nPseudo data is now saved on your computer in file 'detected_photons.txt'!\n") #informs user on where to find the output

print("-- Task 2 --\n")
subsamples=task2() #calls the task and saves the result
if subsamples is not None: #checks if task run correctly
    print("Task completed!\nSubsamples are now saved on your computer in file 'photons_subsamples.txt'!\n") #informs user on where to find the output

print("-- Task 3 --\n")
if subsamples is not None:
    task3(subsamples) #runs task 3 and gives the array of subsamples as argument

print("-- Task 4 --\n")
if subsamples is not None:
    task4(subsamples) #runs task 4 and gives the array of subsamples as argument
