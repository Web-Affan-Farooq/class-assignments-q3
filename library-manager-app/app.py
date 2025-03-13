import questionary
import os

# ___Importing modules
from modules import display_all


# ____Welcome options :
options = [
     "Add new book to collection",
     "Remove an existing book",
     "Search for a specific book",
     "Check book details",
     "Display Status",
     "Exit",
]

# ____function for adding book in collection
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
            "name":"bookGenre",
            "message":"Enter Genre of book",
        },
    ]
    response = questionary.prompt(questions=questions)
    file = open(f"./data/{id(response)}.py", "a")
    file.write(str(response)) 

# while(True):
#     selected_option = questionary.select("What would you like to do", choices=options).ask()
#     if(selected_option == options[5]):
#         os._exit(0)

selected_option = questionary.select("What would you like to do", choices=options).ask()
if(selected_option == options[0]):
    add_book()