# ___function for removing book :
import pandas as pd
import questionary
from modules import connection

db = connection.get_connection()
connection =  db["Connection"]
cursor = db["Cursor"]


def remove_book():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    options = [row[0] for row in rows]  # filtering book name from list of tuples
    book_tobe_deleted = questionary.select("Select a book to be deleted from collection", choices=options).ask()
    
    # Deleting book from database ...
    cursor.execute("DELETE FROM books WHERE BookName = ? ", (book_tobe_deleted,))
    connection.commit()

# getting newly refreshed data from database
    cursor.execute("SELECT * FROM books")
    del(rows)
    rows = cursor.fetchall()
   
    new_list = []
    for row in rows:
        if(row[5]):
            new_list.append({
            "Name":row[0],
            "Author":row[1],
            "Readed": "Done"
            })
        else : 
            new_list.append({
            "Name":row[0],
            "Author":row[1],
            "Readed": "Not readed yet"
            })
    # Creating command line table
    dt = pd.DataFrame(new_list, columns=["Name","Author","Readed"])
    print(f"\n")
    print(f"Deleting item {book_tobe_deleted} ...")
    print(f"\n")
    print(f"------------------------Book Deleted successfully --------------------------")
    print(f"\n")
    print("""
--------------Remaining books :
    
""")
    print(dt)
    print(f"\n")
    print(f"\n")