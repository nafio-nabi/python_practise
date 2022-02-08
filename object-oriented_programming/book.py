class Book:
    def __init__(self, name, author, pages, isbn_thirteen):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn_thirteen = isbn_thirteen
    
    def print_book_info(self):
        return f"Name: {self.name}. Author: {self.author}. Pages: {self.pages}. ISBN-13: {self.isbn_thirteen}."