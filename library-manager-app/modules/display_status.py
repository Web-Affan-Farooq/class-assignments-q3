# Function for displaying Current status of library:
from modules import connection

db = connection.get_connection()
connection =  db["Connection"]
cursor = db["Cursor"]

def display_status():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    current_status = {
        "Readed Books":[],
        "Not Readed":[],
        "Genres":{},
        "Read percentage":"",
        "Unread percentage":"",
    }

    for row in rows:
        if row[5]: 
            current_status["Readed Books"].append(row)
        else:
            current_status["Not Readed"].append(row)

        # Calculating genres occurence ...
        genre = row[3].lower() 
        if genre in current_status["Genres"]:
            current_status["Genres"][genre] += 1
        else:
            current_status["Genres"][genre] = 1
        
        calc_1 = int((len(current_status["Readed Books"]) / len(rows))*100)
        current_status["Read percentage"] = f"{abs(calc_1)}"
        calc_2 = 100-calc_1
        current_status["Unread percentage"] = f"{abs(calc_2)}" 

    print(f"""\n""") 
    print(f"------------Books Readed --------------- {len(current_status["Readed Books"])}")
    print(f"""\n""")
    print(f"------------Not Readed --------------- {len(current_status["Not Readed"])}")
    print(f"""\n""")
    print(f"------------Genres in collection --------------- ")
    print(f"""\n""")
    for item in current_status["Genres"]:
        print(f" {item} : {current_status["Genres"][item]}")
    
    print(f"""\n""")
    print(f"------------Total Books --------------- {len(current_status["Not Readed"]) + len(current_status["Readed Books"])}")
    print(f"""\n""")
    print(f"------------ {current_status["Read percentage"]} % books readed")
    print(f"""\n""")
    print(f"------------ {current_status["Unread percentage"]} % books remaining ")

    print(f"""\n""")