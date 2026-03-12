# Schofield, Kierloyd Vince V.
# BSIS 3B
# Midterm Exam
# Feb. 23, 2026

# Write a program that accepts two integers. The program should determine if the sum of the two integers
# is even or odd.

# Enter first number:
# Enter second number:
# The sum is [odd or even]

# Continue? Y/y or N/n

while True:
    num1Input = input("Enter first number: ")
    if not num1Input.isdigit():
        print("Invalid. Must be a number.")
        continue

    num2Input = input("Enter second number: ")
    if not num2Input.isdigit():
        print("Invalid. Must be a number.")
        continue

    # convert to integer

    num1 = int(num1Input)
    num2 = int(num2Input)

    # compute sum
    sum = num1 + num2

    if sum % 2 == 0:
        print(f"{num1} + {num2} = {sum}. The sum of two numbers is EVEN.")
    else:
        print(f"{num1} + {num2} = {sum}. The sum of two numbers is ODD")

    # decision if continue or not
    while True:
        con = input("Do you want to continue? Y/N: ")
        if con == "Y" or con == "y":
            break  # go back to the first while true
        elif con == "N" or con == "n":
            print("Thank you!")
            exit()  # exit the loop; terminating the session
        else:
            print("Invalid")  # loops back to the second while True
