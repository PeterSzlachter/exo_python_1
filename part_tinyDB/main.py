#Poids très faible, 1k8 ligne de code dont 40% de doc
#Simple d'utilisation
#100% python (pas besoin de serveur/dépendance externe)
from tinydb import TinyDB, Query, where
# from tinydb.storages import MemoryStorage
from pathlib import Path

CUR_DIR = Path(__file__).resolve().parent

db = TinyDB(CUR_DIR / "tinydatabase.json",indent=4)
# db = TinyDB(storage=MemoryStorage)
# db.insert({"name": "Peter","score": 10})

# db.insert_multiple([
#     {"name": "Jean","score": 15},
#     {"name": "Pedro","score": 20}
# ])

User =  Query()
pedro = db.search(User.name == "Pedro")  # type: ignore
pedro_unique = db.get(User.name == "Peter")  # type: ignore
print(pedro)
print(pedro_unique)

high_score = db.search(where("score") > 10)  # type: ignore
print(high_score)
print(len(db))
print(db.contains(User.name == ""))  # type: ignore
print(db.count(User.name == "Peter"))  # type: ignore

db.update({"score": 27}, where("name") == "Pedro")  # type: ignore
db.update({"roles": ["Junior"]})
db.update({"roles": ["Alternant", "Junior"]}, where("name") == "Peter")  # type: ignore
db.upsert({"name": "Manu", "score": 20, "roles": ["Senior"]}, where("name") == "Manu")  # type: ignore
db.remove(where("name") == "Manu")  # type: ignore
# db.truncate()