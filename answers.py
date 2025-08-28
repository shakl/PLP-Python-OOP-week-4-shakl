# ENCAPSULATION
class Book:
    """A class representing a book with encapsulation"""

    def __init__(self, title: str, author: str, price: float):
        self._title = title      
        self._author = author    
        self._price = price      

    # Getter for title
    @property
    def title(self):
        return self._title

    # Setter for title 
    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty!")
        self._title = value

    # Getter for author
    @property
    def author(self):
        return self._author

    # Setter for author
    @author.setter
    def author(self, value):
        if not value.strip():
            raise ValueError("Author cannot be empty!")
        self._author = value

    # Getter for price
    @property
    def price(self):
        return self._price

    # Setter for price 
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

    def book_info(self):
        """Return formatted book details"""
        return f"📖 '{self._title}' by {self._author} - ${self._price:.2f}"
    
    # Create a book object
book1 = Book("The Alchemist", "Paulo Coelho", 12.99)

# Access data safely using getters
print(book1.book_info())  
# Modify values safely using setters
book1.price = 15.50
book1.title = "The Alchemist (Special Edition)"

print(book1.book_info()) 

# Invalid values raise errors
try:
    book1.price = -10
except ValueError as e:
    print("Error:", e)  


# POLYMORPHISM
# Base class 
class Mover:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

# Vehicle classes
class Car(Mover):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Mover):
    def move(self):
        return "✈️ Flying in the sky"

class Boat(Mover):
    def move(self):
        return "🚤 Sailing on water"

# Animal classes
class Dog(Mover):
    def move(self):
        return "🐕 Running happily"

class Bird(Mover):
    def move(self):
        return "🐦 Flying with wings"

class Fish(Mover):
    def move(self):
        return "🐟 Swimming in the water"

# Demonstration of polymorphism
def demonstrate_moves(movers):
    for mover in movers:
        print(mover.move())

# Create objects
things_that_move = [Car(), Plane(), Boat(), Dog(), Bird(), Fish()]

# Test polymorphism
demonstrate_moves(things_that_move)


