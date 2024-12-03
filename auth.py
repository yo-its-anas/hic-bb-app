# auth.py
import json

def create_user(username, password, email, phone, location, blood_group):
    with open("users.json", "r+") as file:
        users = json.load(file)
        if username in users:
            return "Username already exists."
        users[username] = {"password": password, "email": email, "phone": phone, "location": location, "blood_group": blood_group}
        file.seek(0)
        json.dump(users, file, indent=4)
        return "User created successfully!"

def authenticate_user(username, password):
    with open("users.json", "r") as file:
        users = json.load(file)
        if username in users and users[username]["password"] == password:
            return True
        return False
