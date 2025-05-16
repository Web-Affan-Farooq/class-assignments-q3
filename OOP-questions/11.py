class Book:
    total_books = 0
    @classmethod
    def increment_book_count(cls):
        cls.total_books +=1

b1 = Book()
b1.increment_book_count()
b1.increment_book_count()
b1.increment_book_count()
print(b1.total_books)