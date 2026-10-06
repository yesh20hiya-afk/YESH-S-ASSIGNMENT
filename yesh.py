class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def borrow(self):
        is_borrowed = True
        print(f"{self.title} by {self.author} has been borrowed.")
        
    def return_book(self):
        is_borrowed = False
        print(f"{self.title} by {self.author} has been returned.")

Mybook1 = Book("Vachanamrut", "Swami Vivekananda")
Mybook2 = Book("Spy School", "Stuart Gibbs")
Mybook3 = Book("Shiskapatri", "Swami Vivekananda")

Mybook1.borrow()
Mybook2.borrow()
Mybook3.borrow()
Mybook1.return_book()
Mybook2.return_book()
Mybook3.return_book()