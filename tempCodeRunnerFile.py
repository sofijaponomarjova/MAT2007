def task2():    
    print("This programm checks whether a string is a palindrome!")
    print("Enter a string!")
    string=input("")
    for char in string:
        if char.isdigit():
            print("Your string contains number, it can't be a polindrome")
            exit()
    string=string.lower()
    string=string.replace(" ", "")
    reversed_str=string[::-1]
    if string==reversed_str:
        print("It's a palindrome!")
    else:
        print("It is clearly not a palindrome!")
