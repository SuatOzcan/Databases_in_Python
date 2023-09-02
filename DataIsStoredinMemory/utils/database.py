"""
Concerned with storing and retrieving books from a list.
"""

books = []

def add_book_to_library(book_name, author_name):
    books.append({"name" : book_name, "author" : author_name, "read" : False})

def get_all_books_in_library():
    for book in books:
        # print("Book Name: " + book["name"] + ". " + "Author: " + book["author"] + ". " + 
        #  "Is book read? " + str(book["read"]) + ".")
        read_or_not = "Yes" if book["read"] == True else "No"
        print(f"Book Name: {book['name']}. Author: {book['author']}. Is book read? {read_or_not}.")
    

def mark_book_as_read(read_book_name, read_book_author):
    for book in books:
        if book["name"] == read_book_name and book["author"] == read_book_author:
            book["read"] = True

# def delete_book(delete_book_name, delete_book_author):
#     for book in books:
#         if book["name"] == delete_book_name and book["author"] == delete_book_author:
#             books.remove(book)
# This is not good practice because when we remove an item during iteration it may disrupt the order of indices and 
# confuse Python. We may miss some indices or skip some.

def delete_book(delete_book_name, delete_book_author):
    global books
    books = [book for book in books if not (book["name"] == delete_book_name and 
                                            book["author"] == delete_book_author)]
    