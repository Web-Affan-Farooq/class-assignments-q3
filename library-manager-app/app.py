import questionary # inquirer like console interface creator
import os

# ___Importing modules
from modules import connection  #  important ! : database connectivity configuration
from modules import add_book
from modules import remove_book
from modules import search_book
from modules import check_details
from modules import check_collection
from modules import display_status

# Connection methods ...
db = connection.get_connection()
connection =  db["Connection"]
cursor = db["Cursor"]


# ____Welcoming options :
options = [
     "Add new book to collection", 
     "Remove an existing book", 
     "Search for a specific book", 
     "Check book details", 
     "Check collection",
     "Display Status", 
     "Exit",
]


while(True):

    selected_option = questionary.select("What would you like to do", choices=options).ask()
    if(selected_option == options[0]):
        add_book.add_book()
    elif(selected_option == options[1]):
        remove_book.remove_book()
    elif(selected_option == options[2]):
        search_book.search_book()
    elif(selected_option == options[3]):
        check_details.check_details()
    elif(selected_option == options[4]):
        check_collection.check_collection()
    elif(selected_option == options[5]):
        display_status.display_status()
    elif(selected_option == options[6]):
        os._exit(0)