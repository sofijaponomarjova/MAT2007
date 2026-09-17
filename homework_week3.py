def sum_list(numbers):
    total=0 #introduces variable that stores the sum
    for number in numbers: #iterates over the list
        total += number #adds every number in list to the sum
        # the bag was in synta 1) characters were reversed, instead of adding the number to variable (+=), number was saved as the new value of the variable with the according sign (=+/=-)
        # 2) there was a minus sign instead of plus
    return total

def task1():
    #Test the function
    list=input("Enter a list of numbers separated by space:\n") #asks user for input
    try:
        values=list.split() #splits the given string into separate values
        numbers=[] #introduces an empty list variable
        for number in values: #iterates over the list of number user gave
            numbers.append(float(number)) #saves the numbers on by one in a list as float
        if sum(numbers)==sum_list(numbers):
            print(f"The sum of your list is: {sum_list(numbers)}") #prints the sum
        else:
            print("The program is broken!")
    except:
        print("Something went wrong!!") #If an error occurs warns user

def bubble_sort(arr):

    #the bug here was wrong range in second function & reversed sign in if statement
    n=len(arr) #n is the length of given array
    for i in range(n): #repeats the algorithm as many times as there are numbers in list (to put every number in the right place)
        for j in range(0, n-i-1): #idk how to explain, but it repeats the algorithm as many times as there are numbers left not in the correct spot
            #n-1 ensures that when the penultimate item in list is reached, index j+1 doesn't exceed the range
            # n-1-1 ensures that when number is in the right place it is ignored and not compared anymore (because it's definetly bigger than remaining numbers)
            if arr[j+1]<arr[j]: #compares number and next number in the list
                arr[j], arr[j+1]=arr[j+1], arr[j] #if number on the right is smaller, numbers are swapped
    return arr #after modification array is returned

# Test the function
def task2():
    list=input("Enter a list of random numbers separated by space:\n") #asks user for input
    try:
        values=list.split() #splits the given string into separate values
        numbers=[] #introduces an empty list variable
        for number in values: #iterates over the list of number user gave
            numbers.append(float(number)) #saves the numbers on by one in a list as float
        sorted_list=bubble_sort(numbers) #runs the function to sort the numbers
        for i, value in enumerate(sorted_list[:-1]): #iterates over the sorted list
            if value>sorted_list[i+1]: #checks if numbers are sorted correctly
                print("The program is broken!") #informs user in program is not working as intended 
                return #exits the function
        print(f"The numbers in ascending order are: {sorted_list}") #if everything correct, prints the sorted list
    except:
        print("Something went wrong!!") #If an error occurs warns user

print("-- Task 1 --\n")
task1()
print("-- Task 2 --\n")
task2()