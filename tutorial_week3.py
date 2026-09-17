# -- Task 1 --

def factorial(n): #defines the function
    if n==0: #deals with multiplication by 0 by returning 1 if given number was 0
        return 1
    else: #calculates factorial for other numbers
        return n * factorial(n-1) #recursive function (calls itself) to calculate factorial
    #BUG: - factorial(n) was called where n never changed its value,
    #I changed it to factorial(n-1) and now program works


def task1():
    try:
        number=int(input("Enter an integer:\n")) #asks user for a number
        print(f"{number}! = {factorial(number)}") #calls the function to calculate factorial & prints the result
    except:
        print("Something went wrong :(") #if an error warns user about it


# -- Task 2 --
import random

def add(a, b):
    return a+b #BUG: there was a minus instead of +, numbers were substracted

#Random tests
def task2():   
    for _ in range(5): #runs program 5 times
        a, b=random.randint(1, 100), random.randint(1, 100) #calculates random values for a and b (random testing)
        print(f"add({a}, {b})= {add(a,b)}. Expected: {a+b}") #runs the program with random values and compares the output to the expected result


# -- Task 3 --

def is_prime(n):
    if n<=1: #by definition negative numbers, 0 and 1 can't be prime numbers
        return False #returns false if not prime numbers
    for i in range (2, int(n**0.5)+1): #citerates over all numbers from 2 to square root of number + 1 (after that the multipliers are the same, just swithced around e.g 2*5=10 5*2=10)
        if n%i==0: #checks if the reaminder of division is 0 i.e. if the given number is divisible by numbers iterated over in loop
                    #BUG: previously it checked if when given number divided by 1 the reminder is 1 (n%i==1), this expression is always false because all itnergers are divisble by 1 with no reminder
            return False #returns false i.e. the given number is not prime
    return True #returns true if number is not divisble by any number in given range (i.e. is divisble only by 1 and itself and is therefore a prime)

#Black box tests
def task3():
    a,b=random.randint(-100,0), random.randint(0, 100) #generates the lower and upper limit for range
    for i in range (a,b): #iterates over numbers
        print(f"{i} is prime: {is_prime(i)}") #prints the output of function to test it

# -- Task 4 --

def gcd(a,b):
    while b: #runs while b is not 0
        print(f"Euclidean Algorithm {a}={b} * {(a-(a%b))/b }+ {a%b}") #this line is for visualisation, it prints the equation in form of Euclidean Algorithm for finding the gcd
        a, b = b, a%b #BUG: the smaller number needs to be replaced with remainder of the devision, not the result of division
    return a #when the remaining of division is 0 function returns the gcd

#Glass box tests
def task4():
    try: #runs the program with different numbers and assesses whether the given gcd is true
        assert gcd(180, 48)==12
        print("GCD of 180 and 48 is 12\n")
        assert gcd (100, 10)==10
        print("GCD of 180 and 10 is 10\n")
        assert gcd(7,3)==1
        print("GCD of 7 and 3 is 1\n")
    except AssertionError: #if asertion error rises informs user
        print("There was assertion error, programm isn't working correctly!")
    except: #if another error rises informs user
        print("Something went wrong!")

print(" -- Task 1 -- \n")
task1()
print(" -- Task 2 -- \n")
task2()
print(" -- Task 3 -- \n")
task3()
print(" -- Task 4 -- \n")
task4()






