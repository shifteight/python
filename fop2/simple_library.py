"""
A simple library modelled as a collection of
books and patrons.
"""


class Book(object):

    def __init__(self, title, author, patron=None):
        self._title = title
        self._author = author
        self._patron = patron
        self._waiting_patrons = []

    def get_patron(self):
        return self._patron

    def borrowed(self):
        if self._patron:
            return True

    def back(self):
        self._patron = None

    def checked_by(self, patron):
        self._patron = patron

    def booked_by(self, patron):
        self._waiting_patrons.append(patron)

    def show_status(self):
        print("checked by %s." % self._patron.get_name())
        print("waiting list:")
        for p in self._waiting_patrons:
            print(p.get_name())

    def __str__(self):
        return "%s, %s" % (self._title, self._author)


class Patron(object):

    def __init__(self, name):
        self._name = name
        self._number_of_books = 0

    def get_name(self):
        return self._name

    def borrow_book(self, book):
        if not book.borrowed():
            self._number_of_books += 1
            book.checked_by(self)
        elif book.get_patron().get_name() == self._name:
            print("You have borrowed the book. Please choose another book.")
        else:
            book.booked_by(self)

    def show_books(self):
        print("%s borrowed %d book(s)" % (self._name, self._number_of_books))


class Library(object):
    pass


def test():
    """test program."""

    b1 = Book("book 1", "author 1")
    b2 = Book("book 2", "author 2")
    print(b1)
    print(b2)

    p1 = Patron("P1")
    p2 = Patron("P2")
    p1.borrow_book(b1)
    p1.show_books()
    p1.borrow_book(b1)

    b1.show_status()

    p2.borrow_book(b1)
    b1.show_status()

    p2.borrow_book(b2)
    b2.show_status()

    p2.borrow_book(b2)


if __name__ == '__main__':
    test()
