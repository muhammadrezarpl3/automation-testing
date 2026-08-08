import json
from pathlib import Path


def load_users():
    file_path = Path(__file__).parent.parent / "users.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    return data["users"]