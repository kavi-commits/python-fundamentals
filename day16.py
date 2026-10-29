#day 16 week 4 more on oop with python

# __str__ : how an object describes  itself
class Dog:
    def __init__(self, name):
        self.name = name

    def  __str__(self):
        return f"Dog : {self.name}"
d = Dog("Tommy")
print(d) # Dog: Rex

# class attributes Vs instance attributes

class Dog:
    species = "Canis familiaris" # class attributes shared by all dogs

    def __init__(self, name):
        self.name = name

d1 = Dog("Tommy")
d2 = Dog("Jerryca")
print(d1.species, d2.species) # same value
print(d1.name, d2.name) # different values
# class attributes defined in the class body, one copy shared by every object. Instance attribute defined via self, in __init__, separate per object. Use a class attribute for shared constants (like species), an instance attribute for per-object data(like name).

# Why  a class instead of a dictionary?
# ANS: A dictionary holds data, A class holds data and behavior that belongs to it.

# 4. Building library.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self.books = [] # list of Book objects

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if  not  self.books:
            print("No books")
            return
        for i, book in enumerate((self.books), 1):
            print(i, book)

    def search_by_title(self,title):
        matches = [b for b in self.books if title.lower() in b.title.lower()]
        if not matches:
            print("No books with that title")
        return matches


lib = Library()
lib.add_book(Book("Dune", "Herbert"))
lib.add_book(Book("Neuromancer", "Gibson"))
lib.add_book(Book("Dune Messiah", "Herbert"))

lib.list_books()
lib.search_by_title("dune")
lib.search_by_title("Zzz")
















