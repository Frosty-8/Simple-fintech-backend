import json
from pathlib import Path

from utils.generators import (
    generate_user_id,
    generate_wallet_id
)
from utils.hashing import hash_password

USER_FILE = Path("users/users.json")

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            data = json.load(file)

        if "users" not in data:
            data = {"users": []}
        
        return data
    
    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):
        return {"users": []}
    
def save_users(data):
    with open(USER_FILE, "w") as file:
        json.dump(
            data, file, indent=4
        )

def get_user_by_email(email: str):
    data = load_users()

    for user in data["users"]:
        if user["email"] == email:
            return user
        
    return None

def create_user(
        name: str,
        email: str,
        password: str
):
    data = load_users()

    if get_user_by_email(email):
        raise Exception(
            "Email already registered"
        )
    
    user_id = generate_user_id()
    wallet_id = generate_wallet_id()

    user = {
        "id": user_id,
        "name": name,
        "email": email,
        "password": hash_password(password),
        "wallet_id": wallet_id
    }

    data["users"].append(user)
    save_users(data)

    return user