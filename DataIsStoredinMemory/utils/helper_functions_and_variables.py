"""
Concerned with storing and retrieving books from a list.
"""

books =[]

USER_CHOICE = """
Enter:
- "a" to add a new book
- "l" to list all your books
- "r" to mark a book as read
- "d" to delete a book
- "q" to quit

Your choice:
"""


def prompt_add_book():
    book_name = input("Please enter the name of the book: ")
    author_name = input("Please enter the name of the author of the book: ")
    books.append({"name" : book_name, "author" : author_name, "read" : False})
    print("Your book has been added to the library. Congratulations!")

def list_books():
    for book in books:
        print("Book Name: " + book["name"] + ". " + "Author: " + book["author"] + ". " +"Is book read? " + 
              str(book["read"]) + ".")
    print("You have listed all your books. Cheers!")

def prompt_read_book():
    read_book_name = input("Please enter the name of the book you've read: ")
    read_book_author = input("Please enter the author of the book you've read: ")
    for book in books:
        if book["name"] == read_book_name and book["author"] == read_book_author:
            book["read"] = True
    print("You have marked your book read. Wonderful!")

def prompt_delete_book():
    delete_book_name = input("Please enter the name of the book you want to delete: ")
    delete_book_author = input("Please enter the author of the book you want to delete: ")
    for book in books:
        if book["name"] == delete_book_name and book["author"] == delete_book_author:
            books.remove(book)
    print("You have deleted your book from your library. Congratulations!")


dictionary_of_functions = {"a" : prompt_add_book, 
                           "l" : list_books, 
                           "r" : prompt_read_book, 
                           "d" : prompt_delete_book, 
                            }

def menu():
    user_input = input(USER_CHOICE)
    while user_input != "q":
        if user_input in dictionary_of_functions.keys():
            func = dictionary_of_functions[user_input]
            func()
        else:
            print("You have entered an invalid character.")
        user_input = input(USER_CHOICE)