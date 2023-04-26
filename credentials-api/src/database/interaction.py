from .connection import (
    connect,
    create_database
)
import json
from src.config import MONGO_CREDENTIALS_PATH
# with open(MONGO_CREDENTIALS_PATH, "r") as f:
#     credentials: dict = json.load(f)
# user = credentials.get("user")
# password = credentials.get("password")
# print(user, password)
client = connect(
    "mongodb+srv://rakeshhalijol:Rakesh123@cluster0.inydvtx.mongodb.net/test")
db = create_database(client=client, db_name="NATIVE-DATABASE")


# --- Create your collections here ---
User = db["User"]

# Write functions which interact with database


def create_user(userData: dict) -> str:
    user = User.insert_one(userData)
    return str(user.inserted_id)


def validate_user(userData: dict):
    user = User.find_one(userData)
    return user
