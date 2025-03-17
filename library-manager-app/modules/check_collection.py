# ____Function for displaying all books

from modules import connection
import pandas as pd

db = connection.get_connection()
connection =  db["Connection"]
cursor = db["Cursor"]

def check_collection():
    cursor.execute("SELECT * FROM books")
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
    dt = pd.DataFrame(new_list, columns=["Name","Author","Readed"])
    print(f"\n")
    print(f"\n")
    print(dt)
    print(f"\n")
    print(f"\n")