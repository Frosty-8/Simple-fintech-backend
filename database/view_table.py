import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("wallet.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT * FROM wallets")
rows = cursor.fetchall()

print(tabulate(
    [dict(row) for row in rows],
    headers="keys",
    tablefmt="grid"
))

conn.close()