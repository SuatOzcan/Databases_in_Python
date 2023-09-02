"""
Concerned with storing and retrieving books from a JSON file.
"""

from .database_connection import DatabaseConnection

books = [] # 'books' variable will be a list of dictionaries.
library_file = "library.txt"
USER_CHOICE = USER_CHOICE = """
                                    Enter:
                                    - "a" to add a new book
                                    - "l" to list all your books
                                    - "r" to mark a book as read
                                    - "d" to delete a book
                                    - "q" to quit

                                    Your choice:
                                    """

def create_book_table():
    with DatabaseConnection() as connection:
        cursor =connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')

    

# def create_book_teble():
#     with open(library_file,'w') as file:
#         json.dump([],file)
    
def add_book_to_library(book_name, author_name):
    # ",0) ;DROP TABLE books;  # instead of author_name. Our code may be a target for SQL Injection if we directly use the arguments.
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(f'INSERT INTO books VALUES(?,?,0)' , (book_name, author_name))
        #cursor.execute(f'INSERT INTO books VALUES("{book_name}","{author_name}",0)')  # So this is not good practice.
        #cursor.execute(f'INSERT INTO books VALUES("{book_name}","",0) ;DROP TABLE books;",0)')
        except:
            print("This book is already in your library.")
        

def get_all_books_in_library_and_print_them():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * from books')
    
        books = [{"name" : row[0] , "author": row[1], "read": row[2]} for row in cursor.fetchall()]
            
    return books

    
def mark_book_as_read(read_book_name, read_book_author):

    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute(f'UPDATE books SET read = 1 WHERE name = ? AND author = ?',
                    (read_book_name,read_book_author,)) #Interesting, it gives an error if I code 
                                                        #(read_book_name,read_book_author) without a comma in the end
                                                        #and that error is "Database is locked."
    

def delete_book(delete_book_name, delete_book_author):
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute(f'DELETE FROM books WHERE name = ? AND author= ?',
                    (delete_book_name, delete_book_author))
