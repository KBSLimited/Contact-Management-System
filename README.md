Contact Management System
Welcome to the Contact Management System! This Python program allows users to manage their contacts through a command-line interface (CLI). Users can add, edit, delete, search, display, export contacts to a file, and optionally import contacts from a file.

Features
Add a new contact: Enter details such as name, phone number, email address, and additional information for a new contact.
Edit an existing contact: Modify any details of an existing contact based on their phone number.
Delete a contact: Remove a contact from the system using their phone number.
Search for a contact: Look up a contact by their phone number to view their details.
Display all contacts: View a list of all contacts stored in the system.
Export contacts to a text file: Save all contacts to a JSON file for backup or sharing.
Import contacts from a text file (Bonus): Read contacts from a JSON file and add them to the system.
Optional Features (Bonus Points)
Contact Categories: Categorize contacts into groups (e.g., friends, family, work).
Enhanced Contact Search: Search by name, phone number, email address, or additional information.
Contact Sorting: Display contacts alphabetically by name or based on other criteria.
Backup and Restore: Create automatic backups of contact data and restore data from backup files.
Custom Contact Fields: Define and store additional fields for contacts (e.g., birthdays, anniversaries).
Installation
Clone the repository:

bash
Copy code
git clone <https://github.com/KBSLimited/Contact-Management-System.git>
cd contact-management-system
Run the program:

Copy code
python contact_management.py
Follow the on-screen instructions to use the Contact Management System.

Usage
When you run the program, you will see a menu with options numbered from 1 to 8.
Enter the number corresponding to the action you want to perform (e.g., add a contact, edit a contact).
Follow the prompts to enter information as requested.
Use input validation to ensure correct formatting of contact details such as phone numbers and email addresses.
Errors or invalid inputs will be handled gracefully with appropriate error messages.
Examples
Adding a New Contact
mathematica
Copy code
Welcome to the Contact Management System!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file (BONUS)
8. Quit

Enter your choice: 1

Adding a new contact:
Enter name: John Doe
Enter phone number (10 digits): 1234567890
Enter email address: john.doe@example.com
Enter additional information (optional): Friend

Contact added: John Doe (1234567890)
Displaying All Contacts
yaml
Copy code
Enter your choice: 5

All contacts:
Name: John Doe, Phone: 1234567890, Email: john.doe@example.com, Additional Info: Friend
Exporting Contacts to a Text File
mathematica
Copy code
Enter your choice: 6
Enter filename to export contacts (e.g., contacts.json): contacts.json

Contacts exported to contacts.json.

Contributors
DeAndre Johnson

License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize this README file further based on your specific implementation and additional features you might include. Including clear instructions, examples, and a license statement will help users understand and utilize your Contact Management System effectively.