# Schofield, Kierloyd Vince V.
# BSIS 3B
# Practical 1
# 3/16/26

import random
#              0        1        2             3         4
firstName = ["Aleks", "Zeno", "Alejandro", "Allegra", "Michelle"]
middleName = ["Orpheus", "Hermes", "Polydeuces", "Penthesilea", "Io"]
lastName = ["Le", "Robinson", "Saab", "Clark", "Ruff"]

generatedNames = []  # container of generated names

while True:
    again = input("Do you want to generate a new name? (Y/N): ")
    if again.lower() == "y":
        # picks a random name from each list
        firstNameIndex = random.randint(0, 4)
        middleNameIndex = random.randint(0, 4)
        lastNameIndex = random.randint(0, 4)

        name = f"{firstName[firstNameIndex]} {middleName[middleNameIndex]} {lastName[lastNameIndex]}"  # generates the name
        print(name)
        generatedNames.append(name)  # stores the name

    elif again.lower() == "n":
        print("Thank you!\nList of names generated:\n")
        for names in generatedNames:  # looping through all names in the container
            print(names)
        break

    else:
        print("Invalid. Use either Y or N only")  # input validation
