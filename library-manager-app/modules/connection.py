# For database connection:
import sqlite3

def get_connection():
    connection = sqlite3.connect("./data/database.db") # requesting connection from sql file
    cursor = connection.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    BookName TEXT NOT NULL,
    AuthorName TEXT NOT NULL,
    Publication TEXT NOT NULL,
    Genre TEXT NOT NULL,
    Description TEXT NOT NULL,
    ReadStatus INTEGER 
);
""")
    connection.commit()

    # books = [
    #     ("To Kill a Mockingbird", "Harper Lee", "1960", "Fiction", "A novel about racial injustice in the Deep South.", 1),
    #     ("1984", "George Orwell", "1949", "Dystopian", "A chilling dystopian world under total surveillance.", 1),
    #     ("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Classic", "A tragic love story set in the Roaring Twenties.", 1),
    #     ("The Catcher in the Rye", "J.D. Salinger", "1951", "Fiction", "A teenager’s struggle with identity and alienation.", 0),
    #     ("Moby-Dick", "Herman Melville", "1851", "Adventure", "A captain’s obsessive quest for revenge on a whale.", 0),
    #     ("Pride and Prejudice", "Jane Austen", "1813", "Romance", "A witty romantic tale of love and social class.", 1),
    #     ("War and Peace", "Leo Tolstoy", "1869", "Historical Fiction", "An epic novel set during the Napoleonic Wars.", 0),
    #     ("The Hobbit", "J.R.R. Tolkien", "1937", "Fantasy", "A hobbit embarks on a grand adventure with dwarves.", 1),
    #     ("Fahrenheit 451", "Ray Bradbury", "1953", "Dystopian", "A future where books are banned and burned.", 1),
    #     ("Crime and Punishment", "Fyodor Dostoevsky", "1866", "Psychological Fiction", "A psychological exploration of guilt and redemption.", 0),
    #     ("Brave New World", "Aldous Huxley", "1932", "Dystopian", "A society controlled by pleasure and conformity.", 1),
    #     ("The Lord of the Rings", "J.R.R. Tolkien", "1954", "Fantasy", "A fellowship embarks on a quest to destroy a powerful ring.", 1),
    #     ("The Alchemist", "Paulo Coelho", "1988", "Adventure", "A shepherd’s journey in search of his destiny.", 1),
    #     ("The Book Thief", "Markus Zusak", "2005", "Historical Fiction", "A young girl steals books during Nazi Germany.", 0),
    #     ("Dracula", "Bram Stoker", "1897", "Horror", "The original vampire novel.", 0),
    #     ("Frankenstein", "Mary Shelley", "1818", "Horror", "A scientist creates a monstrous being.", 1),
    #     ("The Kite Runner", "Khaled Hosseini", "2003", "Drama", "A tale of friendship, betrayal, and redemption.", 1),
    #     ("The Road", "Cormac McCarthy", "2006", "Post-apocalyptic", "A father and son struggle to survive in a ruined world.", 0),
    #     ("Dune", "Frank Herbert", "1965", "Science Fiction", "A young hero rises in a desert planet's power struggle.", 1),
    #     ("The Shining", "Stephen King", "1977", "Horror", "A family is haunted in a remote hotel.", 0)
    # ]
    
    # cursor.executemany("INSERT INTO books (BookName,AuthorName,Publication, Genre, Description, ReadStatus) VALUES (?,?,?,?,?,?)", books)
    # connection.commit()

    # print("Data seeded successfully")
    return {
        "Connection":connection,
        "Cursor":cursor
    }
# get_connection()