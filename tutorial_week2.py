def task1(): #defines a function
    print("Enter a string") #explains user what iput is expected
    str=input("") #saves the input in variable
    reverse_str=str[::-1] #creates new variable that stores every character of str starting from the last one
    #'step -1' means that the rewriting starts from the end and continues forward
    print(reverse_str) #prints the reverse string

def task2():
    sum=0 #introduces a variable for sum
    n=0 #introduces a variable that represents numbers up to 50
    while n<50: #loop stops when n reaches 50 (50 is even so can be ignored)
        if n%2!=0: #checks if the number is odd
            sum=sum+n #adds number to the sum if its odd
        n+=1 #moves on to next number
    print(f"The sum of all odd numbers from 1 to 50 is {sum}") #prints the resulting sum

def task3():
    print("Enter a letter:") #explains user what input is expected (1 letter)
    letter=input("") #saves the input
    vowels=["a", "e", "i", "o", "u"] #list of vowels to compare to
    consonants=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"] #list of consonants to compare to
    if letter=="y": #checks if the entered letter is y
         print("Y can be both - vowel and consonant!") #informs that y can be both
    elif letter.lower() in vowels: #checks if the entered letter is in list of vowels (lower accounts for capitalization)
        print(f"{letter} is a vowel!") #if so, prints the result
    elif letter.lower() in consonants: #checks if the entered letter is in list of consonants (lower accounts for capitalization)
                print(f"{letter} is a consonent!") #if so, prints the result
    else: 
         print("Invalid input") #if entered character is not vowel nor consonent, informs user that given input is invalid

def odd_or_even(n): #defines function to check if number is odd or even
    if n%2==0: #checks if number is even (if it is divisible by 2)
        return "even number" #returns a string that number is even
    else:
        return "odd number" #if number is not divisible by 2 returns a string that number is odd
        

def task4():
    print("Enter an integer") #explains user what input is expected (an integer)
    try:
        number=int(input("")) #saves input to a variable type int
        answer=odd_or_even(number) #calls the function to check if number is odd or even
        print(f"{number} is {answer}!") #informs user if given number is even or odd
    except ValueError: #activates the code if provided input can't be saved as type int (ValueError)
        print ("You had to enter an integer!") #informs user that the input had to be an integer
    except: #accounts for other errors
         print("Input is invalid.") #informs user that input is invalid
    
def task5():
    print("Multiplication table from 1 to 5") #prints the title of the table
    for multiplicand in range(1, 6): #starts a loop to iterate over numbers from 1 to 5 (multiplicands)
        row=[] #creates a list to save values of each row
        for multiplier in range(1,11): #starts a loop to iterate over numbers 1 to 10 (multiplier)
              result=(multiplicand*multiplier) #saves two multiplied numbers into a variable
              row.append(result) #adds result to the list
        print(row) #prints the corresponding row
        #e.g. first row contains all products of 1, second row contains all products of 2 etc.
     
print("-- Task1 --") #prints the task title
task1() #calls function of first task
print() #prints an empty row so the output is more visually appealing
print("-- Task2 --")
task2()
print()
print("-- Task3 --")
task3()
print()
print("-- Task4 --")
task4()
print()
print("-- Task5 --")
task5()