"""This program acts as an address book for email addresses. It has the options to look up a person's email address, add a new name and email addres, change an existing email address, and delete an existing name and email address.

Programmer: David Weinstein
Date: 12/11/2019
Filename: name_and_email_address_weinstein.py

Pseudocode:
1. From breezypythongui import EasyFrame
2. Import pickle
3. Create new class AddresBook as a subclass of EasyFrame
4. Set up class dictionary as empty dictionary if first time opening program.
5. Set up __init__ constructor method with appropriate buttons, labels, and textfields and textarea
6. Define search button function.
    6a. If text field not blank search through dictionary
    6b. Output name and email if found.
    6c. Output "name not found" if not in dictionary
7. Define add contact button function.
    7a. If name and email text fields are not blank, create key value pair in dictionary
8. Define edit contact button function.
    8a. If name and email text fields are not blank, search dictionary for name
    8b. If name is found in dictionary, edit email and update dictionary
    8c. If name is not found output "name not found"
9. Define delete contact button function.
    9a.If name text field is not blank, search dictionary for name
    9b. If name is found, delete name and email from dictionary and update dictionary
10. Define save and quit button function.
    10a. Updates file with most up to date dictionary and saves file, and exits the program
"""
from breezypythongui import EasyFrame
import pickle

class AddressBook(EasyFrame):
    """Address book for email addresses. Options to look up, add, edit, and delete email addresses from contacts."""
    #set up class dictionary
    contactDict = {}

    def __init__(self):
        """Sets up window and widgets."""
        EasyFrame.__init__(self, "Email Address Book")
        self.searchButton = self.addButton(text = "Search", row = 0, column=0, command=self.search)
        self.addLabel(text="Enter Name to Search:", row=0, column=1)
        self.nameSearch = self.addTextField(text="", row=0, column=2)
        self.addContact = self.addButton(text="Add Contact", row=1, column=0, command=self.addAddress)
        self.addLabel(text="Enter Name:", row=1, column=1)
        self.addName = self.addTextField(text="", row=1, column=2)
        self.addLabel(text="Enter Email:", row=1, column=3)
        self.addEmail = self.addTextField(text="", row=1, column=4)
        self.editButton = self.addButton(text="Edit Contact", row=2, column=0, command=self.editAddress)
        self.addLabel(text="Enter name of contact to edit:", row=2, column=1)
        self.nameToEdit = self.addTextField(text="", row=2, column=2)
        self.addLabel(text="New Email Address:", row=2, column=3)
        self.newEmail = self.addTextField(text="", row=2, column=4)
        self.deleteButton = self.addButton(text="Delete Contact", row=3, column=0, command=self.deleteAddress)
        self.addLabel(text="Enter name to delete:", row=3, column=1)
        self.nameToDelete = self.addTextField(text="", row=3, column=2)
        self.saveAndQuit = self.addButton(text="Save and Quit", row=4, column=0, command=self.save)
        self.outputArea = self.addTextArea(text="", row=5, column=0, columnspan=5, height=10)

    def search(self):
        """Searches through current contacts for their email"""
        # Grabs name search text and creates a variable. Resets ouput area
        searchName = self.nameSearch.getText()
        self.outputArea.setText("")

        # try/except for error if searching for a contact with no dictionary yet created.
        try:
            # if search name not blank, open up to date dictionary with pickle, search through dictionary, print desired output
            if searchName != "":
                pickleIn = open("emails.dat", "rb")
                AddressBook.contactDict = pickle.load(pickleIn)
                for k in AddressBook.contactDict:
                    if searchName == k:
                        self.outputArea["state"] = "normal"
                        self.outputArea.appendText("Name: " + searchName + "\n" "Email: " + AddressBook.contactDict[k])
                        self.nameSearch.setText("")
                        return
                self.outputArea["state"] = "normal"
                self.outputArea.appendText("The specified name was not found.")
                self.nameSearch.setText("")
        except OSError:
            self.outputArea.appendText("The specified name was not found.")
            self.nameSearch.setText("")
            

    def addAddress(self):
        """Adds new email address and name to dictionary"""

        # gets text from addName and addEmail text field and create variable, reset output area.
        newName = self.addName.getText()
        newEmail = self.addEmail.getText()
        self.outputArea.setText("")
        # if name and email not blank create new key value pair and save to file with pickle, print desired output.
        if newName != "" and newEmail != "":
            AddressBook.contactDict[newName] = newEmail
            pickleOut = open("emails.dat", "wb")
            pickle.dump(AddressBook.contactDict, pickleOut)
            pickleOut.close()
            self.outputArea["state"] = "normal"
            self.outputArea.appendText("Name and address have been added.")
            self.addName.setText("")
            self.addEmail.setText("")
        else:
            self.outputArea.appendText("Provide neccessary info.")
            
    def editAddress(self):
        """Edits existing address in dictionary."""

        # gets text from nameToEdit and newEmail and creates variable, resets output area
        name = self.nameToEdit.getText()
        emailEdit = self.newEmail.getText()
        self.outputArea.setText("")
        # if name and emailEdit not blank, load updated file with pickle
        if name != "" and emailEdit != "":
            pickleIn = open("emails.dat", "rb")
            AddressBook.contactDict = pickle.load(pickleIn)
            # search if name is in dictionary, update email address, save new info to file with pickle, print desired output
            for k in AddressBook.contactDict:
                if name == k:
                    AddressBook.contactDict[k] = emailEdit
                    self.outputArea.appendText("Information updated.")
                    pickleOut = open("emails.dat", "wb")
                    pickle.dump(AddressBook.contactDict, pickleOut)
                    pickleOut.close()
                    self.nameToEdit.setText("")
                    self.newEmail.setText("")
                    return
            self.outputArea.appendText("The specified name was not found.")
            self.nameToEdit.setText("")
            self.newEmail.setText("")

    def deleteAddress(self):
        """Deletes an existing address in dictionary."""

        # get text from nameToDelete and create variable, reset output area, open and load updated file with pickle
        delete = self.nameToDelete.getText()
        self.outputArea.setText("")
        pickleIn = open("emails.dat", "rb")
        AddressBook.contactDict = pickle.load(pickleIn)

        # if delete not blank, search if name is in dictionary and delete if it is, save updated file with pickle, print desired output
        if delete != "":
            for k in AddressBook.contactDict:
                if delete == k:
                    del AddressBook.contactDict[k]
                    pickleOut = open("emails.dat", "wb")
                    pickle.dump(AddressBook.contactDict, pickleOut)
                    pickleOut.close()
                    self.outputArea.appendText("Information deleted.")
                    self.nameToDelete.setText("")
                    return
            self.outputArea.appendText("The specified name was not found.")

    def save(self):
        """Saves and quits the program."""

        # open file and save up to date dictionary to file and close with pickle.
        pickleOut = open("emails.dat", "wb")
        pickle.dump(AddressBook.contactDict, pickleOut)
        pickleOut.close()
        self.quit()

def main():
    AddressBook().mainloop()

if __name__ == "__main__":
    main()
