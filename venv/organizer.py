import iobooks

class BooksOrganizer:

    def __init__(self, dirpath):
        self.io = iobooks.IObooks(dirpath)
        self.books = self.io.load_books()

    def add_book(self,title, authors, *args, **kwargs):
        book = iobooks.build_book(title, authors, *args,  **kwargs)
        self.io.save_book(book)

    def modify_book(self):
        pass

    def get_all_books(self):
        return self.books

b = BooksOrganizer('books')
b.add_book("Encyklopedia Cyckow", 'Kobiety')