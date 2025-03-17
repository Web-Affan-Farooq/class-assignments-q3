# ____function for adding book in collection

import questionary
from modules import connection  # importing database configuration
import pandas as pd

# Getting methods returned by get_connection function
db = connection.get_connection()
connection =  db["Connection"]
cursor = db["Cursor"]

def add_book():
    questions = [
        {
            "type":"text",
            "name":"bookName",
            "message":"Enter book name",
        },
        {
            "type":"text",
            "name":"authorName",
            "message":"Enter author name",
        },
        {
            "type":"text",
            "name":"publication",
            "message":"Enter publication year",
        },
        {
            "type":"text",
            "name":"bookContent",
            "message":"Enter book content here ...",
        },
        {
            "type":"text",
            "name":"bookGenre",
            "message":"Enter Genre of book",
        },
    ]
    response = questionary.prompt(questions=questions)

    # Inserting book into database
    cursor.execute("INSERT INTO books (BookName, AuthorName, Publication, Genre, Description , ReadStatus) VALUES (?,?,?,?,?,?)", (
        response["bookName"],
        response["authorName"],
        response["publication"],
        response["bookGenre"],
        response["bookContent"],
        0,
    ))
    connection.commit()

    # Fetching all books from database
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

# Creating more concise list ...
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
    dt = pd.DataFrame(new_list, columns=["Name","Author","Readed"])
    print(f"\n")
    print(f"Adding 1 item ...")
    print(f"\n")
    print(f"------------------------Book Added Successfully --------------------------")
    print(f"\n")
    print("""
-------------- All Books : ------------------------------
    
""")
    print(dt)
    print(f"\n")
    print(f"\n")