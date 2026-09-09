def converter(): #first task

    answer=input("What unit you want convert into?\n") #asks what convertion users wants to do
    
    if answer.lower()== "fahrenheit":
        temperature=float(input("Enter the temperature in Celsius:\n")) #receives the temperature from user
        fahrenheit=temperature*9/5+32 #converts to fahrenheit
        print(f"This is {fahrenheit} degrees in Franheit!") #prints the result

    elif answer.lower()== "celsius":
        temperature=float(input("Enter the temperature in Fahrenheit:\n")) #receives the temperature from user
        celsius=(temperature-32)*5/9 #converts to celsius
        print(f"This is {celsius} degrees in Celsius!") #prints the result

    else:
          print("Wrong input") #warns user that the given input is invalid (not celisus or fahrenheit)

def calculator(): #task 2
    a=float(input("Enter the first number:\n")) #receives the first number as float (so that user can input a decimal)
    b=float(input("Enter the second number:\n")) #receives the second number
    print("Choose what you want to do:\n", "- sum\n", "- substract\n", "- multiply\n", "- divide\n") #gives user available expressions
    answer=input("") #receives the answer

    if answer.lower()== "sum":
        print(f"{a} + {b} = {a+b}") #sums numbers and prints the result

    elif answer.lower()== "substract":
            print(f"{a} - {b} = {a-b}") #substracts numbers and prints the result

    elif answer.lower()== "multiply":
            print(f"{a} * {b} = {a*b}") #multiplies numbers and prints the result

    elif answer.lower()== "divide":
            if b==0: #checks if the divisor is 0
                  print("Can't divide with 0") #warns user that division by 0 is impossible
            else:
                print(f"{a} / {b} = {a/b}") # divides two numbers and prints the result
    else:
          print("Wrong input") #warns user that the input is incorrect (not one of the provided expressions)

print("Here is task 1 'Temperature Conversion'")
converter() #calls the task 1

print("Here is task 2 'Simple Calculator'")
calculator() #calls the task 2