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
        filenames = os.listdir(dirname +'/')
        books = []
        for filename in filenames:
            d = self.load_book(filename)
            books.append(d)
        return books


    def build_book(self, title, authors, sub_title= '', publisher = '', pubish_year = -1, read_date = '', owner = '',
                   user = '', rating = -1, notes = ''):
        authors = authors.split(',')
        d = {
            "Title": title,
            "SubTitle": sub_title,
            "Authors": authors,
            "Publisher": publisher,
            "Year": pubish_year,
            "ReadDate": read_date,
            "Owner": owner,
            "User": user,
            "Rating": rating,
            "Notes": rating
        }
        return d

    def save_book(self, book):
        title = book["Title"]
        title = title.lower()
        title = title.replace(" ", '_')
        with open(self.get_filename(title) + '.json', 'w') as f:
            json.dump(book, f)


books = IObooks('books')
book1 = books.build_book("Wlamywacz", 'Lona, Webber')
print(book1)
books.save_book(book1)