"""This program will search through the 200 most popular boy and girl names in the United States from the year 2000 through 2009. The end user will be able to type in either a boy or girl name, or both, and see if it is one of the most popular names from the lists. 

Programmer: David Weinstein
Date: 12/10/2019
Filename: name_search_weinstein.py

Pseudocode:
"""
from breezypythongui import EasyFrame

class NameSearch(EasyFrame):
    """A name search for boy and girl names, to check if they are in the most popular 200 names in the US"""

    def __init__(self):
        """Set up window and widgets"""
        EasyFrame.__init__(self, "Name Search")
        self.addLabel(text="Enter boy name, or leave blank:", row=0, column=0)
        self.boyName = self.addTextField("", row=0, column=1)
        self.addLabel(text="Enter girl name, or leave blank:", row=1, column=0)
        self.girlName = self.addTextField("", row=1, column=1)
        self.searchButton = self.addButton(text="Search", row=2, column=0, command=self.search)
        self.outputArea = self.addTextArea("", row=3, column=0, columnspan=2, width=50, height=4)

    def search(self):
        """Searches lists if anything is typed in search text areas."""
        boyNames = open("./BoyNames.txt", 'r')
        girlNames = open("./GirlNames.txt", 'r')
        boyList = boyNames.read().splitlines()
        girlList = girlNames.read().splitlines()
        boyName = self.boyName.getText()
        count = 0
        while count < len(boyList):
            if boyList[count] == boyName:
                self.outputArea["state"] = "normal"
                self.outputArea.setText(boyName + " is the most popular name")
                break
            else:
                count += 1

def main():
    NameSearch().mainloop()

if __name__ == "__main__":
    main()
