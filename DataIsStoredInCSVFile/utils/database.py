"""
Concerned with storing and retrieving books from a CSV file.
"""

library_file = "library.txt"

def create_book_table():
    with open(library_file,'a'):
        pass
    
def add_book_to_library(book_name, author_name):
    with open(library_file, "a") as file:
        file.write(f'{book_name},{author_name},No\n')

def get_all_books_in_library_and_print_them():
    books = _get_all_books_in_library()   
    for book in books:
        print(f'Book Name: {book["name"]}. Author: {book["author"]}. Is book read? {book["read"]}.')

def _get_all_books_in_library():
    with open(library_file, "r") as file:
         lines = [line.strip("\n").split(",") for line in file.readlines()]

    books =[
        {"name": line[0],"author":line[1],"read":line[2]}
        for line in lines
        ]
    return books



def mark_book_as_read(read_book_name, read_book_author):
    try:
        books = _get_all_books_in_library()

        for book in books:
            if book["name"] == read_book_name and book["author"] == read_book_author:
                book["read"] = "Yes"
 
        save_books_to_library(books)   
    except:
        USER_CHOICE = USER_CHOICE = """
                                    Enter:
                                    - "a" to add a new book
                                    - "l" to list all your books
                                    - "r" to mark a book as read
                                    - "d" to delete a book
                                    - "q" to quit

                                    Your choice:
                                    """
        user_input = input(USER_CHOICE)
        

    # with open(library_file,"r") as file:
    #     books_in_library = [line.strip("\n").split(",") for line in file.readlines()]
    #     # print(books_in_library)       
    
    #     for line in books_in_library:
    #         if line[0] == read_book_name and line[1] == read_book_author:
    #             line[2] = "Yes"
    #     books_in_library = [",".join(line) for line in books_in_library]
    #     #print(books_in_library)

    # with open(library_file,"w") as file:
    #     for line in books_in_library:
    #         file.write(f"{line}\n")

    

# def delete_book(delete_book_name, delete_book_author):
#     for book in books:
#         if book["name"] == delete_book_name and book["author"] == delete_book_author:
#             books.remove(book)
# This is not good practice because when we remove an item during iteration it may disrupt the order of indices and 
# confuse Python. We may miss some indices or skip some.

def save_books_to_library(books_in_library):
    with open(library_file,"w") as file:
                for book in books_in_library:
                    file.write(f'{book["name"]},{book["author"]},{book["read"]}\n') 

def delete_book(delete_book_name, delete_book_author):

    books =_get_all_books_in_library()
    
    books = [book for book in books if not (book["name"] == delete_book_name and 
                                           book["author"] == delete_book_author)]

    save_books_to_library(books)

    # with open(library_file,"r") as file:
    #     books_in_library = [line.strip("\n").split(",") for line in file.readlines()]
    #     # print(books_in_library)

    #     books_in_library  = [book for book in books_in_library  
    #                              if not (book[0] == delete_book_name 
    #                                     and book[1] == delete_book_author)]
        
    # books_in_library = [",".join(line) for line in books_in_library]

    # with open(library_file,"w") as file:
    #     for line in books_in_library:
    #         file.write(f"{line}\n")