

def task2():
    a=10 #defines the integers
    b=2

    
    sum=a+b #calculates the result
    print(f"{a} + {b} = {sum}") #prints the result
    difference=a-b
    print(f"{a} - {b} = {difference}")
    multiplication=a*b
    print(f"{a} * {b} = {multiplication}")
    division=a/b
    print(f"{a} / {b} = {division}")

    

def task3():
    numbers=[1, 5, 37, 29, 41] #stores integers as a list
    numbers.append(24) #adds number to list
    print(numbers) #prints the list with added value
    numbers.pop(-1) #removes the last item from list
    print(numbers) #prints the list with last item removed
def task4(): 
    number=6 #defines the number
    if number%2==0: #checks if remainder of divison by 2 is 0 (if the number is even)
        print(f"{number} is even number") #prints that the number is even
    else:
        print(f"{number} is odd number") #if the remainder of division by 2 is not 0, prints tha number is odd



print("Task 1") #prints the label of task
print("Sofija")
print("Task 2")
task2() #calls the function of corresponding task
print("Task 3")
task3()
print("Task 4")
task4()