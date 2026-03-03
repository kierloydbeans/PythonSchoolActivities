# Schofield, Kierloyd Vince V.
# BSIS 3B
# Exercise No. 4

name = input("Enter your name: ")
print("Enter your grades: ")
math = int(input("Math: "))
sci = int(input("Science: "))
eng = int(input("English: "))
average = (math + sci + eng)/3
# passed
if average >= 75 and math >= 75 and sci >= 75 and eng >= 75:
    print(f"Your average is {round(average, 2)}. Congratulations! You passed the semester!")
# failed
elif average <= 75:
    print(f"Your average is {round(average, 2)}. You failed the semester.")
# retake
elif average >= 75 or math <= 75 or sci <= 75 or eng <= 75:
    print(f"Your average is {round(average, 2)}. Congratulations! You passed the semester, but you need to retake the following subjects:")
    # conditions
    if math <= 75:
        print("Math")
    if sci <= 75:
        print("Science")
    if eng <= 75:
        print("English")