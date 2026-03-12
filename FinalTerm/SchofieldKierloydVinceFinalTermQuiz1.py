# add record dict["key"] = value
# delete = dict.pop
# update =
# search = dict.values(input)
# display = print
# exit

record = {}  # initialize empty dict

while True:

    print("===========RECORD MANAGEMENT SYSTEM================")
    print("1 - Add record")
    print("2 - Delete record")
    print("3 - Update record")
    print("4 - Search record")
    print("5 - Display record")
    print("6 - Exit")
    action = input("Enter your choice: ")

    if action == "1":
        lastNameValue = input("Enter your last name: ")
        firstNameValue = input("Enter your first name: ")
        ageValue = input("Enter you age: ")
        courseValue = input("Enter your course: ")

        lastNameInfo = {
            "FirstName": firstNameValue,
            "Age": ageValue,
            "Course": courseValue
        }
        record[lastNameValue] = lastNameInfo
        print("Successfully stored!")
    elif action == "2":
        toDelete = input("Enter what to delete: ")
        record.pop(toDelete)
        print("Successfully deleted!")
    elif action == "3":
        search = input("Enter the last name to update: ")
        if search in record:
            newFirstName = input("Enter new first name: ")
            newAge = input("Enter new age: ")
            newCourse = input("Enter new course: ")
            record[search]["FirstName"] = newFirstName
            record[search]["Age"] = newAge
            record[search]["Course"] = newCourse
            print("Record updated!")
        else:
            print("Record not found.")
    elif action == "4":
        search = input("Enter the last name to search: ")
        if search in record:
            print(f"Details for {search}: {record[search]}")
        else:
            print("Record not found.")
    elif action == "5":
        print("Last Name | First Name | Age | Course")
        for name, info in record.items():
            print(f"{name} {info} ")
    elif action == "6":
        print("THANK YOU FOR USING THE SYSTEM")
        break