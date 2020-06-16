""" Plik generujący losowe dane do bazy danych """

from random import randint
import sqlite3
import datetime

conn = sqlite3.connect("database.db")
cur = conn.cursor()
list1=[]
tables=[
    'DOCHOD_ZE_SPRZEDAZY',
    'INNE',
    'PENSJE_PRACOWNIKOW',
    'PODATKI_I_CZYNSZE',
]
for i in range(2400):
    table = randint(0,3)
    month = randint(1,9)
    day = randint(1,28)
    money = randint(1,5000)
    if table == 1:
        t = randint(0,1)
        if t==0:
            money = -money
    if table == 2 or table == 3:
        money = - money
    if table ==0:
        money = 5*money
    date = datetime.date(year=2020,month=month, day=day)
    date = datetime.date.strftime(date, "%Y-%m-%d")
    cur.execute("INSERT INTO {} VALUES({},'{}',{},'');".format(tables[table], i, date, money))

conn.commit()
conn.close()

    



