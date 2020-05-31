import os
import sqlite3

BASE_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(BASE_DIR, 'Dane.csv')

if __name__ == '__main__':
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Bilans(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Czas TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        Waga INTEGER NOT NULL DEFAULT 2,
        Bilans INTEGER NOT NULL,
        Opis TEXT,
        CHECK(Waga >= 0 AND Waga <= 10)
        );""")
