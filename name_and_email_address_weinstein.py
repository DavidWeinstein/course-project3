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

    def __init__(self):
        """Sets up window and widgets."""
        EasyFrame.__init__(self, "Email Address Book")
        self.searchButton = self.addButton(text = "Search", row = 0, column=0)
        self.addLabel(text="Enter Name to Search:", row=0, column=1)
        self.nameSearch = self.addTextField(text="", row=0, column=2)
        self.addLabel(text="Enter Email to Search:", row=0, column=3)
        self.emailSearch = self.addTextField(text="", row=0, column=4)
        self.addContact = self.addButton(text="Add Contact", row=1, column=0)
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
        self.saveAndQuit = self.addButton(text="Save and Quit", row=4, column=0)
        self.outputArea = self.addTextArea(text="", row=5, column=0, columnspan=5, height=10)


def main():
    AddressBook().mainloop()

if __name__ == "__main__":
    main()
