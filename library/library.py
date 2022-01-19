"""A representation of a library with books"""
from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + ' by ' + self.author


class Library:
    def __init__(self, books: List[Book] = None):
        if books:
            self.books = books
        else:
            self.books = []

    def __len__(self):
        return len(self.books)

    def __getitem__(self, item):
        return self.books[item]

    def add_book(self, title, author):
        self.books.append(Book(title=title, author=author))

    def by_author(self, author):
        author_books = []
        for book in self.books:
            if book.author == author:
                author_books.append(book)
        if author_books:
            return author_books
        else:
            raise KeyError("Author does not exist")


