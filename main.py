import json 

"""
Concerned with storing and retrieving books from a json file. 

[
  {
    'name': 'Clean Code', 
    'author': 'Trisha'
    'read': True
  }
]
"""

books_file = 'books.json'


def create_book_table(): 
    with open(books_file, 'w'): 
        pass  # just to make the file is there 


def add_book(name, author): 
   books = get_all_books()
   books.append({'name': name, 'author': author, 'read': False})
   _save_all_books(books)


   def get_all_books(): 
    with open(books_file, 'r') as file: 
        return json.load(file)


def _save_all_books(books): 
    with open(books_file, 'w') as file: 
        for book in books: 
            file.write(f"{book['name']},{book['author']},{book['read']}\n")



def mark_book_as_read(name):
    books = get_all_books()
    for book in books: 
        if book['name'] == name: 
            book['read'] = '1'
    _save_all_books(books)


