import random as ran
import pandas as pd

def addBooks(bL):
    '''
    This function creates a unique ID for the book and adds it to the existing booklist.
    bL: Existing booklist
    '''

    #create empty book dictionary
    book = {}

    # creating a panda dataframe with respect to book list
    myBooks = pd.DataFrame(bL)

    # Storing all the existing book ID's in a variable
    existingID = list(myBooks.id)

    # Generating a random number between 100 and 1000
    randomID = ran.randint(100,1000)
    
    # Iterating until generated ID doesn't exist in the all ID's list
    while randomID in existingID:
        randomID = ran.randint(100,1000)

    # Taking user input for book Name
    bookName = input("Enter the book name: ")
    
    # Taking user input for book author
    bookAuthor = input("Enter the book author: ")

    # assigning values to book parameters
    book['id'] = randomID
    book['name'] = bookName
    book['author'] = bookAuthor

    # Appending book to book list
    bL.append(book)
    print()


def removeBooks(bL):
    '''
    This function removes books from the book list based on the ID given to us from the user
    bL: book list
    '''

    # Displays books available to remove
    viewBooks(bL)

    # Takes user input for the ID of book
    bookIDRemove = int(input("Enter the book ID of the book you want to remove: "))

    # Assigning panda datafram to variable
    data = pd.DataFrame(bL)

    # Assigning ID list to variable
    IDList = list(data['id'])

    # Iterrating until the chosen ID is not found
    for i in range(len(bL)):
        if bookIDRemove == IDList[i]:
            # Remove the book from book list when found
            bL.pop(i)
    print()


def viewBooks(bL):
    '''
    The function allows the user to view books in book list
    bL: book List
    '''

    # Counts the number of books
    totalBooks = len(bL)

    # Displays the available number of books
    print(f'Total number of books available in library: {totalBooks}')

    # Displays the entire booklist only when the book list has some item
    if (totalBooks > 0):
        print("Below are the books available in the library: ")
        print(pd.DataFrame(bL).reindex(columns=['id','name','author']))
    print()


def borrowBooks(bL,bRL):
    '''
    This function allows users to borrow books from the library
    bL: book list
    bRL: borrowed book list
    '''

    # Calls view books function so user can see the books to choose
    viewBooks(bL)

    # Storing all the ID's of existing book list
    blIDs = [bL[i]['id'] for i in range(len(bL))]

    # Taking user input of the ID of the book the user wants to borrow
    borrowInput = int(input("Enter the ID of the book you want to borrow: "))

    # Condition to see if the borrow ID exists in available books
    if borrowInput not in blIDs:
        print("ID not found")
    else:
        for i in range(len(bL)):
            # Condition to see if the existing ID found is equal to borrowed ID
            if bL[i]['id'] == borrowInput:
                borrowedBook = bL[i]['name']

                # Adds entered book into borrow list
                bRL.extend(bL[i])

                # Deletes borrowed book from book list
                bL.pop(i)
                break
        print(f'The book {borrowedBook} has been borrowed successfully')

    # returns both book list and borrow list
    return bL, bRL



# def returnBooks(bL,bRL):
#     viewBooks(bRL)
#     bRLIDs = [bRL[i]['id'] for i in range(len(bRL))]
#     returnBookInput = int(input("Enter the ID of the book you want to return: "))
#     if returnBookInput not in bRLIDs:
#         print("ID not found")
#     else:
#         for i in range(len(bRL)):
#             if bRL[i]['id'] == returnBookInput:
#                 returnedBook = bRL[i]['name']
#                 bL.extend(bRL[i])
#                 bRL.pop(i)
#                 break
#         print(f'The book {returnedBook} has been returned successfully')
#     return bL,bRL