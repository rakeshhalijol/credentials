from .connection import (
    connect,
    create_database
)

client = connect("mongodb://13.48.132.14 :27017")
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
