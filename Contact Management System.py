import re
import json

# Global variable to store contacts
contacts = {}

# Regular expressions for input validation
phone_regex = re.compile(r'^\d{10}$')  # Matches a 10-digit phone number
email_regex = re.compile(r'^[\w.-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$')  # Matches an email address

# Function to display the menu
def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file (BONUS)")
    print("8. Quit")

# Function to add a new contact
def add_contact():
    print("\nAdding a new contact:")
    name = input("Enter name: ")
    phone = input("Enter phone number (10 digits): ")
    while not re.match(phone_regex, phone):
        print("Invalid phone number format! Please enter 10 digits.")
        phone = input("Enter phone number (10 digits): ")
    email = input("Enter email address: ")
    while not re.match(email_regex, email):
        print("Invalid email format! Please enter a valid email address.")
        email = input("Enter email address: ")
    additional_info = input("Enter additional information (optional): ")
    contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'additional_info': additional_info}
    print(f"Contact added: {name} ({phone})")

# Function to edit an existing contact
def edit_contact():
    print("\nEditing an existing contact:")
    phone = input("Enter phone number of the contact to edit: ")
    if phone in contacts:
        print(f"Current details for {contacts[phone]['name']}:")
        print(f"Phone: {contacts[phone]['phone']}")
        print(f"Email: {contacts[phone]['email']}")
        print(f"Additional Info: {contacts[phone]['additional_info']}")
        print("Enter new details (leave blank to keep current):")
        name = input(f"Enter name [{contacts[phone]['name']}]: ") or contacts[phone]['name']
        email = input(f"Enter email address [{contacts[phone]['email']}]: ") or contacts[phone]['email']
        additional_info = input(f"Enter additional information [{contacts[phone]['additional_info']}]: ")
        contacts[phone] = {'name': name, 'phone': phone, 'email': email, 'additional_info': additional_info}
        print(f"Contact updated: {name} ({phone})")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    print("\nDeleting a contact:")
    phone = input("Enter phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print(f"Contact with phone number {phone} deleted.")
    else:
        print("Contact not found.")

# Function to search for a contact
def search_contact():
    print("\nSearching for a contact:")
    phone = input("Enter phone number of the contact to search for: ")
    if phone in contacts:
        print(f"Contact found:")
        print(f"Name: {contacts[phone]['name']}")
        print(f"Phone: {contacts[phone]['phone']}")
        print(f"Email: {contacts[phone]['email']}")
        print(f"Additional Info: {contacts[phone]['additional_info']}")
    else:
        print("Contact not found.")
        
# Function to display all contacts
def display_contacts():
    print("\nAll contacts:")
    for phone, contact in contacts.items():
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Additional Info: {contact['additional_info']}")

# Function to export contacts to a text file
def export_contacts():
    filename = input("Enter filename to export contacts (e.g., contacts.txt): ")
    with open(filename, 'w') as file:
        json.dump(contacts, file)
    print(f"Contacts exported to {filename}.")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            print("Importing contacts from a text file (Bonus feature).")
            # Implement import_contacts function if you want to add this feature
        elif choice == '8':
            print("Exiting the Contact Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()