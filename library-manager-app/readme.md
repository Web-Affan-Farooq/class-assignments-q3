## Personal library manager application :

### Dependencies:
install the following dependencies
 ```bash
 pip install questionary pandas 
 ```

This project is using sqlite as database in python

 ### Guide for sqlite with python :

First create a file with .db extension then in python code configure it as 

 ```python
import sqlite3

FILE_PATH = "Your file path"

connnection = sqlite3.connect(FILE_PATH)
cursor = connnection.cursor()

 ```

 Create a table and commit it as

 ``` python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT
)
""")
connnection.commit()
 ```
 **example code**:

 ```python
import sqlite3

FILE_PATH = "Your file path"

connnection = sqlite3.connect(FILE_PATH)
cursor = connnection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    city TEXT
)
""")
connnection.commit()

# Fetchhing data from database 
cursor.execute("SELECT * FROM users")
 row = cursor.fetchAll()
 print(row)  
 ```

## Fetch data from table :
You can fetch data from table as 
```python
# Updating data
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",)) # always insert an extra comma
connnection.commit()
```
Or fetch all the data from the table 
```python
cursor.execute("SELECT * FROM users")
 row = cursor.fetchAll()
```
## Creating new entries:

Insert data into table as :
```python
# insert data into table :
cursor.executemany("INSERT INTO users (name, age,city) VALUES (?,?,?)",[
    ("Alice", 30, "London"),
    ("Bob", 22, "Paris"),
    ("Charlie", 35, "Berlin")
])
connnection.commit()
print("Data seeded successfully")
```
 or insert only one data into table

```python

# insert data into table :
cursor.execute("INSERT INTO users (name, age,city) VALUES (?,?,?)",("Alice", 30, "London"))
connnection.commit()
print("Data seeded successfully")
```

## Updating existing entries: 
Find and update the data as:
```python
# Updating data
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (90, "Alice"))
connnection.commit()
```

## Deleting data from table:
Delete the entry as :
```python 
cursor.execute("DELETE FROM users WHERE name = ?", ("Charlie",)) # always insert an extra comma
connnection.commit()
```