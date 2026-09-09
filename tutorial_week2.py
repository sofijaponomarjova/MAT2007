def task1(): #defines a function
    print("Enter a string") #explain user what iput is expected
    str=input("") #saves the input in variable
    reverse_str=str[::-1] #creates new variable that stores every character of str
    #step -1 means that the copyirewritingsng starts at the end and continues forward
    print(reverse_str) #prints the reverse string

def task2():
    sum=0 #introduces a variable for sum
    n=0 #introduces a variable that represents numbers up to 50
    while n<50: #loop stops when n reaches 50 (50 is even so can be ignored)
        if n%2!=0: #checks if the numeber is odd
            sum=sum+n #adds number to the sum if its odd
        n+=1 #moves on to next number
    print(f"The sum of all odd numbers up to 50 is {sum}") #prints the resulting sum

def task3():
    print("Enter a letter:") #asks user for input (1 letter)
    letter=input("") #saves the input
    vowels=["a", "e", "i", "o", "u", "y"] #array of vowels to compare to
    consonents=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"] #array of consonents to compare to
    if letter.lower() in vowels: #checks if the entered letter is in array of consonents (lower accounts for capitalization)
        print(f"{letter} is a vowel!") #if so, prints the result
    elif letter.lower() in consonents: #checks if the entered letter is in array of vowels (lower accounts for capitalization)
                print(f"{letter} is a consonent!") #if so, prints the result
    else: 
         print("Invalid input") #if entered letter is not vowel nor consonent, informs user that given input is invalid

def odd_or_even(n):
    if n%2==0:
        return "even number"
    else:
        return "odd number"
        

def task4():
    print("Enter an integer")
    number=(input(""))
    if number.isdigit()==True:
        number=int(number)
        answer=odd_or_even(number)
        print(f"{number} is {answer}!")
    else:
        print ("Input is invalid.")
    
def task5():
    print("Multiplication table from 1 to 5")
    for multiplicand in range(1, 6):
        row=[]
        for multiplier in range(1,11):
              result=(multiplicand*multiplier)
              row.append(result)
        print(row)
     
''' print("-- Task1 --")
task1()
print("-- Task2 --")
task2()
print("-- Task3 --")
task3()
print("-- Task4 --")
task4()'''
print("-- Task5 --")
task5()