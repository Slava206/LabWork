class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_info(self):
        return f"Названеи книги:{self.title}, Автор:{self.author}, Год написания:{self.year}"
book = Book("Вий", "Н.В.Гоголь","1833")
print(book.get_info())