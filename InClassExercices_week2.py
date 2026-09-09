def task1():
    int1 = 10
    int2 = 12
    float1 = 8.5457
    sum= int1 + int2 + float1
    difference = int1 - int2 - float1
    product = int1 * int2 * float1
    division = int1 / int2 / float1
    print("Variables: ")
    print(type(int1), int1)
    print(type(int2), int2)
    print(type(float1), float1)
    print(f"Sum: {sum}")
    print(f"Difference: {difference}")
    print(f"Product: {product}")
    print(f"Division: {division}")

def task2():
    string1="Green"
    string2="apple"

    print(f"Concatenation: {string1 + ' ' + string2}")
    print(f"Comparison: {string1==string2}")
    print(f"The length of first string: {len(string1)}")
    print(f"The length of second string: {len(string2)}")

def task3():
    int1=int(input("Enter an integer: "))
    if int1>0:
        print(f"{int1} is positive")
    elif int1==0:
        print(f"{int1} is zero")
    elif int1<0:
        print(f"{int1} is negative")

def task4():
    for i in range (1, 21):
        if i%2==0:
            print(i)

def task5(a,b):
    return a+b


print(" -- Task 1 --")
task1()
print(" -- Task 2 --")
task2()
print(" -- Task 3 --")
task3()
print(" -- Task 4 --")
task4()
print(" -- Task 5 --")
print(f"The sum is {task5(4,6)}")