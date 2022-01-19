import pytest


@pytest.fixture
def example_library():
    from library import Library

    lib = Library()

    lib.add_book('My First Book', 'Alice')
    lib.add_book('My Second Book', 'Alice')
    lib.add_book('A Different Book', 'Bob')
    return lib


def test_create_book():
    from library import Book

    title = 'Watership Down'
    author = 'Richard Adams'
    b = Book(title, author)
    assert (b.title, b.author) == (title, author)


def test_library_add_book(example_library):
    assert (example_library.books[0].title, example_library.books[0].author) \
           == ("My First Book", "Alice")


def test_library_length(example_library):
    assert len(example_library) == 3


def test_library_index_access(example_library):
    book = example_library[2]
    assert (book.title, book.author) == ('A Different Book', 'Bob')


def test_library_by_author(example_library):
    test_books = (('My First Book', 'Alice'), ('My Second Book', 'Alice'))
    books = example_library.by_author('Alice')
    assert len(books) == 2
    for i in range(len(test_books)):
        assert (books[i].title, books[i].author) == test_books[i]


def test_library_by_author_keyerror(example_library):
    with pytest.raises(KeyError):
        example_library.by_author('Carol')

