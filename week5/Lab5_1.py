#-----Lab 5.1 - Simple Contact Book Manager (Dictionary Focus)-----

contacts = {}

while True:
    print("\n=== Contact Book Manager ===")
    print("1. Add/Update Contact")
    print("2. View Contact Details")
    print("3. List All Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ").lower()
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact '{name}' saved successfully!")

    elif choice == '2':
        name = input("Enter contact name to view: ").lower()

        info = contacts.get(name)

        if info:
            print(f"\nName: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print("Contact not found.")

    elif choice == '3':
        if not contacts:
            print("No contacts available.")
        else:
            print("\n--- All Contacts ---")
            for name, details in contacts.items():
                print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")

    elif choice == '4':
        name = input("Enter contact name to delete: ").lower()

        removed_contact = contacts.pop(name, None)

        if removed_contact:
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == '5':
        print("Exiting Contact Book Manager. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")