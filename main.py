# book library program
# bookList = [""]
# userChoice = input("Do you want to add, remove, or view books: ")

# def addBooks(userChoice):
#     #enter function command here
#     while userChoice == "Add" or "add":
#         userAdd = input("Enter the book name you want to add: ")
#         bookList.append(userAdd)

# def removeBooks(userChoice):
#     #enter function command here
#     while userChoice == "remove" or "Remove":
#         userRemove = input("Enter the book name that you want to remove: ")
#         bookList.remove(userRemove)

# def viewBooks(userChoice):
#     while userChoice == "view" or "View":
#         print(bookList)


#restarting the program


bookList = []


def addBooks(bookAddInput):
    #enter function command here
    bookList.append(bookAddInput)
    print()
def removeBooks(bookRemoveInput):
    #enter function command here
    bookList.remove(bookRemoveInput)
    print()

def viewBooks(bookList):
  totalBooks = len(bookList)
  print(f'Total number of books available in library: {totalBooks}')
  if (totalBooks > 0):
    print("Below are the books available in the library: ")
    for i in range(totalBooks):
      print(str(i+1)+".", bookList[i])
  print()

userChoice = 0
while userChoice != 4:
    userChoice = int(input("What do you want to do?\n1. Add books\n2. Remove books\n3. View books\n4. Quit\n\n"))
    if userChoice == 1:
        bookAddInput = input("Enter the book name that you would like to add: ")
        addBooks(bookAddInput)
    if userChoice == 2:
        bookRemoveInput = input("Enter the book name that you would like to remove: ")
        removeBooks(bookRemoveInput)
    if userChoice == 3:
        viewBooks(bookList)

#update your removeBook function by improving the user experience. Let them choose what book to remove