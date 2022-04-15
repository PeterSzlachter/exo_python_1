from tinydb import TinyDB, Query, where
# from tinydb.storages import MemoryStorage
from pathlib import Path

CUR_DIR = Path(__file__).resolve().parent

db = TinyDB(CUR_DIR / "tinydatabase_2.json",indent=4)

users = db.table("Users")
roles = db.table("Roles")

users.insert({"name": "Peter","score": 10})

users.insert_multiple([
    {"name": "Jean","score": 15},
    {"name": "Pedro","score": 20}
])

roles.insert_multiple([
    {"roles": "Junior"},
    {"roles": "Senior"},
    {"roles": "Rien"}
])

