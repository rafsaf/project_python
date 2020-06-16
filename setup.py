""" Plik instalacyjny, w pierwszym uruchomieniu tworzy tabele w bazie danych(i baze jesli jej nie ma), w pp. tabele juz istnieja wiec program nie robi nic. """
import sqlite3


if __name__ == '__main__':
    try:
        conn = sqlite3.connect('database.db')
        cur = conn.cursor()

        cur.execute("""CREATE TABLE PODATKI_I_CZYNSZE(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CZAS TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
            BILANS INTEGER NOT NULL,
            ADNOTACJA TEXT,
            CHECK(BILANS <=0)
            );""")
        cur.execute("""CREATE TABLE DOCHOD_ZE_SPRZEDAZY(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CZAS TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
            BILANS INTEGER NOT NULL,
            ADNOTACJA TEXT,
            CHECK(BILANS >=0)
            );""")
        cur.execute("""CREATE TABLE PENSJE_PRACOWNIKOW(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CZAS TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
            BILANS INTEGER NOT NULL,
            ADNOTACJA TEXT,
            CHECK(BILANS <=0)
            );""")
        cur.execute("""CREATE TABLE INNE(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            CZAS TIMESTAMP NOT NULL DEFAULT CURRENT_DATE,
            BILANS INTEGER NOT NULL,
            ADNOTACJA TEXT
            );""")
        cur.close()
        conn.close()
    except Exception:
        pass
