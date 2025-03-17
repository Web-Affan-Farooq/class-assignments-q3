# ____Function for displaying book details
import questionary
from modules import connection

db = connection.get_connection()
connection =  db["Connection"]
cursor = db["Cursor"]

def check_details():
    cursor.execute("SELECT * FROM books")
    connection.commit()
    rows = cursor.fetchall()
    options = [row[0] for row in rows]
    print(f"\n")
    selected_option = questionary.select("Select a book :", choices=options).ask()
    # print(f"Select option : {selected_option}")

    cursor.execute("SELECT * FROM books WHERE BookName = ?", (selected_option,))
    connection.commit()
    [book] = cursor.fetchall()
    print(f"\n")
    print(f"Book name :", book[0])
    print(f"Written by :", book[1])
    print(f"Published :", book[2])
    print(f"Genre :", book[3])
    print(f"Contains :", len(book[4].split(" ")) , "words")
    print(f"\n") 
    done_reading = questionary.confirm("Mark as done").ask()
    if(done_reading):
        cursor.execute("UPDATE books SET ReadStatus = ? WHERE BookName = ?",(1,selected_option))
        connection.commit()       