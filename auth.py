import json
import os

def create_user(username, password, email, phone, location, blood_group):
    if not os.path.exists("users.json"):
        with open("users.json", "w") as file:
            json.dump({}, file)
    
    with open("users.json", "r+") as file:
        users = json.load(file)
        if username in users:
            return "Username already exists."
        users[username] = {
            "password": password,
            "email": email,
            "phone": phone,
            "location": location,
            "blood_group": blood_group
        }
        file.seek(0)
        json.dump(users, file, indent=4)
        return "User created successfully!"

def login_user(username, password):
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            users = json.load(file)
            if username in users and users[username]["password"] == password:
                return True
    return False
