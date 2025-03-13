# Contact manager application
contacts = []
def add_contact(name, phone, email):
    for contact in contacts:
        if contact[0] == name:  
            print("Contact with this name already exists!")
            return
    contacts.append((name, phone, email))
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
def search_contact(name):
    for contact in contacts:
        if contact[0].lower() == name.lower():
            print(f"\nContact Found: Name: {contact[0]}, Phone: {contact[1]}, Email: {contact[2]}")
            return contact
    print("Contact not found.")
    return None
def update_contact(name, new_phone):
    global contacts
    updated = False
    contacts = [(c[0], new_phone, c[2]) if c[0].lower() == name.lower() else c for c in contacts]
    for contact in contacts:
        if contact[0].lower() == name.lower():
            updated = True
    if updated:
        print("Phone number updated successfully!")
    else:
        print("Contact not found.")
def delete_contact(name):
    global contacts
    new_contacts = [c for c in contacts if c[0].lower() != name.lower()]
    if len(new_contacts) == len(contacts):
        print("Contact not found.")
    else:
        contacts = new_contacts
        print("Contact deleted successfully!")
while True:
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact by Name")
    print("4. Update Contact Phone Number")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        add_contact(name, phone, email)

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        name = input("Enter Name to Search: ")
        search_contact(name)

    elif choice == "4":
        name = input("Enter Name to Update: ")
        new_phone = input("Enter New Phone Number: ")
        update_contact(name, new_phone)

    elif choice == "5":
        name = input("Enter Name to Delete: ")
        delete_contact(name)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
