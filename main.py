# import functions from utilities
from utilities import addBooks, removeBooks, viewBooks, borrowBooks

# Create booklist with predefined books
bookList = [
    {'id': 101, 'name': 'romeo and juliet', 'author': 'shakespeare'},
    {'id': 102, 'name': 'romeo', 'author': 'sp'},
    {'id': 103, 'name': 'juliet', 'author': 'spr'}
]

# Create borrow list with dummy data
borrowList = [
    {'id': 99, 'name': 'dummy', 'author': 'dummy'}
]

# Initialize user choice
userChoice = 0

# Itterate until user quits
while userChoice != 6:
    # Take user input
    userChoice = int(input("What do you want to do?\n1. Add books\n2. Remove books\n3. View books\n4. Borrow\n5. Quit\n\n"))

    # If user chooses to add, add books function is called
    if userChoice == 1:
        addBooks(bookList)
    
    # If user chooses to remove books, remove books function is called
    if userChoice == 2:
        removeBooks(bookList)
    
    # If user chooses to view books, view books function is called
    if userChoice == 3:
        viewBooks(bookList)

    # If user chooses to borrow books, borrow books function is called
    if userChoice == 4:
        bookList,borrowList = borrowBooks(bookList,borrowList)
    
    # If user chooses to quit program, the while loop will quit
    if userChoice == 5:
        break
