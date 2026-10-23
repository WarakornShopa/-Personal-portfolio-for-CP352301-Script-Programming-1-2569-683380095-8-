# lab4_1.py - Student Management System (List Operations)

print("\n","--- Lab 4.1: Student Management System ---","\n")

student_names = []
con = 1

while(con == 1):    
    print("1.) |--- Add Student ------|")
    print("2.) |--- Remove Student ---|")
    print("3.) |--- Search Student ---|")
    print("4.) |--- Sort Student -----|")
    print("5.) |--- Exit -------------|","\n")
    choice = int(input("Please choose the command 1-5 : "))

    if (choice == 1):
        print("\n[1] Add Students")
        AddSTD = input(f"Enter student name : ")
        student_names.append(AddSTD)

    elif (choice == 2):
        print("\n[2] Remove a Student")
        remove_name = input("Enter a name to remove: ")

        if remove_name in student_names:
            student_names.remove(remove_name)
            print(f"'{remove_name}' has been removed")
        else:
            print(f"'{remove_name}' not found, nothing removed")

        print(f"Updated list: {student_names}")

    elif (choice == 3):
        print("\n[3] Find a Student")
        search_name = input("Enter a name to search for: ")

        if search_name in student_names:
            position = student_names.index(search_name)
            print(f"Found '{search_name}' at index {position}")
        else:
            print(f"'{search_name}' not found in the list")
            print("\n")
            print(f"Current list: {student_names}")
            print("\n")

    elif (choice == 4):
        print("\n[4] Sort Students")
        student_names.sort()
        print(f"Sorted list: {student_names}")

    elif (choice == 5):
        print("\n","Thank you!!")
        break

    else:
        print("Please type only 1-5")

    print("\n")
    print(f"Current list: {student_names}") 
    print("\n")