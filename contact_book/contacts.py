contacts = {}

def add_contact(name, number):
    contacts[name] = number

def show_contacts():
    if contacts:
        for name, number in contacts.items():
            print(f"name: {name}, number: {number}")
    else:
        print("No contacts found.!!!!")

def remove_contacts(name):
    contacts.pop(name, None)

while True:
    print("1. Add Contact\n2. Show Contact\n 3. Remove Contact\n 4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
        print("Contact added successfully!")

    elif choice == '2':
        show_contacts()

    elif choice == '3':
        name = input("Enter name of contact to remove: ")
        remove_contacts(name)
        print("Contact removed successfully!")

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please try again!")
