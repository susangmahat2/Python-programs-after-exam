try:
    num=int(input("Enter a number:"))
    print("The number you entered is:",num)
except ValueError:
    print("Invalid input. Please enter a valid integer.")