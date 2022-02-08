from book import Book

book_one = Book("Atomic Habits", "James Clear", "320", "978-0735211292")
print(f"Name: {book_one.name}")
print(f"Author: {book_one.author}")
print(f"Pages: {book_one.pages}")
print(f"ISBN-13: {book_one.isbn_thirteen}")

print()
print(book_one.print_book_info())
print()

book_two = Book("Think Again", "Adam Grant", "320", "978-1984878106")
print(f"Name: {book_two.name}")
print(f"Author: {book_two.author}")
print(f"Pages: {book_two.pages}")
print(f"ISBN-13: {book_two.isbn_thirteen}")

print()
print(book_two.print_book_info())
print()
