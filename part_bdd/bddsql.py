import sqlite3
from pathlib import Path

CUR_DIR = Path(__file__).resolve().parent

conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees
(
    prenom text,
    nom text,
    salaire int
)
""")

d = {"salaire": 20000, "prenom": "Patrick", "nom": "Dupont"}

c.execute("""UPDATE employees SET salaire=:salaire
WHERE prenom=:prenom AND nom=:nom""", d)

conn.commit()
conn.close()

# c.execute("INSERT INTO employees (prenom,nom) VALUES(:a,:b)", d)
# c.execute("SELECT * FROM employees WHERE prenom = :a",d)
# datas = c.fetchall()
# print(datas)
