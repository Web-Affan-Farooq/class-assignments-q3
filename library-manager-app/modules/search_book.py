# ____Function for searching book 
import questionary
from modules import connection

db = connection.get_connection()
connection =  db["Connection"]
cursor = db["Cursor"]

def search_book():
    book_name = questionary.text("Enter book name").ask()
    cursor.execute("SELECT * FROM books WHERE LOWER(BookName) LIKE LOWER(?)", ('%' + book_name + '%',))
    rows = cursor.fetchall()

    # If search matches found ...   
    if(len(rows) != 0):
            search_options = [row[0] for row in rows]
            selected_book = questionary.select("Related matches", choices=search_options).ask()
            
            cursor.execute("SELECT * FROM books WHERE BookName = ?", (selected_book,))
            connection.commit()
            [book] = cursor.fetchall()  # returns a list 
            print(f"-----------------------{book[0]}--------------------------")
            print(f"Written By {book[1]}   Published: {book[2]}")
            print(f" \n")
            print(book[4])
            print(f"Genre : {book[3]}")
            print(f'\n')
            done_reading = questionary.confirm("Done Reading. Mark as readed").ask()
            print(f'\n')
            if(done_reading == True):
                  cursor.execute("UPDATE books SET ReadStatus = ? WHERE BookName = ?",(1,selected_book))
                  connection.commit()     
 # else return not found   
    else : print("No book found for this name")