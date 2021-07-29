import json
import os


class IObooks:

    def __init__(self, dirname):
        self.dirname = dirname

    def get_filename(self, book):
        return self.dirname + '/' + book

    def load_book(self, filename):

        with open(self.get_filename(filename), 'r') as f:
            text = json.load(f)
            return text

    def load_books(self):
        filenames = os.listdir(self.dirname +'/')
        books = []
        for filename in filenames:
            d = self.load_book(filename)
            books.append(d)
        return books

    def save_book(self, book):
        title = book["title"]
        title = title.lower()
        title = title.replace(" ", '_')
        with open(self.get_filename(title) + '.json', 'w') as f:
            json.dump(book, f)

def build_book(**kwargs):
    required = ['title', 'authors']
    optional = [
        ("sub_title", ''),
        ("publisher", ''),
        ("pubish_year", -1),
        ("read_date", ''),
        ("owner", ''),
        ('user', ''),
        ('rating', -1),
        ('notes', '')
    ]

    for arg in required:
        if arg not in kwargs:
            raise Exception(arg + ' nie instnieje w obiekcie!')

    for arg, default in optional:
        if arg not in kwargs:
            kwargs[arg] = default

    return kwargs

if __name__ == '__name__':
    books = IObooks('books')
    book1 = build_book(title= "Wlamywacz", authors=['Lona', 'Webber'])
    print(book1)
    books.save_book(book1)