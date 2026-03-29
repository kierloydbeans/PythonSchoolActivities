# Schofield, Kierloyd Vince V
# BSIS 3B
# 3/17/26
# Practical 2

# ask for choice if addition, subtraction, multiplication, or division
# ask for two numbers
# display the result
# try again or nah
# use functions and exceptions

def mainMenu():
    while True:
        print("=====================")
        print("Welcome to Calculator")
        print("=====================")

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        action = input("Enter your choice: ")
        if action in ["1", "2", "3", "4"]:
            performCaluclation(action)
        elif action == "5":
            print("Thank you!")
            break
        else:
            print("Invalid. Numbers 1-5 only\n")

def getNumbers():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Error. Invalid. Must be a valid number.\n")

def performCaluclation(choice):
    num1, num2 = getNumbers()

    try:
        if choice == "1":
            print(f"The result is {num1 + num2}")
        elif choice == "2":
            print(f"The result is {num1 - num2}")
        elif choice == "3":
            print(f"The result is {num1 * num2}")
        elif choice == "4":
            print(f"The result is {num1 / num2}")
    except ZeroDivisionError:
        print("Error. Cannot divide by zero.")
    except Exception as e:
        print("An unexpected erro occured.")
    again()

def again():
    while True:
        repeat = input("Do you want to repeat? (Y/N): ")
        if repeat.lower() == "y":
            mainMenu()
        elif repeat.lower() == "n":
            print("Thank you!")
            exit()
        else:
            print("Invalid. Y or N only.")
mainMenu()