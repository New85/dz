import sqlite3 as sql


with sql.connect("bd.bd") as con:
    cur = con.cursor()

    cur.executescript('''
            create table if not exists person(
            f_name varchar(15),
            l_name varchar(15),
            cod int,
            open_accounts int);
    ''')

