class API_Library:

    def __init__(self):
        self.books = [
            {'id': 1, 'title': '1984', 'author': 'George Orwell'},
            {'id': 2, 'title': 'Brave New World', 'author': 'Aldous Huxley'}
        ]

    def get_books(self):
        return self.books

    def get_book(self, book_id):
        book = next((book for book in self.books if book['id'] == book_id), None)
        return book if book else 'Book not found'

    def add_book(self, new_book):
        new_book['id'] = max(book['id'] for book in self.books) + 1
        self.books.append(new_book)
        return new_book

    def add_book2(self, new_book):
        self.books.append(new_book)
        return new_book

    def update_book(self, book_id, book_data):
        book = next((book for book in self.books if book['id'] == book_id), None)
        if book:
            book.update(book_data)
            return book
        return 'Book not found'

    def delete_book(self, book_id):
        book_i = next((i for i, book in enumerate(self.books) if book['id'] == book_id), None)
        if book_i is not None:
            return self.books.pop(book_i)
        return 'Book not found'


api = API_Library()
print(api.get_books())
print(api.get_book(1))
#print(api.add_book({'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}))
print(api.add_book2({'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'}))
print(api.update_book(1, {'title': 'Nineteen Eighty-Four'}))
print(api.delete_book(2))
print()
print(api.get_books())