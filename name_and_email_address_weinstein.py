"""This program acts as an address book for email addresses. It has the options to look up a person's email address, add a new name and email addres, change an existing email address, and delete an existing name and email address.

Programmer: David Weinstein
Date: 12/11/2019
Filename: name_and_email_address_weinstein.py

Pseudocode:
"""
from breezypythongui import EasyFrame
import pickle

class AddressBook(EasyFrame):
    """Address book for email addresses. Options to look up, add, edit, and delete email addresses from contacts."""
    #set up dictionary and class variables for pickle.
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
        self.editButton = self.addButton(text="Edit Contact", row=2, column=0)
        self.addLabel(text="Enter name of contact to edit:", row=2, column=1)
        self.nameToEdit = self.addTextField(text="", row=2, column=2)
        self.addLabel(text="New Email Address:", row=2, column=3)
        self.newEmail = self.addTextField(text="", row=2, column=4)
        self.deleteButton = self.addButton(text="Delete Contact", row=3, column=0)
        self.addLabel(text="Enter name to delete:", row=3, column=1)
        self.nameToDelete = self.addTextField(text="", row=3, column=2)
        self.saveAndQuit = self.addButton(text="Save and Quit", row=4, column=0, command=self.save)
        self.outputArea = self.addTextArea(text="", row=5, column=0, columnspan=5, height=10)
        self.test = self.addButton(text="test", row=4, column=1, command=self.testing)

    def search(self):
        searchName = self.nameSearch.getText()
        self.outputArea.setText("")
        if searchName != "":
            pickleIn = open("emails.dat", "rb")
            AddressBook.contactDict = pickle.load(pickleIn)
            for k in AddressBook.contactDict:
                if searchName == k:
                    self.outputArea["state"] = "normal"
                    self.outputArea.appendText(AddressBook.contactDict[k])
                    return
            self.outputArea["state"] = "normal"
            self.outputArea.appendText("Name not found.")

    def addAddress(self):
        newName = self.addName.getText()
        newEmail = self.addEmail.getText()
        if newName != "" and newEmail != "":
            AddressBook.contactDict[newName] = newEmail
            pickleOut = open("emails.dat", "wb")
            pickle.dump(AddressBook.contactDict, pickleOut)
            pickleOut.close()
            self.outputArea["state"] = "normal"
            self.outputArea.appendText("Contact added!")
            self.addName.setText("")
            self.addEmail.setText("")
        else:
            self.outputArea.appendText("Provide neccessary info.")
            
    def editAddress(self):
        pass

    def deleteAddress(self):
        pass

    def save(self):
        pickleOut = open("emails.dat", "wb")
        pickle.dump(AddressBook.contactDict, pickleOut)
        pickleOut.close()
        self.quit()

    def testing(self):
        pickleIn = open("emails.dat", "rb")
        AddressBook.contactDict = pickle.load(pickleIn)
        self.outputArea["state"] = "normal"
        self.outputArea.appendText(AddressBook.contactDict)


def main():
    AddressBook().mainloop()

if __name__ == "__main__":
    main()
