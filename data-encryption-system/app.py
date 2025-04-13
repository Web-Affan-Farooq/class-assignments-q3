import streamlit as st
from cryptography.fernet import Fernet

# from dotenv import load_dotenv
import json
from datetime import date

key = st.secrets["KEY"]
f = Fernet(key.encode())

if (
    "users" not in st.session_state
    and "is_login" not in st.session_state
    and "current_user" not in st.session_state
    and "login_attemps_count" not in st.session_state
    and "edit_mode" not in st.session_state
):
    st.session_state.users = [
        {
            "id": 1,
            "name": "affan",
            "password": b"gAAAAABn-2fYIDphRf3W6PA_a4UMuFUdbWEIIetUC6gFcIUy0sh5v5wlTP9U640lq5xxBX-WzAEu-dB56bfeGlKq0ai3Fp82iQ==",
            "data": b"gAAAAABn-6UGDsB3JNcgFUP9IHanlkTKekjD5y2QcPpE5vs9euMm-pLvrcrwv93KJORSdUqnas-7eFeo3NbKTvmzoYDchDqasVKp5GNVWhgi3bSBlh0lg0hoDj4c85aEEg0g-U5Itzm13ac4GwfTGbhz4IhwM_z-RzM-nSChZ9v503MKjjRyl6tysYtBEzSQmxDNwnB57YeKx28gU-z5DBM59qvJoNz3J0XZ04cVAfdjEfjeiNgt2CNQNwu4WLyLx7u_r1PSbDusy4wzVqhCzOzLRziecEQMsI5OSBXZoJ3AK3rHOa7CoCyPWAkRUMqCE9nciHmqQl5JnW2uXYKykbxYfLNhd8yRZ6UN0U5zBndk6afetmRvGa4FMcbsK6RpcFzsCLMrLvOwBolJZ7A9v1fA_TXBYGoQUbHOFBcpUNwkNJXLRPltEvGSlBDssqmubejFM8HqVwynYcS5YM42lZQpWgjxd6KY-OzHr8--6Ym2GdcwNBEgOdRvdBRj7yT9dyFpbzahBrEDf-IFjilCMFUZ953rM_nwwLlpFvwL5DniNnBI6QiSlus=",
        },
        {
            "id": 2,
            "name": "aqib",
            "password": b"gAAAAABn-2h78qb-o6mNztVPyeo3K0MH8H1P-szcg-GqcNbsvXdBAUaOfXj1Dv9L1S9r7wp5TotdsDxDf_xjOFyBOAmB7wBKQA==",
            "data": b"gAAAAABn-6UGDsB3JNcgFUP9IHanlkTKekjD5y2QcPpE5vs9euMm-pLvrcrwv93KJORSdUqnas-7eFeo3NbKTvmzoYDchDqasVKp5GNVWhgi3bSBlh0lg0hoDj4c85aEEg0g-U5Itzm13ac4GwfTGbhz4IhwM_z-RzM-nSChZ9v503MKjjRyl6tysYtBEzSQmxDNwnB57YeKx28gU-z5DBM59qvJoNz3J0XZ04cVAfdjEfjeiNgt2CNQNwu4WLyLx7u_r1PSbDusy4wzVqhCzOzLRziecEQMsI5OSBXZoJ3AK3rHOa7CoCyPWAkRUMqCE9nciHmqQl5JnW2uXYKykbxYfLNhd8yRZ6UN0U5zBndk6afetmRvGa4FMcbsK6RpcFzsCLMrLvOwBolJZ7A9v1fA_TXBYGoQUbHOFBcpUNwkNJXLRPltEvGSlBDssqmubejFM8HqVwynYcS5YM42lZQpWgjxd6KY-OzHr8--6Ym2GdcwNBEgOdRvdBRj7yT9dyFpbzahBrEDf-IFjilCMFUZ953rM_nwwLlpFvwL5DniNnBI6QiSlus=",
        },
    ]
    st.session_state.is_login = False
    st.session_state.current_user = {}
    st.session_state.login_attemps_count = 0
    st.session_state.edit_mode = False


def Login():
    if st.session_state.login_attemps_count >= 3:
        st.html(
            """
                <script>window.close()
                alert("Only 3 attemps allowed")</script>"""
        )
        st.toast("Only 3 login attemps allowed")
    else:
        name = st.text_input("Enter username")
        password = st.text_input("Enter you password", type="password")
        if st.button("Login"):
            required = {}
            for user in st.session_state.users:
                decrypted = f.decrypt(user["password"]).decode()  # decrypt the password
                # st.write("Password : ", password)
                # st.write("decrypted: ", decrypted)
                # st.write(password == decrypted)
                if user["name"] == name and password == decrypted:
                    required = user
                else:
                    pass
            # st.write(required)
            if len(required) > 0:
                st.session_state.is_login = True
                st.session_state.current_user = required
                # st.write("login status : ", st.session_state.is_login)
                st.toast("Login successfull")
                st.rerun()
            else:
                st.session_state.login_attemps_count += 1
                st.toast("Invalid username or password")


def Signup():
    name = st.text_input("Enter your name")
    password = st.text_input("Set a password to your account")

    if st.button("Signup"):
        if name != "" and password != "":
            user_data = {
                "id": st.session_state.users[-1]["id"] + 1,
                "name": name,
                "password": f.encrypt(password.encode()),
                "data": f.encrypt(json.dumps([]).encode()),
            }

            already_exists = {}  # __ dictionary containing already exist account
            for user in st.session_state.users:
                if (
                    name == user["name"]
                    and f.decrypt(user["password"]).decode() == password
                ):
                    already_exists = user
                else:
                    pass

            if len(already_exists) <= 0:
                # st.write("User already exists : ", already_exists)
                # st.write("user dict : ", user_data)
                st.session_state.users.append(user_data)
                st.session_state.is_login = True
                st.session_state.current_user = user_data
                st.toast("Account created successfully")
                st.rerun()
            else:
                st.toast("Account already exists ")

        else:
            st.warning("Please enter a valid name and password")


def show_data():
    st.write("#### Add data")

    user = st.session_state.current_user
    decrypted_data = f.decrypt(user["data"]).decode()
    parsed_data = json.loads(decrypted_data)
    text = st.text_area("Enter text to add in your collection")

    if st.button("Add"):
        if text != "":
            if len(parsed_data) > 0:
                id_to_be_assigned = parsed_data[-1]["id"] + 1
                parsed_data.append(
                    {
                        "id": id_to_be_assigned,
                        "text": text,
                        "created": date.today().isoformat(),
                    }
                )
                json_converted_string = json.dumps(parsed_data).encode()
                # st.write("json converted string : ", json_converted_string)
                encrypted_new_list = f.encrypt(json_converted_string)
                # st.write("encryoted list : ", encrypted_new_list)
                user["data"] = encrypted_new_list
                # st.write("user data after ", user)
                idx = st.session_state.users.index(user)
                st.session_state.users[idx] = user
                st.toast("Added successfully")
                st.rerun()
            else:
                parsed_data.append(
                    {
                        "id": 1,
                        "text": text,
                        "created": date.today().isoformat(),
                    }
                )
                json_converted_string = json.dumps(parsed_data).encode()
                # st.write("json converted string : ", json_converted_string)
                encrypted_new_list = f.encrypt(json_converted_string)
                # st.write("encryoted list : ", encrypted_new_list)
                user["data"] = encrypted_new_list
                # st.write("user data after ", user)
                idx = st.session_state.users.index(user)
                st.session_state.users[idx] = user
                st.toast("Added successfully")
                st.rerun()

        st.write("---")

        st.write("#### Your collection ")
        st.write(" ")
        st.write(" ")
    if len(parsed_data) <= 0:
        st.write(" ")
        st.write(" ")
        st.write("Your collection is empty .  .  .")
    else:
        for dictionary in parsed_data:
            st.write(f"##### {dictionary["text"]}")
            st.write(f"Added to collections on _{dictionary["created"]}_")
            # st.write("id : ",dictionary["id"])
            st.write(" ")

            if st.button("Delete", key=f"{dictionary['id']}"):
                # st.toast("Data deleted from collections successfully") # toast is not working
                parsed_data.remove(dictionary)
                json_converted_string = json.dumps(parsed_data)
                encrypted_new_list = f.encrypt(json_converted_string.encode())
                # st.write("Encrypted string : ", encrypted_new_list)
                user["data"] = encrypted_new_list
                idx = st.session_state.users.index(user)
                st.session_state.users[idx] = user
                # print(st.session_state.users[idx])  ## __check the data of the updated account
                st.rerun()
            st.write("---")
            st.write(" ")
            st.write(" ")
            st.write(" ")


def account_info(user):
    decrypted_password = f.decrypt(user["password"]).decode()
    st.write(decrypted_password)
    # json_parsed_string = json.loads(decrypted)

    st.write(f"#### Username : {user['name']}")
    st.write(f"#### Account password : {decrypted_password}")

    if st.button("Edit credentials"):
        st.session_state.edit_mode = True

    if st.session_state.get("edit_mode", False):
        name = st.text_input("Your username:", value=user["name"], key="edit_name")
        password = st.text_input(
            "Your password:", value=decrypted_password, key="edit_pass"
        )

        if st.button("Save", key="save_button"):
            encrypted_password = f.encrypt(password.encode())
            new_info = {
                "id": user["id"],
                "name": name,
                "password": encrypted_password,
                "data": user["data"],
            }

            for i, u in enumerate(st.session_state.users):
                if u["id"] == user["id"]:
                    st.session_state.users[i] = new_info
                    break

            st.success("✅ User credentials updated.")
            # st.write("Edited user's credentials:", new_info)
            st.session_state.current_user = new_info
            st.session_state.edit_mode = False  # Reset


st.title("Data encryption system")
st.write("---")
menu = []
if not st.session_state.is_login:
    menu = ["Login", "Signup", "Test"]
else:
    menu = ["Your collection", "Log out", "Your account", "Test"]

option = st.sidebar.selectbox("Sidebar ", menu)

if option.lower() == "login":
    st.write("#### Login to your account")
    Login()
elif option.lower() == "signup":
    st.write("#### Create account")
    Signup()
elif option.lower() == "your collection":
    show_data()
elif option.lower() == "log out":
    st.session_state.is_login = False
    st.session_state.current_user = {}
    st.rerun()
elif option.lower() == "your account":
    account_info(st.session_state.current_user)
elif option.lower() == "test":
    st.write("Current session state : ", st.session_state)
    st.write("Current user : ", st.session_state.current_user)
    st.write("Is login : ", st.session_state.is_login)
