# Schofield, Kierloyd Vince V.
# BSIS 3B
# Exercise No. 3\

# prob 1 - FIND THE SUM OF 2 INPUT NUMBERS AND DISPLAY THE RESULT.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum is: {sum}")

# prob 2 - PERFORM AN MDAS OPERATION.
mnum1 = int(input("Enter first number: "))
mnum2 = int(input("Enter second number: "))
product = mnum1 * mnum2
quotient = mnum1 / mnum2
msum = mnum1 + mnum2
difference = mnum1 - mnum2
print(f"The product is: {product}")
print(f"The quotient is: {quotient}")
print(f"The sum is: {msum}")
print(f"The difference is: {difference}")

# prob 3 - FIND THE AVERAGE OF 3 INPUT QUIZZES AND DISPLAY THE RESULT.
quiz1 = int(input("Enter first quiz: "))
quiz2 = int(input("Enter second quiz: "))
quiz3 = int(input("Enter third quiz: "))
average = (quiz1 + quiz2 + quiz3)/3
print(f"The average is: {average}")