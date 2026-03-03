# Schofield, Kierloyd Vince V.
# BSIS 3B
# Activity 2 - Record Keeping App
# Time started: 1:38PM
# Time finished: 1:59PM (2:05PM with validations)

# ask the user to choose between add, delete or end the process - if elif elif else
# if add, input key and value, and store using dict and display result - dict key value
# if delete, the app will ask for the key, remove from dct and display result - pop, print
# if end, display Thank you - print

data = {}  # start with empty list

while True:
    print("\nRecord Keeping App\n")  # menu
    print("1. Add Data")
    print("2. Delete Data")
    print("3. End")
    action = input('\nEnter your choice: ')
    if action.isdigit():  # validation for choice
        if action == '1':
            key = input('Enter your category: ')
            value = input('Enter your value: ')
            data[key] = value  # store
            for category, detail in data.items():  # printing
                print(f"\nCategory: {category} | Value: {detail}")
        elif action == '2':
            if not data:  # check if dict is empty
                print("\nThe data is empty! Nothing to delete!")
            else:
                key = input('Enter your category: ')
                if not key in data:  # check if the key exists
                    print("Category does not exist.")
                else:
                    data.pop(key)
                    for category, detail in data.items():
                        print(f"\nCategory: {category} | Value: {detail}")
        elif action == '3':
            print("\nThank you!")
            break  # ends the while true loop
        else:
            print("\nInvalid Input! Numbers from 1-3 only")
    else:
        print("\nInvalid Input! Numbers only")