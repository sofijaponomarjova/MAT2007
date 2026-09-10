def task1():
    print("Enter a list of integers (separate them by space please)!") #explains user the expected input
    initial_list=input("") #saves input in to a variable
    try: #tries to execute the code
        integers=initial_list.split() #splits (after every space) the entered string into a list
        integer_list=[] #creates an empty list to store the integers
        for number in integers: #iterates over the list
            integer_list.append(int(number)) #changes the numbers, changes their type to int and appends to list
        average=sum(integer_list)/len(integer_list) #calculates the average of list by summing up all integers and dividing by their number
        print(f"The average of your list {integer_list} is {average}!") #prints the result for user
    except ValueError: #if any of the list items can't be transformed into int, informs user that input vas invalid
        print("You gave invalid input!")
    except ZeroDivisionError: #if when calculating average the number of integers is 0, informs user that they didn't enter any number
        print("You didn't enter any number!")
    except: #if any other error occurs informs user
        print("Something went wrong:(")
        
def task2():    
    print("This programm checks whether a string is a palindrome!") #explains the goal of the program
    print("Enter a string!") #explains expected input
    string=input("") #saves the input into a variable
    clean_str=[] #creates an empty list to store cleaned string in future
    letter_count=0 #creates a variable to keep track of letters in string
    string=string.lower() #transforms all letters into lowercase
    for char in string: #iterates over characters in string
        if char.isdigit(): #checks whether character is a number
            print("Your string contains number, it can't be a palindrome") #explains the user the mistake
            return #stops the function
        if char.isalpha(): #checks whether the character is a letter
            letter_count+=1 #increases letter count
            clean_str.append(char) #adds the letter to the cleaned string list (allows to exclude spaces, commas, dots etc.)
    clean_str="".join(clean_str) #joins the list of letters back into a string
    if letter_count<2: #checks whether there's enough characters in string
        print("There is not enough characters in your string for it to be a palindrome!") #informs user about mistake
        return #stops the function
    reversed_str=clean_str[::-1] #turns around the string by saving every character starting from last to another variable
    if clean_str==reversed_str: #checks whether reversed and og string are the same
        print("It's a palindrome!") #informs that it's a palindrome
    else:
        print("It is clearly not a palindrome!") #informs that it's not a palindrome


#calls the functions of tasks
task1()
task2()
