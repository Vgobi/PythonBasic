import iobooks

class BooksOrganizer:

    def __init__(self, dirpath):
        self.io = iobooks.IObooks(dirpath)
        self.books = self.io.load_books()

    def add_book(self, **kwargs):
        book = iobooks.build_book(**kwargs)
        self.io.save_book(book)

    def filter_book(self,arg, value):
        l = []
        for book in self.books:
            if book[arg] == value:
                l.append(book)
        return l

    def find_book(self, arg, value):
        l = self.filter_book(arg, value)
        if len(l) != 1:
            raise Exception('Blad wyszukiwania. Istnieje wiecej niz jedna szukana ksiazka')
        return l[0]

    def modify_book(self, arg, value, set_arg, set_value):
        book = self.find_book(arg, value)
        book[set_arg] = set_value
        self.io.save_book(book)

    def get_all_books(self):
        return self.books

b = BooksOrganizer("books")
b.add_book(title="Encyklopedia Cyckow", authors=['Kobiety'])
# print(b.find_book(title='Encyklopedia Cyckow'))
b.modify_book('title' ,'Encyklopedia Cyckow', 'authors', ['Kobiety, mezczyzni'])

for book in b.get_all_books():
    print(book)