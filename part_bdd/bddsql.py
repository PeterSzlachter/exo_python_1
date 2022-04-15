import sqlite3
from pathlib import Path

CUR_DIR = Path(__file__).resolve().parent

conn = sqlite3.connect(CUR_DIR / "database.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS employees
(
    prenom text,
    nom text,
    salaire int
)
""")
data_1 = {"salaire": 10000, "prenom": "Patrick", "nom": "Dupont"}

c.execute("INSERT INTO employees VALUES (:prenom, :nom,:salaire)", data_1)

data_2 = {"salaire": 10000, "prenom": "Patrick", "nom": "Dupont"}

c.execute("""UPDATE employees SET salaire=:salaire
WHERE prenom=:prenom AND nom=:nom""", data_2)

# c.execute("DELETE FROM employees WHERE prenom='Patrick'")
conn.commit()
conn.close()

# c.execute("INSERT INTO employees (prenom,nom) VALUES(:a,:b)", d)
# c.execute("SELECT * FROM employees WHERE prenom = :a",d)
# datas = c.fetchall()
# print(datas)
