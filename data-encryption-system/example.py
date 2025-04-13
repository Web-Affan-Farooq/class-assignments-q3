# from cryptography.fernet import Fernet
# key = Fernet.generate_key()

# f = Fernet(key)
# token = f.encrypt(b"hello world")
# decrypted = f.decrypt(token)
# print("Actual data : ", "hello world")
# print("encrypted : ", f.encrypt(b"hello world"))
# print("decrypted : ", decrypted)
# print("decoded : ", decrypted.decode())

from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os
from datetime import date
import json

load_dotenv()

key = os.getenv("KEY")
f = Fernet(key)
data = [
    {
        "id": 1,       
        "created": date.today().isoformat(),
        "text": "this is example data-1 ",
    },
    {
        "id": 2,
        "created": date.today().isoformat(),
        "text": "this is example data-2 ",
    },
    {
        "id": 3,
        "created": date.today().isoformat(),
        "text": "this is example data-3 ",
    },
    {
        "id": 4,
        "created": date.today().isoformat(),
        "text": "this is example data-4 ",
    },
    {
        "id": 5,
        "created": date.today().isoformat(),
        "text": "this is example data-5 ",
    },
]

string = json.dumps(data).encode()
encrypted = f.encrypt(string)
decrypted = f.decrypt(encrypted).decode()
print(encrypted)
# print("Decrypted data : ", type(json.loads(decrypted)))
# print((f.decrypt(encrypted)))
