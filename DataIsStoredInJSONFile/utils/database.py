"""
Concerned with storing and retrieving books from a JSON file.
"""

import json

books = [] # 'books' variable will be a list of dictionaries.
library_file = "library.txt"

def create_book_table():
    try:
        with open(library_file,'r') as file:
            global books
            books = json.load(file)
    except:
        with open(library_file,'w') as file:
            file.write('[]')

# def create_book_table():
#     with open(library_file,'w') as file:
#         json.dump([],file)
    
def add_book_to_library(book_name, author_name):
    books.append({'name' : book_name, 'author' : author_name, 'read' : False})

    with open(library_file, "w") as file:        
        json.dump(books, file)

def get_all_books_in_library_and_print_them():
        with open(library_file, "r") as file:
            books = json.load(file)
            
        for book in books:
            read_or_not = "Yes" if book["read"] == True else "No"
            print(f'Book Name: {book["name"]}. Author: {book["author"]}. Is book read? {read_or_not}.')


    
def _get_all_books_in_library():
        with open(library_file, "r") as file:
            books = json.load(file)
        return books
    
def mark_book_as_read(read_book_name, read_book_author):

        books = _get_all_books_in_library()

        for book in books:
            if book["name"] == read_book_name and book["author"] == read_book_author:
                book["read"] = True
 
            with open(library_file,"w") as file:
                json.dump(books,file)
        
        for book in books:
            read_or_not = "Yes" if book["read"] == True else "No"
            print(f'Book Name: {book["name"]}. Author: {book["author"]}. Is book read? {read_or_not}.')


def delete_book(delete_book_name, delete_book_author):
    global books
    books = _get_all_books_in_library()
    books = [book for book in books if not (book["name"] == delete_book_name and 
                                           book["author"] == delete_book_author)]

    with open(library_file,'w') as file:
        json.dump(books,file)
