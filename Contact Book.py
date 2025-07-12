contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    })
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'])
            print("-" * 20)

def search_contact():
    keyword = input("Enter name or phone to search: ")
    found = False
    for contact in contacts:
        if contact['name'] == keyword or contact['phone'] == keyword:
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'])
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input("Enter new phone: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice.")
